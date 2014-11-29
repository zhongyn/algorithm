import kmeans as km
import numpy as np


data = np.loadtxt('../data/example-input-1.txt', delimiter=' ', dtype=int)
points = np.empty((len(data),4), dtype=int)
points[:,:3] = data
k = 10

points[:,3] = km.kmeans(data[:,1:], k, partition=True)
print 'finish partition'
np.savetxt('../data/partition.txt',points, fmt='%1d')
