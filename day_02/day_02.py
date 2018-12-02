def checksum(box_Ids):
	multiply = {2:0,3:0}
	for element in box_Ids:
		char_count_dict = {}
		for char in element:
			if char in char_count_dict:
				char_count_dict[char] +=1
			else:
				char_count_dict[char] = 1

		if 3 in char_count_dict.values():
			multiply[3] +=1
		if 2 in char_count_dict.values():
			multiply[2] +=1
	return multiply[2] * multiply[3]

def findCorrectLetters(box_Ids):
	for reference in box_Ids:
		for element in box_Ids[1:]:
			result = []
			different_elements = 0
			index = 0
			for index in range(len(reference)):
				if reference[index] != element[index]:
					different_elements += 1
					if different_elements > 1:
						break
				else:
					result.append(reference[index])
			if different_elements == 1:
				final_result = ''.join(result)
				return final_result
