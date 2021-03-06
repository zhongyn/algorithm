def maxSum(A,m,n):
	T = [[0 for i in range(n)] for i in range(m)]
	T[0][0] = A[0][0]
	for i in range(m):
		for j in range(n):
			tmp = A[i][j]
			if i > 0:
				tmp = max(tmp,T[i-1][j]+A[i][j])
			if j > 0: 
				tmp = max(tmp,T[i][j-1]+A[i][j])
			T[i][j] = tmp
	return T

def findMaxScore(T,m,n):
	a, b = 0, n-1
	for i in range(m):
		if T[a][b] < T[i][n-1]: 
			a, b = i, n-1
	for j in range(n):
		if T[a][b] < T[m-1][j]:
			a, b = m-1, j
	return (a, b, T[a][b])

def backTrack(T,A,a,b):
	stack = []
	while a >= 0 and b>=0:
		stack.append((a,b))
		if T[a][b] == A[a][b]: 
			break
		if a==0 and b==0: 
			break
		if a > 0:
			if T[a][b] == T[a-1][b] + A[a][b]:
				a = a-1
				continue
		if b > 0:
			if T[a][b] == T[a][b-1] + A[a][b]:
				b = b-1
				continue
	return stack



