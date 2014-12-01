import numpy as np
import par_nn as pn
import opt2 as op
import near_neighbor as nn
import multiprocessing as mp
import sharedmem as shm

def tsp(data, k, runs, opt):
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
	for r in result:
		opt_dist = nn.tour_distance(r.get(),data)
		print 'dist_ratio:', opt_dist/(opt*1.0)
		
	# opt_tour = op.opt2(distMat,init_tour)
	# opt_dist = nn.tour_distance(opt_tour,data)

	print 'tour_length:', n
	pool.close()
	pool.join()

	# return opt_tour



if __name__ == '__main__':
	# load input data
	# data = np.loadtxt('../data/example-input-1.txt', dtype=int)
	# data = np.loadtxt('../data/example-input-2.txt', dtype=int)
	# data = np.loadtxt('../data/example-input-3.txt', dtype=int)
	data = np.loadtxt('../data/brd14051.tsp',dtype=int)
	# data = np.loadtxt('../data/att48.tsp',dtype=int)
	# data = np.loadtxt('../data/att532.tsp',dtype=int)
	# data = np.loadtxt('../data/pla7397.tsp',dtype=int)
	# data = np.loadtxt('../data/fnl4461.tsp',dtype=int)

	
	# shDistMat = shm.empty((n,n),dtype=int)
	# shDistMat = nn.distanceMatrix(data)
	k = 1
	runs = 1
	opt = [108159, 2579, 1573084, 469385, 10628, 27686, 23260728, 182566]

	# print 'example 1,',k,'clusters'
	# for r in result:
	# 	print r.get()

	# for i in range(runs):
	# 	print 'run',i,':'
	# 	tsp(data,shDistMat,k,opt)

	tsp(data, k, runs, opt[3])

