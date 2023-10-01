import unittest
import tempfile
import os
from genome_regions1 import process_input

class TestProcessInputFile(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def test_process_input_file_valid(self):
        input_file_name = os.path.join(self.test_dir, 'test_input.txt')
        output_file_name = os.path.join(self.test_dir, 'test_output.txt')
        with open(input_file_name, 'w') as input_file:
            input_file.write("31744131\t31744131\n31811117\t31858544\n")

        process_input(input_file_name, output_file_name)

        with open(output_file_name, 'r') as output_file:
            result = output_file.read()
        self.assertEqual(result, "1\t31744131\t31744131\n2\t31811117\t31858544\n")
        
if __name__ == '__main__':
    unittest.main()
