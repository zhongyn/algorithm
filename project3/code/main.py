import maxSum as ms
import helper as hp

matrix,m,n = hp.read_data('../data/test2.txt')
# b = hp.read_data('../data/test2.txt')
print 'finish reading data'

T = ms.maxSum(matrix,m,n)
print 'finish compute T'

a,b,score = ms.findMaxScore(T,m,n)
print 'finish find max score'
print 'a,b,score: ',a,b,score

stack = ms.backTrack(T,matrix,a,b)
print 'finish backTrack'

output = hp.write_data(stack,score,'../data/output.txt')



