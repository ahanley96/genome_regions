import unittest
from genome_regions2 import determine_overlap

class TestRegionOverlap(unittest.TestCase):

    def test_determine_overlap_no_overlap(self):
        region1 = (1, 10)
        region2 = (11, 20)
        result = determine_overlap(region1, region2)
        self.assertEqual(result, 0)

    def test_determine_overlap_partial_overlap(self):
        region1 = (5, 15)
        region2 = (10, 20)
        result = determine_overlap(region1, region2)
        self.assertEqual(result, 5)
        
        
if __name__ == "__main__":
    unittest.main()
