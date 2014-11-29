import numpy as np
import multiprocessing as mp


def distanceMatrix(data):
	n = len(data)
	result = np.empty((n,n),dtype=int)
	for i, item in enumerate(data):
		result[i] = np.rint(np.sqrt(np.sum((item-data)**2,axis=1)))
	return result


data = np.loadtxt('../data/partition.txt', delimiter=' ', dtype=int)
distance_matrix = []
k = 10

PROCESS = 4
pool = mp.Pool(PROCESS)

result = [pool.apply_async(distanceMatrix, (data[data[:,3]==i],)) for i in range(k)]
for r in result:
	distance_matrix.append(r.get())

print distance_matrix
np.savetxt('../data/distance_matrix.txt', np.array(distance_matrix, dtype=object))
