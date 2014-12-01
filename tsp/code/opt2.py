import numpy as np
import near_neighbor as nn

def opt2(distMat, tour):
	# init a flag
	isOptimized = True
	n = len(tour)

	k = 1
	while isOptimized:
		print 'round',k,':'
		isOptimized = False
		maxChange = 0
		maxi = None
		maxj = None
		# local optimize search
		for i in range(n-3):
			for j in range(i+2,n-1):
				old = distMat[tour[i],tour[i+1]]+distMat[tour[j],tour[j+1]]
				new = distMat[tour[i],tour[j]]+distMat[tour[i+1],tour[j+1]]
				change = old - new
				if change > maxChange:
					maxChange = change
					maxi, maxj = i, j
					isOptimized = True
		if isOptimized:
			# tour = swap_tour(tour,maxi,maxj)
			tour[i+1:j+1] = tour[j:i:-1]
		k += 1
	return tour

# swap 2 edges
def swap_tour(tour,i,j):
	newtour = np.empty(len(tour),dtype=int)
	newtour[:i+1] = tour[:i+1]
	newtour[i+1:j+1] = tour[j:i:-1]
	newtour[j+1:] = tour[j+1:]
	return newtour

