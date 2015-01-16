import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Ellipse

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_axes((0.12, 0.12, 0.8, 0.8))
    ax.set_ylim([18, 82])
    ax.set_xlim([10, 60])
    plt.axis('off')

    # draw incoming W
    t = np.arange(10,26)
    in_W = np.array([50]*16)
    plt.plot(t,in_W,color='black',linestyle='-')
    fig.text(0.3, 0.55,'W',ha='center',fontsize=30,color='black')

    # draw q
    tq1 = np.arange(25,41)
    out_q1 = np.array([50+(x-25) for x in tq1])
    plt.plot(tq1,out_q1,color='black',linestyle='-')
    fig.text(0.48, 0.64,'q',ha='center',fontsize=25,color='black')

    # draw hadronization stuff
    thad = np.arange(40,50)
    had1 = np.array([65-(x-40)*0.3 for x in thad])
    plt.plot(thad,had1,color='black',linestyle='-')
    had2 = np.array([65-(x-40)*0.6 for x in thad])
    plt.plot(thad,had2,color='black',linestyle='-')
    had1p = np.array([65+(x-40)*0.3 for x in thad])
    plt.plot(thad,had1p,color='black',linestyle='-')
    had2p = np.array([65+(x-40)*0.6 for x in thad])
    plt.plot(thad,had2p,color='black',linestyle='-')
    had3 = np.array([65 for x in thad])
    plt.plot(thad,had3,color='black',linestyle='-')

    # draw q`
    tq2 = np.arange(25,41)
    out_q2 = np.array([50-(x-25) for x in tq2])
    plt.plot(tq2,out_q2,color='black',linestyle='-')
    fig.text(0.48, 0.36,"q'",ha='center',fontsize=25,color='black')

    # draw hadronization stuff
    thad = np.arange(40,50)
    had1 = np.array([35-(x-40)*0.3 for x in thad])
    plt.plot(thad,had1,color='black',linestyle='-')
    had2 = np.array([35-(x-40)*0.6 for x in thad])
    plt.plot(thad,had2,color='black',linestyle='-')
    had1p = np.array([35+(x-40)*0.3 for x in thad])
    plt.plot(thad,had1p,color='black',linestyle='-')
    had2p = np.array([35+(x-40)*0.6 for x in thad])
    plt.plot(thad,had2p,color='black',linestyle='-')
    had3 = np.array([35 for x in thad])
    plt.plot(thad,had3,color='black',linestyle='-')

    # draw ellipses 
    el1 = Ellipse(xy=(49,65),width=5,height=20,angle=0,lw=3,fc='b',alpha=0.3,edgecolor='b')
    ax.add_patch(el1)

    el2 = Ellipse(xy=(49,35),width=5,height=20,angle=0,lw=3,fc='b',alpha=0.3,edgecolor='b')
    ax.add_patch(el2)

    el3 = Ellipse(xy=(49,50),width=8,height=60,angle=0,lw=3,fc='none',edgecolor='r')
    ax.add_patch(el3)

    plt.savefig("W_subjets.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

