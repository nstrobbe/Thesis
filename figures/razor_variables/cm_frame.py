import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Circle, Arrow

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 100)    
    plt.axis('off')

    # Draw CM
    blob = Circle(xy=(50,50),radius=14,angle=0,lw=0,edgecolor='MediumVioletRed',fc='MediumVioletRed',zorder=5)
    ax.add_patch(blob)
    fig.text(0.5, 0.45,r'$\sqrt{\hat{s}}$',ha='center',fontsize=50,color='black')

    # draw sparticles
    t1 = np.arange(3,37)
    t2 = np.arange(64,97)
    out_p1 = np.array([50]*len(t1)) 
    out_p2 = np.array([50]*len(t2))

    ax.annotate('', xytext=(20,50), xy=(15,50),
                arrowprops=dict(arrowstyle="-|>,head_width=0.8,head_length=3",color='RoyalBlue'))
    plt.plot(t1,out_p1,color='RoyalBlue',linestyle='-',lw=3)
    fig.text(0.1,0.47,r'$S_2$',ha='center',fontsize=40,color='k')
    fig.text(0.25, 0.55,r'$-\vec{\beta}^{CM}$',ha='center',fontsize=40,color='k')

    ax.annotate('', xy=(85,50), xytext=(80,50), alpha=0.75,
                arrowprops=dict(arrowstyle="-|>,head_width=0.8,head_length=3",color='RoyalBlue'))
    plt.plot(t2,out_p2,color='RoyalBlue',linestyle='-',lw=3)
    fig.text(0.93, 0.47,r'$S_1$',ha='center',fontsize=40,color='k')
    fig.text(0.82, 0.55,r'$\vec{\beta}^{CM}$',ha='center',fontsize=40,color='k')

    plt.savefig("cm_frame.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

