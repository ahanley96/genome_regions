import os 

# Define the input and output file names



def process_input(input_file_name, output_file_name):

    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        row_number = 1
        for line in input_file:
            integers = line.strip().split('\t')
            # Check if there are exactly two integers in the line
            if len(integers) == 2:
                int1, int2 = integers
                output_file.write(f"{row_number}\t{int1}\t{int2}\n")
                row_number += 1
            else:
                # Handle cases where the line doesn't contain two integers
                print(f"File does not contain correct integers for start and end co-ords. {row_number}: {line.strip()}")


if __name__ == "__main__":
    
    input_file_name = "../input/regions_small.txt"
    output_file_name = "../output/q1.txt"
    
    process_input(input_file_name, output_file_name)