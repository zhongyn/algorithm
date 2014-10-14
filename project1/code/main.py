import read_data as rd
import find_visible as fv
import generate_set as gs
import json
import time

# read data from test files
test_set = rd.read_data('../data/test_set.txt')
exp_test = rd.read_data('../data/solve_these.txt')
exp_result = open('../data/test_result.txt', 'w+')

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
	exp_result.write(json.dumps(result)+'\n')
exp_result.close()

# running time analysis
size = range(100,1000,100)+range(1000,10000,1000)
for n in size:
	data = gs.generate_data(n)
	start = time.time()
	result = fv.FindVisible_3(data[0],data[1])
	end = time.time()-start
	print 'Time: '+str(end)+'\n'
