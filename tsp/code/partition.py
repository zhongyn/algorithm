import kmeans as km
import numpy as np
import near_neighbor as nn

data = np.loadtxt('../data/example-input-3.txt', delimiter=' ', dtype=int)
points = np.empty((len(data),4), dtype=int)
points[:,:3] = data
k = 10

points[:,3] = km.kmeans(data[:,1:], k, partition=True)
print 'finish partition'

np.savetxt('../data/partition.txt',points)

distanceM = nn.distanceMatrix(data[:,1:])
np.savetxt('../data/distance-matrix.txt', distanceM, fmt='%1d')
