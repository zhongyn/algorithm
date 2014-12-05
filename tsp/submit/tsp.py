import numpy as np
import par_nn as pn
import opt2 as op
import near_neighbor as nn
import multiprocessing as mp
import tsp_verifier as vf

def tsp(data, k, runs, test_id):
	n = len(data)
	tours = np.empty((runs,n+1),dtype=int)

	print 'init_tour:'
	for i in range(runs):
		init_tour = pn.parNN(data,k)
		init_dist = nn.tour_distance(init_tour,data)
		tours[i] = init_tour
	
	distMat = nn.distanceMatrix(data)
	PROCESS = 4
	pool = mp.Pool(PROCESS)
	result = [pool.apply_async(op.opt2,(distMat,init_tour)) for init_tour in tours]

	print 'opt_tour:'
	input_file = '../data/input-test'+str(test_id)+'.txt'

	a = 1
	for r in result:
		opt_dist = nn.tour_distance(r.get(),data)
		output_file = '../data/test'+str(test_id)+'-'+str(a)+'.txt'
		np.savetxt(output_file,np.concatenate([np.array([opt_dist]),r.get()[:-1]]),fmt='%1d')
		vf.main(input_file,output_file)
		a += 1

	print 'tour_length:', n
	pool.close()
	pool.join()


def main(k,runs,test_id):
	test_file = '../data/input-test'+str(test_id)+'.txt'
	data = np.loadtxt(test_file)
	tsp(data, k, runs, test_id)


if __name__ == '__main__':
	k = 1
	runs = 5
	test_id = 1
	main(k, runs, test_id)
