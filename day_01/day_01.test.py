import unittest
from day_01 import calculate_frequency, calculate_same_frequency_result

class day_one_test(unittest.TestCase):
	def test_equal_1(self):
		input=[1,-2,3,1]
		self.assertEqual(calculate_frequency(input),3)

	def test_equal_2(self):
		input=[1,1,1]
		self.assertEqual(calculate_frequency(input),3)

	def test_equal_3(self):
		input=[1,1,-2]
		self.assertEqual(calculate_frequency(input),0)

	def test_equal_4(self):
		input=[-1,-2,-3]
		self.assertEqual(calculate_frequency(input),-6)

	def test_equal_twice_1(self):
		input=[1,-1]
		self.assertEqual(calculate_same_frequency_result(input),0)

	def test_equal_twice_2(self):
		input=[3,3,4,-2,-4]
		self.assertEqual(calculate_same_frequency_result(input),10)

	def test_equal_twice_3(self):
		input=[-6,3,8,5,-6]
		self.assertEqual(calculate_same_frequency_result(input),5)

	def test_equal_twice_4(self):
		input=[7,7,-2,-7,-4]
		self.assertEqual(calculate_same_frequency_result(input),14)

if __name__ == '__main__':
	unittest.main()
