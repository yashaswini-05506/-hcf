import unittest
from unittest.mock import patch
import sys
from hcf_lcm import hcf  # import hcf function from main program

# Function to calculate HCF and LCM for testing
def calculate_hcf_lcm(a, b):
    h = hcf(a, b)
    l = (a * b) // h
    return h, l

class TestHCFLCM(unittest.TestCase):

    @patch('sys.argv', ['hcf_lcm.py', '12', '18'])
    def test_case1(self):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        h, l = calculate_hcf_lcm(a, b)
        self.assertEqual(h, 6)
        self.assertEqual(l, 36)

    @patch('sys.argv', ['hcf_lcm.py', '20', '30'])
    def test_case2(self):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        h, l = calculate_hcf_lcm(a, b)
        self.assertEqual(h, 10)
        self.assertEqual(l, 60)

    @patch('sys.argv', ['hcf_lcm.py', '7', '5'])
    def test_case3(self):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        h, l = calculate_hcf_lcm(a, b)
        self.assertEqual(h, 1)
        self.assertEqual(l, 35)

if __name__ == "__main__":
    unittest.main()
