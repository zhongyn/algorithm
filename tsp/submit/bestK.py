import kmeans as km
import numpy as np


# data = np.loadtxt('../data/example-input-1.txt')
# data = np.loadtxt('../data/example-input-2.txt')
# data = np.loadtxt('../data/example-input-3.txt')
# data = np.loadtxt('../data/input-test1.txt',dtype=int)
# data = np.loadtxt('../data/input-test2.txt',dtype=int)
data = np.loadtxt('../data/input-test3.txt',dtype=int)

points = data[:,1:]

km.findK_parallel(points)
print 'finish findK_parallel'

km.findKplot(points)
print 'finish findKplot'