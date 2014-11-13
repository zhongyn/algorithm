import maxSum as ms
import helper as hp


for i in range(1,4):

	print 'test '+str(i)+':'
	
	matrix,m,n = hp.read_data('../data/test'+str(i)+'.txt')
	print 'finish reading test data'

	T = ms.maxSum(matrix,m,n)
	print 'finish computing T'

	a,b,score = ms.findMaxScore(T,m,n)
	print 'finish finding max score'

	stack = ms.backTrack(T,matrix,a,b)
	print 'finish backTrack'

	output = hp.write_data(stack,score,'../data/output'+str(i)+'.txt')
	print 'finish writing output'



