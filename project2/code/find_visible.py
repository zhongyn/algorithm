
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
#		V[i] = True, i = 1..n
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

#----------------------- 
# Algorithm 4
#-----------------------

# FindVisible_4(Lines[1..n])
# 	if n == 1:
# 		return Lines[1]
# 	m = n/2
# 	left = FindVisible_4(Lines[1..m])
# 	right = FindVisible_4(Lines[m+1..n])
# 	result = MergeVisible(left, right)
# 	return result
#
# MergeVisible(L[1..a], R[1..b])
# 	LPts = endpoints of the visible line segments in L
# 	RPts = endpoints of the visible line segments in R
#
# 	Li = Ri = 1
# 	targetL = 1
# 	while Li <= len(LPts):
# 		(P1x, P1y) = LPts[Li]
# 		(P2x, P2y) = RPts[Ri]
# 		if P1x <= P2x:
# 			if (P1x, P1y) is above line segment R[Ri]:
# 				Li = Li + 1
# 				Ri = Ri + 1
# 			else:
# 				targetL = Li
# 				break
# 		else:
# 			Ri = Ri + 1
#
# 	Li = Ri = 1
# 	targetR = b
# 	while Ri <=len(RPts):
# 		(P1x, P1y) = LPts[Li]
# 		(P2x, P2y) = RPts[Ri]
# 		if P2x <= P1x:
# 			if (P2x, P2y) is below line segment L[Li]:
# 				Li = Li + 1
# 				Ri = Ri + 1
# 			else:
# 				targetR = Ri
# 				break
# 		else:
# 			Li = Li + 1
# 	return L[1..targetL] + R[targetR..b]
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


#-----------------------------------------------------
#-----------------------------------------------------
class line:
	def __init__(self, index, slope, intersect):
		self.m = slope
		self.b = intersect
		self.id = index		
		
def FindVisible_4(lines):
	n = len(lines)
	if n <= 2:
		return lines
	if n == 3:
		if IsAbove(lines[0],lines[2],lines[1]):
			return [lines[0],lines[2]]
		else:
			return lines
	m = n/2
	left = FindVisible_4(lines[:m])
	right = FindVisible_4(lines[m:])
	print 'len(right): '+str(len(right))
	print 'len(left): '+str(len(left))
	result =  MergeVisible(left, right)
	return result

def MergeVisible(left, right):
	li = ri = 0
	while li<len(left)-1 and ri<len(right)-1:
		if CompareCross(left[li],left[li+1],right[ri],right[ri+1]):
			if IsAboveEqual(left[li],left[li+1],right[ri]):
				li += 1
			else: break
		else:
			ri += 1
	targetL = li
	print 'targetL: '+str(targetL)

	li = ri = 0
	while ri<len(right)-1 and li <len(left)-1:
		if CompareCross(right[ri],right[ri+1],left[li],left[li+1]):
			if not IsAboveEqual(right[ri],right[ri+1],left[li]):
				ri += 1
			else: break
		else:
			li += 1
	targetR = ri

	return left[:targetL+1]+right[targetR:]

def IsAbove(l1,l2,l3):
	# verify that whether the cross point of line1 and line2
	# is above line3.
	return (l1.m-l3.m)*(l2.b-l1.b) - (l3.b-l1.b)*(l1.m-l2.m) < 0

def IsAboveEqual(l1,l2,l3):
	# verify that whether the cross point of line1 and line2
	# is above or on line3.
	return (l1.m-l3.m)*(l2.b-l1.b) - (l3.b-l1.b)*(l1.m-l2.m) <= 0

def CompareCross(l1,l2,l3,l4):
	# compare the x value of two cross points, 
	# P1 between l1 and l2, P2 between l3 and l4.
	return (l3.m-l4.m)*(l2.b-l1.b) - (l1.m-l2.m)*(l4.b-l3.b) <= 0
























	