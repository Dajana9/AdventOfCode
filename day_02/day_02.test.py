import unittest
from day_02 import checksum, findCorrectLetters
from input import large_input

class day_two_test(unittest.TestCase):
	def test_equal_1(self):
		input=["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
		self.assertEqual(checksum(input),12)

	def test_equal_2(self):
		self.assertEqual(checksum(large_input),5952)

	def test_equal_3(self):
		input = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
		self.assertEqual(findCorrectLetters(input),"fgij")	

	def test_equal_4(self):
		self.assertEqual(findCorrectLetters(large_input),"krdmtuqjgwfoevnaboxglzjph")

if __name__ == "__main__":
	unittest.main()