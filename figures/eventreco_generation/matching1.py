import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Ellipse, Polygon

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_axes((0.12, 0.12, 0.8, 0.8))
    ax.set_ylim([18, 82])
    ax.set_xlim([0, 60])
    plt.axis('off')

    # draw parton 1
    t = np.arange(10,26)
    in_W = np.array([50]*16)
    plt.plot(t,in_W,color='black',linestyle='-')
    pol3 = Polygon(xy=np.array([ [10,40], [10,60], [25,50] ]),closed=True,lw=3,fc=(65./225,105./225,1,0.2),edgecolor=(65./225,105./225,1,0.7))
    ax.add_patch(pol3)
    el3 = Ellipse(xy=(10,50),width=5,height=20,angle=0,lw=3,fc='royalblue',edgecolor='royalblue')
    ax.add_patch(el3)
    
    # draw parton 2
    tq1 = np.arange(25,41)
    out_q1 = np.array([50+(x-25) for x in tq1])
    plt.plot(tq1,out_q1,color='black',linestyle='-')
    pol1 = Polygon(xy=np.array([ [37.5,74], [44.5,55.5], [25,50] ]),closed=True,lw=3,fc=(65./225,105./225,1,0.2),edgecolor=(65./225,105./225,1,0.7))
    ax.add_patch(pol1)
    el1 = Ellipse(xy=(41,65),width=5,height=20,angle=20,lw=3,fc='royalblue',edgecolor='royalblue')
    ax.add_patch(el1)

    # draw parton 3
    tq2 = np.arange(25,41)
    out_q2 = np.array([50-(x-25) for x in tq2])
    plt.plot(tq2,out_q2,color='black',linestyle='-')
    pol2 = Polygon(xy=np.array([ [37.5,26], [44.5,44.5], [25,50] ]),closed=True,lw=3,fc=(65./225,105./225,1,0.2),edgecolor=(65./225,105./225,1,0.7))
    ax.add_patch(pol2)
    el2 = Ellipse(xy=(41,35),width=5,height=20,angle=-20,lw=3,fc='royalblue',edgecolor='royalblue')
    ax.add_patch(el2)

    fig.text(0.4, 0.25,"matched",ha='center',fontsize=25,color='black')


    plt.savefig("matching1.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

