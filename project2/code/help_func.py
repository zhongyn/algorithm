import json
import random

class line:
	def __init__(self, index, slope, intersect):
		self.m = slope
		self.b = intersect
		self.id = index	

def read_data(file_name):
	with open(file_name) as f:
		# convert each line into nested list
		tmp = [line.rstrip('\r\n').replace('],', '];').replace('True', 'true').replace('False', 'false').split('; ') for line in f]
		data = [map(json.loads, line) for line in tmp]
	return data

def format_solution(s):
	return s.lstrip('[').rstrip(']').replace('true', 'True').replace('false', 'False')

def generate_data(n):
	slope = random.sample(range(-n,n),n)
	slope.sort()
	intersect = random.sample(range(-n,n),n)
	return [slope, intersect]

def create_line(test_set):
	lines_set = []
	for instance in test_set:
		lines = [line(i,instance[0][i],instance[1][i]) for i in range(len(instance[0]))]
		lines_set.append(lines)
	return lines_set

def create_line_new(data):
	return [line(i,slope,data[1][i]) for i, slope in enumerate(data[0])]

def bool_list(lines, n):
	result = [False]*n
	for l in lines:
		result[l.id] = True
	return result 








