import read_data as rd
import find_visible as fv

test_set = rd.read_data('../data/test_set.txt')
exp_test = rd.read_data('../data/solve_these.txt')

instance = test_set[0]
test_1 = fv.FindVisible_3(instance[0],instance[1])
print test_1
print instance[2]
