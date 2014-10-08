
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
#		for j = len(SubVis), j > 2, j--:
#			(x, y) = Intersection point of line Y[SubVis[j]] and Y[SubVis[j-1]]
#			if y > M[i]*x + B[i]: 
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

def FindVisible_1(M, B):































	