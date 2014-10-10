import random

def generate_data(n):
	slope = random.sample(range(-n,n),n)
	slope.sort()
	intersect = random.sample(range(-n,n),n)
	return [slope, intersect]