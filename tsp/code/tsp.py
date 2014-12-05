import numpy as np
import par_nn as pn
import opt2 as op
import near_neighbor as nn
import multiprocessing as mp
import sharedmem as shm
import tsp_verifier as vf

def tsp(data, k, runs, opt, test_id):
	n = len(data)
	tours = np.empty((runs,n+1),dtype=int)

	print 'init_tour:'
	for i in range(runs):
		init_tour = pn.parNN(data,k)
		init_dist = nn.tour_distance(init_tour,data)
		tours[i] = init_tour
		print 'dist_ratio:', init_dist/(opt*1.0)
	
	distMat = nn.distanceMatrix(data)
	PROCESS = 4
	pool = mp.Pool(PROCESS)
	result = [pool.apply_async(op.opt2,(distMat,init_tour)) for init_tour in tours]

	print 'opt_tour:'

	input_file = '../data/input-test'+str(test_id)+'.txt'

	a = 1
	for r in result:
		opt_dist = nn.tour_distance(r.get(),data)
		print 'dist_ratio:', opt_dist/(opt*1.0)
		output_file = '../data/test1-'+str(a)+'.txt'
		np.savetxt(output_file,np.concatenate([np.array([opt_dist]),r.get()[:-1]]),fmt='%1d')
		vf.main(input_file,output_file)
		a += 1
	# for i, r in enumerate(result):
	# 	opt_dist = nn.tour_distance(r,data)
	# 	print 'dist_ratio:', opt_dist/(opt*1.0)
	# 	output_file = '../data/test1-'+str(i)+'.txt'
	# 	np.savetxt(output_file,np.concatenate([np.array([opt_dist]),r[:-1]]),fmt='%1d')
	# 	vf.main(input_file,output_file)
	# opt_tour = op.opt2(distMat,init_tour)
	# opt_dist = nn.tour_distance(opt_tour,data)

	print 'tour_length:', n
	pool.close()
	pool.join()

	# return opt_tour

def main(k,runs,test_id):
	test_file = '../data/input-test'+str(test_id)+'.txt'
	data = np.loadtxt(test_file)
	opt = [538,107217,469385]
	tsp(data, k, runs, opt[test_id-1], test_id)


if __name__ == '__main__':
	k = 1
	runs = 5
	test_id = 1
	main(k, runs, test_id)
	# load input data
	# data = np.loadtxt('../data/example-input-1.txt', dtype=int)
	# data = np.loadtxt('../data/example-input-2.txt', dtype=int)
	# data = np.loadtxt('../data/example-input-3.txt', dtype=int)
	# data = np.loadtxt('../data/brd14051.tsp',dtype=int)
	# data = np.loadtxt('../data/att48.tsp',dtype=int)
	# data = np.loadtxt('../data/att532.tsp',dtype=int)
	# data = np.loadtxt('../data/pla7397.tsp',dtype=int)
	# data = np.loadtxt('../data/fnl4461.tsp',dtype=int)
	# data = np.loadtxt('../data/bayg29.tsp',dtype=int)
	# data = np.loadtxt('../data/rat575.tsp',dtype=int)
	# data = np.loadtxt('../data/pa561.tsp',dtype=int)
	# data = np.loadtxt('../data/input-test1.txt',dtype=int)
	# data = np.loadtxt('../data/input-test2.txt',dtype=int)
	# data = np.loadtxt('../data/input-test3.txt',dtype=int)

	
	# shDistMat = shm.empty((n,n),dtype=int)
	# shDistMat = nn.distanceMatrix(data)
	# opt = [108159, 2579, 1573084, 469385, 10628, 27686, 23260728, 182566, 1610,6773,2763]
	# opt = [538,107217,469385]

	# print 'example 1,',k,'clusters'
	# for r in result:
	# 	print r.get()

	# for i in range(runs):
	# 	print 'run',i,':'
	# 	tsp(data,shDistMat,k,opt)

	# tsp(data, k, runs, opt[2])

