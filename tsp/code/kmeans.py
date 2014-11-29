import numpy as np
import random
import matplotlib.pyplot as pl
import multiprocessing as mp
import time


def kmeans(data, numCluster, partition=None):
	numData = len(data)
	index = random.sample(xrange(numData), numCluster)
	centers = data[index]

	label = np.empty(numData)
	newCenters = np.empty([numCluster,2])

	np.seterr(divide='ignore', invalid='ignore')
	while True:
		for i, item in enumerate(data):
			dists = np.sqrt(np.sum((item-centers)**2,axis=1))
			label[i] = np.argmin(dists)

		for i in range(numCluster):
			cluster = data[label==i]
			newCenters[i] = np.sum(cluster,axis=0)/(1.0*len(cluster))

		if np.array_equal(centers,newCenters):
			sumSqDist = 0.0;
			for i in range(numCluster):
				cluster = data[label==i]
				tmp = np.sum(np.sum((centers[i]-cluster)**2,axis=1))
				sumSqDist += tmp
			break
		else:
			centers = newCenters.copy()
	
	if partition:
		return label
	return [centers, sumSqDist]


def findK(data):
	k = np.arange(2,16)
	minDist = np.empty(len(k))
	minCenter = []
	runs = 10

	t = time.time()	
	for i, item in enumerate(k):
		sumSqDist = np.empty(runs)
		centers = np.empty([runs,item,2])
		for j in range(runs):
			result = kmeans(data,item)
			sumSqDist[j] = result[1]
			centers[j] = result[0]
		minCenter.append(centers[np.argmin(sumSqDist)])
		minDist[i] = np.amin(sumSqDist)
	print 'time1: ',time.time()-t

	np.savez("../data/findK.npz", k=k, minDist=minDist, minCenter=minCenter)


def findK_parallel(data):
	k = np.arange(2,16)
	minDist = np.empty(len(k))
	minCenter = []
	runs = 10
	processes = 4
	pool = mp.Pool(processes)

	t = time.time()
	for i, item in enumerate(k):
		centers = []
		sumSqDist = []
		result = [pool.apply_async(kmeans,(data,item)) for j in range(runs)]
		for r in result:
			centers.append(r.get()[0])
			sumSqDist.append(r.get()[1])
		sumSqDist = np.array(sumSqDist)
		centers = np.array(centers)
		minCenter.append(centers[np.argmin(sumSqDist)])
		minDist[i] = np.amin(sumSqDist)
	print 'time2: ',time.time()-t

	np.savez("../data/findK.npz", k=k, minDist=minDist, minCenter=minCenter)


def findKplot(data):
	with np.load("../data/findK.npz") as result:
		k = result["k"]
		minDist = result["minDist"]
		minCenter = result['minCenter']


	fig,ax1 = pl.subplots()
	fonts = 18
	ax1.plot(k,minDist,color='b',marker='o')
	ax1.set_xlabel('k',size=16)
	ax1.set_ylabel('Minimum Sum of Squared Distance',size=16)

	knees = np.array([[2,5],[10,12]])
	kindex = knees-2

	f,axarr = pl.subplots(2,2)
	for i in range(2):
		for j in range(2):
			axarr[i,j].set_title('k = '+str(knees[i,j]))
			axarr[i,j].scatter(data[:,0],data[:,1],color='b',alpha=0.5,label='data')
			axarr[i,j].scatter(minCenter[kindex[i,j]][:,0],minCenter[kindex[i,j]][:,1],color='r',marker='s',s=20,label='centers')
			# axarr[i,j].legend(scatterpoints=1,fancybox=True,fontsize=10)

	pl.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
	pl.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

	pl.show()










