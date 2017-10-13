# Idea is to generate the first n lines of the following pattern where we read
# the previous pattern and write how we say the written number
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221

import sys


def generate_see_say_pattern(num_iterations):
	if (num_iterations <= 0):
		return ""
	prev_pattern = "1"

	for i in xrange(num_iterations - 1):
		count = 1
		prev_char = prev_pattern[0]
		pattern = ""
		for char in prev_pattern[1:]:
			if (char == prev_char):
				count += 1
			else:
				pattern += "{}{}".format(count, prev_char)
				count = 1
			prev_char = char
		pattern += "{}{}".format(count, prev_char)
		prev_pattern = pattern
	return prev_pattern

if __name__ == '__main__':
	if len(sys.argv)!= 2:
		raise ValueError("wrong number of args, should be 2 instead of {}".format(len(sys.argv)))
	print generate_see_say_pattern(int(sys.argv[1]))

		
