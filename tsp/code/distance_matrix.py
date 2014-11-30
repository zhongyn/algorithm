import numpy as np
import multiprocessing as mp


def distanceMatrix(data):
	n = len(data)
	result = np.empty((n,n),dtype=int)
	for i, item in enumerate(data):
		result[i] = np.rint(np.sqrt(np.sum((item-data)**2,axis=1)))
	return result


data = np.loadtxt('../data/partition-3.txt', delimiter=' ', dtype=int)
k = len(np.unique(data[:,3]))
PROCESS = 4
pool = mp.Pool(PROCESS)

result = [pool.apply(distanceMatrix, (data[data[:,3]==i],)) for i in range(k)]
print result
np.save('../data/distance_matrix.npy', np.array(result))
