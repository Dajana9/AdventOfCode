def calculate_frequency(frequency_list):
	frequency_sum = 0
	for frequency in frequency_list:
		frequency_sum += frequency
	return frequency_sum


def calculate_same_frequency_result(frequency_list):
	frequency_sum = 0
	frequency_sum_list= {frequency_sum}
	while True:
		for frequency in frequency_list:
			frequency_sum = frequency_sum + frequency
			if frequency_sum in frequency_sum_list:
				return frequency_sum
			else:
				frequency_sum_list.add(frequency_sum)