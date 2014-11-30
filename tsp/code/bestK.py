import kmeans as km
import numpy as np


data = np.loadtxt('../data/example-input-2.txt')
points = data[:,1:]

km.findK_parallel(points)
print 'finish findK_parallel'

km.findKplot(points)
print 'finish findKplot'