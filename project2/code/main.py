import help_func as hf
import find_visible as fv
import json
import time


# read data from test files
test_set = hf.read_data('../data/test_set.txt')
exp_set = hf.read_data('../data/solve_these.txt')
test_lines = hf.create_line(test_set)
exp_lines = hf.create_line(exp_set)

plot_data = open('../data/plotdata4.json', 'w+')


for i,lines in enumerate(test_lines):
	test = fv.FindVisible_4(lines)
	print 'Test:   '+str(hf.bool_list(test,len(lines)))
	print 'Answer: '+str(test_set[i][2])+'\n'

for i,lines in enumerate(exp_lines):
	test = fv.FindVisible_4(lines)
	test_1 = fv.FindVisible_2(exp_set[i][0],exp_set[i][1])
	alg4 = hf.bool_list(test,len(lines))
	alg1 = test_1
	# print alg1
	if alg1 != alg4:
		print 'algr4 does not match algr1'
	else:
		print 'success'

#running time analysis
size = range(100,1000,100)+range(1000,10000,1000)
runtime4 = []

print '\nAlg 4:'
for n in size:
	data = hf.generate_data(n)
	lines = hf.create_line_new(data)
	start = time.time()
	result = fv.FindVisible_4(lines)
	end = time.time()-start
	runtime4.append(end)
	print 'Time: '+str(end)

json.dump(runtime4, plot_data)
plot_data.close()
