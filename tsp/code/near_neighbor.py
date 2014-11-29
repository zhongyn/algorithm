import numpy as np
import random

def nearNeighbor(distance_matrix, city_num):
	dm = distance_matrix

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


if __name__ == '__main__':
	test = np.array([[0,3,2],[3,0,4],[2,4,0]])
	print nearNeighbor(test,3)






