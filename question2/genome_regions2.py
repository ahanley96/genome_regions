
import csv

# Calculates the overlap between two regions regions
def determine_overlap(region1, region2):
    start1, end1 = region1
    start2, end2 = region2
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    return max(0, overlap_end - overlap_start)


def process_segments(input_file, output_file):
    
    genome_regions = []

    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            start, end = map(int, row)
            genome_regions.append((start, end))

    segments = []
    for region in genome_regions:
        start, end = region
        overlapping = False
        for segment in segments:
            ## 
            # If the you find a region to be overlapping, determine 
            # the min and max length of the segment and increase it's count by 1.
            ##
            if determine_overlap(region, segment[1:]) > 0:
                overlapping = True
                segment[0] += 1
                segment[1] = min(segment[1], start)
                segment[2] = max(segment[2], end)
                break
            ##
            # Else, add it to the segements array as only seen once along with 
            # the start and co-ordinates it was seen at.
            ##
        if not overlapping:
            segments.append([1, start, end])

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        for segment in segments:
            writer.writerow(segment)
            
if __name__ == "__main__":
    
    input_file = '../input/regions_big.txt'
    output_file = '../output/q2.txt'
    process_segments(input_file, output_file)
