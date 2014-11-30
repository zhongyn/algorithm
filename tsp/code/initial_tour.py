import near_neighbor as nn
import multiprocessing as mp
import numpy as np

# load partition data for all points and distance matrix for all clusters
points = np.loadtxt('../data/partition-1.txt', delimiter=' ', dtype=int)
distance_matrix = np.load('../data/distance-matrix-1.npy')

# partition label
label = points[:,3]

# create mutiprocesses and compute near neighbor tour for each cluster
PROCESS = 4
pool = mp.Pool(PROCESS)
result = pool.map(nn.nearNeighbor, distance_matrix)

# translate visiting sequence into a tour for each cluster
for i, r in enumerate(result):
	r[:] = points[:,0][label==i][r]

# extract the begining and end points for each cluster
segment_set = []
for r in result:
	begin = r[0]
	end = r[-1]
	p1 = points[begin,:]
	p2 = points[end,:]
	segment_set.append(nn.segment(p1, p2))

# return the order of all cluster
con_seg = nn.connecting(segment_set)
print con_seg

# connect all cluster into a tour
tour = nn.linkCluster(result, con_seg, len(points))
distance = nn.tour_distance(tour, points)
print 'initial tour:'
print tour
print 'lenth of initial tour:'
print len(tour)
print 'distance of initial tour:'
print distance

distance = np.array([distance])
solution = np.concatenate([distance,tour])
np.savetxt('../data/solution-1.txt',solution,fmt='%1d')

