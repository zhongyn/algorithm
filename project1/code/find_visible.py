
#----------------------- 
# Algorithm 1
#-----------------------

# FindVisible_1(M[1..n], B[1..n])
#	n = len(M)
#	Initialize each line as visible:
#		V[i] = True, i = 1..n
#	if n <= 2: return V
#
#	for i = 2, i < n, i++:
#		for j = 1, j < i, j++:
#			for k = i+1, k <= n, k++:
#				(x, y) = Intersection point of line Yj and Yk
#				if y > M[i]*x + B[i]:
#					V[i] = False
#	return V

#----------------------- 
# Algorithm 2
#-----------------------

# FindVisible_2(M[1..n], B[1..n])
#	n = len(M)
#	Initialize each line as visible:
#		V[i] = True, i = 1..n
#	if n <= 2: return V
#
#	for i = 2, i < n, i++:
#		for j = 1, j < i, j++:
#			for k = i+1, k <= n, k++:
#				if V[i] == False: break
#				(x, y) = Intersection point of line Yj and Yk
#				if y > M[i]*x + B[i]:
#					V[i] = False
#			if V[i] == False: break
#	return V

#----------------------- 
# Algorithm 3
#-----------------------

# FindVisible_3(M[1..n], B[1..n])
#	n = len(M)
#	Initialize each line as visible:
#		V[i] = False, i = 1..n
#	if n <= 2: return V
#
#	SubVis = [1, 2]
#	for i = 3, i <= n, i++:
#		while len(SubVis) > 1
#			(x, y) = Intersection point of line Y[SubVis[-1]] and Y[SubVis[-2]]]
#			if y >= M[i]*x + B[i]: 
#				break
#			else:
#				Remove SubVis[j] from SubVis
#		Add i to SubVis
#
#	for k = 1, k < len(SubVis), k++:
#		V[k] = True
#
#	return V

#---------------------------------------------------
#---------------------------------------------------

def FindVisible_1(m, b):
	# m is sorted slope array
	n = len(m)
	v = [True] * n
	# If there are only two lines, both are visible
	if n <= 2: return v

	# Loop through each triple to find the invisible lines
	for i in range(1,n-1):
		for j in range(0,i):
			for k in range(i+1,n):
				# Compare Yi(x) with Y(x), where (x,Y) is the 
				# intersection point of Yj and Yk
				tem = (m[j]-m[i])*(b[k]-b[j]) - (b[i]-b[j])*(m[j]-m[k])
				if tem < 0: v[i] = False
	return v


def FindVisible_2(m, b):
	# m is sorted slope array
	n = len(m)
	v = [True] * n
	# If there are only two lines, both are visible
	if n <= 2: return v

	# Loop through each triple to find the invisible lines
	# Skip loop if the line is invisible
	for i in range(1,n-1):
		for j in range(0,i):
			for k in range(i+1,n):
				if v[i] == False: break
				# Compare Yi(x) with Y(x), where (x,Y) is the 
				# intersection point of Yj and Yk
				tem = (m[j]-m[i])*(b[k]-b[j]) - (b[i]-b[j])*(m[j]-m[k])
				if tem < 0: v[i] = False
			if v[i] == False: break
	return v


def FindVisible_3(m, b):
	# m is sorted slope array
	n = len(m)
	v = [False] * n
	# If there are only two lines, both are visible
	if n <= 2: return [True,True]

	SubVis = [0,1]
	for i in range(2,n):
		while len(SubVis) > 1:
			# Compare Yi(x) with Y(x), where (x,Y) is the 
			# intersection point of Y[SubVis[j]] and Y[SubVis[j-1]]
			tem = (m[SubVis[-1]]-m[i])*(b[SubVis[-2]]-b[SubVis[-1]]) - (b[i]-b[SubVis[-1]])*(m[SubVis[-1]]-m[SubVis[-2]])
			if tem >= 0: break
			del SubVis[-1]
		SubVis.append(i)
		# add the last line into the visible subset

	for k in SubVis: v[k] = True
	return v



	