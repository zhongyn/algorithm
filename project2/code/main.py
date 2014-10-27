import help_func as hf
import find_visible as fv
import json
import time


# read data from test files
test_set = hf.read_data('../data/test_set.txt')
lines_set = hf.read_line(test_set)

# test = fv.FindVisible_4(lines_set[2])

for lines in lines_set:
	test_1 = fv.FindVisible_4(lines)
	hf.print_visible(test_1)

