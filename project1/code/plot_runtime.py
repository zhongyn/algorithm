import matplotlib.pyplot as pl
import json

with open('../data/plotdata.txt') as f:
	data = json.load(f)

datasize = data[0]
runtime = data[1]

fig,ax1 = pl.subplots()
fonts = 20
ax1.set_title('Experimental Running Time',size=fonts)
ax1.plot(datasize[:10],runtime[0],color='b',marker='o',label='algorithm 1',linewidth=2)
ax1.plot(datasize,runtime[1],color='r',marker='o',label='algorithm 2',linewidth=2)
ax1.plot(datasize,runtime[2],color='y',marker='o',label='algorithm 3',linewidth=2)
ax1.legend(fancybox=True,loc='best',fontsize=18)
ax1.set_xlabel('number of lines',size=fonts)
ax1.set_xscale('log')
ax1.set_ylabel('running time',size=fonts)


pl.show()