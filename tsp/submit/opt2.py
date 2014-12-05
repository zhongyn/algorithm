import numpy as np
import near_neighbor as nn

def opt2(distMat, tour):
	# init a flag
	isOptimized = True
	n = len(tour)

	bound = 100
	k = 1
	while isOptimized and k<=bound:
	# while isOptimized:
		print 'round',k,':'
		isOptimized = False
		maxChange = 0
		maxi = None
		maxj = None
		# local optimum search
		for i in range(n-3):
			for j in range(i+2,n-1):
				old = distMat[tour[i],tour[i+1]]+distMat[tour[j],tour[j+1]]
				new = distMat[tour[i],tour[j]]+distMat[tour[i+1],tour[j+1]]
				change = old - new
				if change > maxChange:
					maxChange = change
					maxi, maxj = i, j
					isOptimized = True
		# print maxi, maxj
		if isOptimized:
			tour[maxi+1:maxj+1] = tour[maxj:maxi:-1]
		k += 1
	return tour

