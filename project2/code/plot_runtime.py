import matplotlib.pyplot as pl
import json
import numpy as np

with open('../data/plotdata.json') as f:
	runtime = json.load(f)

with open('../data/plotdata4.json') as f:
	runtime4 = json.load(f)

alg1_x = np.array(runtime[0][:9])
alg1_y = np.array(runtime[1])
alg2_x = np.array(runtime[0])
alg2_y = np.array(runtime[2])
alg3_y = np.array(runtime[3])
alg4_y = np.array(runtime4)

alg1_lgx = np.log(alg1_x)
alg1_lgy = np.log(alg1_y)
alg2_lgx = np.log(alg2_x)
alg2_lgy = np.log(alg2_y)
alg3_lgy = np.log(alg3_y)
alg4_lgy = np.log(alg4_y)

coef1 = np.polyfit(alg1_lgx, alg1_lgy, 1)
poly1 = np.poly1d(coef1)
yfit1 = np.exp(poly1(alg1_lgx))


coef2 = np.polyfit(alg2_lgx, alg2_lgy, 1)
poly2 = np.poly1d(coef2)
yfit2 = np.exp(poly2(alg2_lgx))

coef3 = np.polyfit(alg2_lgx, alg3_lgy, 1)
poly3 = np.poly1d(coef3)
yfit3 = np.exp(poly3(alg2_lgx))

coef4 = np.polyfit(alg2_lgx, alg4_lgy, 1)
poly4 = np.poly1d(coef4)
yfit4 = np.exp(poly4(alg2_lgx))

print 'alg1: '
print coef1
print 'alg2: '
print coef2
print 'alg3: '
print coef3
print 'alg4: '
print coef4

fig1,ax1 = pl.subplots()
fonts = 18
ax1.set_title('Experimental Running Time',size=fonts)
ax1.plot(alg1_x,alg1_y,color='r',marker='o',label='algr1',linewidth=2)
ax1.plot(alg2_x,alg2_y,color='g',marker='s',label='algr2',linewidth=2)
ax1.plot(alg2_x,alg3_y,color='b',marker='h',label='algr3',linewidth=2)
ax1.plot(alg2_x,alg4_y,color='m',marker='D',label='algr4',linewidth=2)
ax1.legend(fancybox=True,loc='best',fontsize=18)
ax1.set_xlabel('problem size N',size=fonts)
ax1.set_ylabel('running time T(N)/s',size=fonts)

fig2,ax2 = pl.subplots()
fonts = 18
ax2.set_title('Experimental Running Time',size=fonts)
ax2.plot(alg1_x,alg1_y,color='r',linewidth=0)
ax2.plot(alg2_x,alg2_y,color='g',linewidth=0)
ax2.plot(alg2_x,alg3_y,color='b',linewidth=0)
ax2.plot(alg2_x,alg4_y,color='m',linewidth=0)
ax2.plot(alg1_x,yfit1,color='r',label='algr1',marker='o',linewidth=2)
ax2.plot(alg2_x,yfit2,color='g',label='algr2',marker='s',linewidth=2)
ax2.plot(alg2_x,yfit3,color='b',label='algr3',marker='h',linewidth=2)
ax2.plot(alg2_x,yfit4,color='m',label='algr4',marker='D',linewidth=2)
ax2.legend(fancybox=True,loc='best',fontsize=fonts)
ax2.set_xlabel('problem size logN',size=fonts)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_ylabel('running time logT(N)/s',size=fonts)

pl.show()