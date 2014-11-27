import kmeans as km
import numpy as np

data = np.loadtxt('../data/example-input-3.txt', delimiter=' ')
points = np.empty((len(data),4))
points[:,:3] = data
k = 10

km.kmeans(data,k,partition=True)
print 'finish partition'

