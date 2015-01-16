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

    # draw incoming q/g
    t = np.arange(10,26)
    in_W = np.array([50]*16)
    plt.plot(t,in_W,color='black',linestyle='-')
    fig.text(0.25, 0.55,'q/g',ha='center',fontsize=30,color='black')

    # draw hadronization stuff
    thad = np.arange(25,50)
    had1 = np.array([50-(x-25)*0.3 for x in thad])
    plt.plot(thad,had1,color='black',linestyle='-')
    had2 = np.array([50-(x-25)*0.6 for x in thad])
    plt.plot(thad,had2,color='black',linestyle='-')
    had3 = np.array([50-(x-25)*0.9 for x in thad])
    plt.plot(thad,had3,color='black',linestyle='-')
    had1p = np.array([50+(x-25)*0.3 for x in thad])
    plt.plot(thad,had1p,color='black',linestyle='-')
    had2p = np.array([50+(x-25)*0.6 for x in thad])
    plt.plot(thad,had2p,color='black',linestyle='-')
    had3p = np.array([50+(x-25)*0.9 for x in thad])
    plt.plot(thad,had3p,color='black',linestyle='-')
    had3 = np.array([50 for x in thad])
    plt.plot(thad,had3,color='black',linestyle='-')

    # draw ellipses 
    el3 = Ellipse(xy=(49,50),width=8,height=60,angle=0,lw=3,fc='none',edgecolor='r')
    ax.add_patch(el3)

    plt.savefig("qg_jets.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

