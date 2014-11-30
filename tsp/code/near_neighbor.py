import numpy as np
import random

def nearNeighbor(distance_matrix):
	dm = distance_matrix
	city_num = len(dm)

	# init visited array
	visited = np.empty(city_num,dtype=int)
	visited[:] = False

	# pick a random starting city
	start_city = random.randint(0,city_num-1)
	result = np.empty(city_num,dtype=int)

	for i in range(city_num):
		# mark start_city as visited and add it to result
		visited[start_city] = True
		result[i] = start_city

		# get the list of unvisited ids
		unvisited_id = np.where(visited==False)[0]

		# find the id of the nearest city of the start_city
		if len(unvisited_id):
			index = np.argmin(dm[start_city][visited==False])
			next_city_id = unvisited_id[index]
			start_city = next_city_id

	return result

def distanceMatrix(data):
	n = len(data)
	result = np.empty((n,n),dtype=int)
	for i, item in enumerate(data):
		result[i] = np.rint(np.sqrt(np.sum((item-data)**2,axis=1)))
	return result

class segment(object):
	"""docstring for segment"""
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end

def distance(a,b):
	return np.rint(np.sqrt(np.sum((a-b)**2)))

def connecting(data):
	unvisted = data[1:]
	start = data[0]
	visited = [start.begin, start.end]

	while unvisted:
		start_point = visited[-1]
		dist_list = np.empty((len(unvisted)*2,3), dtype=int)

		for i, seg in enumerate(unvisted):
			dist0 = distance(start_point[1:3], seg.begin[1:3])
			dist1 = distance(start_point[1:3], seg.end[1:3])
			dist_list[2*i] = [i, 0, dist0] 
			dist_list[2*i+1] = [i, 1, dist1] 

		# find the nearest point
		next = dist_list[np.argmin(dist_list[:,2])]
		# next segment
		seg = unvisted[next[0]]
		# init the visiting sequence in the next segment
		next_seg = [seg.begin, seg.end]
		# reorder the next segment
		if next[1] == 1:
			next_seg.reverse()
		# add the next segment to visited
		visited.extend(next_seg)
		# remove the segment
		unvisted.pop(next[0])

	return visited

def linkCluster(clusters, con_seg, total):
	# init an empty tour
	tour = np.empty(total,dtype=int)
	start = 0
	end = 0

	for i in range(len(con_seg)/2):
		seg = con_seg[2*i]
		clu = clusters[seg[3]]
		end = len(clu)+start

		# check the begining and ending of each cluster
		if seg[0] == clu[0]:
			tour[start:end] = clu
		else:
			tour[start:end] = clu[::-1]
		start = end
	return tour
	
def tour_distance(tour,points):
	dist = 0
	start = points[tour[0]][1:3]
	for i in range(1,len(tour)):
		next = points[tour[i]][1:3]
		dist += distance(start,next)
		start = next
	back = distance(points[tour[-1]][1:3],points[tour[0]][1:3])
	return int(dist+back)


if __name__ == '__main__':
	test = np.array([[0,3,2],[3,0,4],[2,4,0]])
	print nearNeighbor(test)






