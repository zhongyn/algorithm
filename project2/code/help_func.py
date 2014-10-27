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

def read_line(test_set):
	lines_set = []
	for instance in test_set:
		lines = [line(i,instance[0][i],instance[1][i]) for i in range(len(instance[0]))]
		lines_set.append(lines)
	return lines_set

def print_visible(lines):
	print 'visible line:'
	for l in lines:
		print l.id
