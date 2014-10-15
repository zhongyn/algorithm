import json
import random

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