import json

def read_data(file_name):
	with open(file_name) as f:
		# convert each line into nested list
		tmp = [line.rstrip('\r\n').replace('],', '];').replace('True', 'true').replace('False', 'false').split('; ') for line in f]
		data = [map(json.loads, line) for line in tmp]
	return data

