def read_data(file_name):
	matrix=[]
	with open(file_name, 'r') as f:
		m = int(f.readline().rstrip())
		n = int(f.readline().rstrip())
		for line in f:
			tmp = [int(i) for i in line.split()]
			matrix.append(tmp)
	return (matrix,m,n)


def write_data(stack,score,file_name):
	output = open(file_name, 'w+')
	output.write(str(score)+'\n')
	l = len(stack)
	output.write(str(l)+'\n')
	for i in range(l):
		tmp = ' '.join(map(str,stack.pop()))+'\n'
		output.write(tmp)



