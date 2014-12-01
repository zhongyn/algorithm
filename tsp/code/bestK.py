import kmeans as km
import numpy as np


# data = np.loadtxt('../data/example-input-2.txt')
# data = np.loadtxt('../data/brd14051.tsp')
# data = np.loadtxt('../data/att48.tsp')
# data = np.loadtxt('../data/pla7397.tsp')
data = np.loadtxt('../data/fnl4461.tsp')
points = data[:,1:]

km.findK_parallel(points)
print 'finish findK_parallel'

km.findKplot(points)
print 'finish findKplot'