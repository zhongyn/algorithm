import kmeans as km
import numpy as np
import near_neighbor as nn
import multiprocessing as mp

def parNN(data, k):
	# partition by kmeans
	points = np.empty((len(data),4), dtype=int)
	points[:,:3] = data
	points[:,3] = km.kmeans(data[:,1:], k, partition=True)
	# print 'finish partition'

	# compute distance matrix for each cluster
	PROCESS = 4
	pool = mp.Pool(PROCESS)
	distance_matrix = [pool.apply(nn.distanceMatrix, (points[points[:,3]==i],)) for i in range(k)]
	# print 'finish computing distanceMatrix'

	# compute initia tour
	# partition label
	label = points[:,3]
	# create mutiprocesses and compute near neighbor tour for each cluster
	# PROCESS = 4
	# pool = mp.Pool(PROCESS)
	cluster_tours = pool.map(nn.nearNeighbor, distance_matrix)
	# translate visiting sequence into a tour for each cluster
	for i, r in enumerate(cluster_tours):
		r[:] = points[:,0][label==i][r]

	# extract the begining and end points for each cluster
	segment_set = []
	for r in cluster_tours:
		begin = r[0]
		end = r[-1]
		p1 = points[begin,:]
		p2 = points[end,:]
		segment_set.append(nn.segment(p1, p2))

	# return the order of all cluster
	con_seg = nn.connecting(segment_set)
	# connect all cluster into a tour
	tour = nn.linkCluster(cluster_tours, con_seg, len(points))
	pool.close()
	pool.join()

	return tour
	# distance = nn.tour_distance(tour, points)
	# print 'initial tour:'
	# print tour
	# print 'lenth of initial tour:'
	# print len(init_tour)
	# print 'distance of initial tour:'

	# distance = np.array([distance])
	# solution = np.concatenate([distance,tour])
	# np.savetxt('../data/solution-1.txt',solution,fmt='%1d')




if __name__ == '__main__':
	# load input data
	data1 = np.loadtxt('../data/example-input-1.txt', dtype=int)
	# data2 = np.loadtxt('../data/example-input-2.txt', dtype=int)
	# data3 = np.loadtxt('../data/example-input-3.txt', dtype=int)
	# data4 = np.loadtxt('../data/brd14051.tsp',dtype=int)
	# data5 = np.loadtxt('../data/att48.tsp',dtype=int)
	# data6 = np.loadtxt('../data/pla7397.tsp',dtype=int)
	# data6 = np.loadtxt('../data/fnl4461.tsp',dtype=int)
	runs = 5
	k = 1
	print 'example 1,',k,'clusters'
	for i in range(runs):
		print main(data1, k)/108159.0

	# print 'example 2,',k,'clusters'
	# for i in range(runs):
	# 	print main(data2, k)/2579.0

	# print 'example 3:'
	# for i in range(runs):
	# 	print main(data3, 1)/ 1573084.0

	# print 'example 4:'
	# for i in range(runs):
	# 	print main(data4, k)/ 469385.0

	# print 'example 6:'
	# for i in range(runs):
	# 	print main(data6, k)/182566.0

