import help_func as hf
import find_visible as fv
import json
import time

# read data from test files
test_set = hf.read_data('../data/test_set.txt')
exp_test = hf.read_data('../data/solve_these.txt')
exp_result = open('../data/solution.txt', 'w+')
plot_data = open('../data/plotdata.txt', 'w+')

# test case of two lines
two_line = [[1,4],[2,-2]]
test = fv.FindVisible_1(two_line[0],two_line[1])
print 'Test:   '+ str(test)
print 'Answer: [True, True]\n'

# run test_set
fail = [0,0,0]
for instance in test_set:
	test_1 = fv.FindVisible_1(instance[0],instance[1])
	test_2 = fv.FindVisible_2(instance[0],instance[1])
	test_3 = fv.FindVisible_3(instance[0],instance[1])
	print 'Test_1: '+str(test_1)
	print 'Test_2: '+str(test_2)
	print 'Test_3: '+str(test_3)
	print 'Answer: '+str(instance[2])+'\n'
	if test_1!=instance[2]: fail[0]+=1
	if test_2!=instance[2]: fail[1]+=1
	if test_3!=instance[2]: fail[2]+=1

print 'Total number of test set: '+str(len(test_set))
print 'Fail:\nTest_1: '+str(fail[0])+'\nTest_2: '+str(fail[1])+'\nTest_3: '+str(fail[2])+'\n'

# run experiment test
for instance in exp_test:
	result = fv.FindVisible_3(instance[0],instance[1])
	exp_result.write(hf.format_solution(json.dumps(result))+'\n')
exp_result.close()

#running time analysis
size1 = range(100,1000,100) 
size = range(100,1000,100)+range(1000,10000,1000)
runtime = []
plotdata = [size]

print 'Algorithm 1\n'
for n in size1:
	data = hf.generate_data(n)
	start = time.time()
	result = fv.FindVisible_1(data[0],data[1])
	end = time.time()-start
	runtime.append(end)
	print 'Time: '+str(end)+'\n'
plotdata.append(runtime)

print 'Algorithm 2\n'
for n in size:
	data = hf.generate_data(n)
	start = time.time()
	result = fv.FindVisible_2(data[0],data[1])
	end = time.time()-start
	runtime.append(end)
	print 'Time: '+str(end)+'\n'
plotdata.append(runtime)

print 'Algorithm 3\n'
for n in size:
	data = hf.generate_data(n)
	start = time.time()
	result = fv.FindVisible_3(data[0],data[1])
	end = time.time()-start
	runtime.append(end)
	print 'Time: '+str(end)+'\n'
plotdata.append(runtime)

plot_data.write(json.dumps(plotdata))
plot_data.close()
