import read_data as rd
import find_visible as fv

test_set = rd.read_data('../data/test_set.txt')
exp_test = rd.read_data('../data/solve_these.txt')

two_line = [[1,4],[2,-2]]
test = fv.FindVisible_1(two_line[0],two_line[1])
print 'Test:   '+ str(test)
print 'Answer: [True, True]\n'

instance = test_set[3]
test_1 = fv.FindVisible_1(instance[0],instance[1])
test_2 = fv.FindVisible_2(instance[0],instance[1])
test_3 = fv.FindVisible_3(instance[0],instance[1])
print test_1
print test_2
print test_3
print 'Answer:'
print instance[2]

