import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Circle, Arrow

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax = fig.add_axes((0.,0.,1.,1.))
    #ax = plt.axes()
    #ax.set_aspect(1)
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 100)    
    plt.axis('off')

    # Draw S1
    blob = Circle(xy=(50,50),radius=14,angle=0,lw=0,edgecolor='b',fc='RoyalBlue',zorder=5)
    ax.add_patch(blob)
    fig.text(0.52, 0.48,r'$S_1$',ha='center',fontsize=50,color='black')

    # draw decay products
    t1 = np.arange(5,37)
    t2 = np.arange(64,95)
    out_p1 = np.array([44+0.5*(x-t1[-1]) for x in t1[::-1]])
    out_p2 = np.array([56+0.5*(x-t2[0]) for x in t2])

    ax.annotate('', xytext=(t1[-1]-10,out_p1[0]-5), xy=(t1[-1]-20,out_p1[0]-10),
                arrowprops=dict(arrowstyle="-|>,head_width=0.8,head_length=3",color='g'))
    plt.plot(t1,out_p1[::-1],color='g',linestyle='-',lw=3)
    fig.text(0.12,0.3,r'$\chi_1$',ha='center',fontsize=40,color='k')
    fig.text(0.23, 0.45,r'$-\vec{p}_1^S$',ha='center',fontsize=40,color='k')

    ax.annotate('', xy=(t2[-1]-10,out_p2[-1]-5), xytext=(t2[0]+10,out_p2[0]+5),
                arrowprops=dict(arrowstyle="-|>,head_width=0.8,head_length=3",color='g'))
    plt.plot(t2,out_p2,color='g',linestyle='-',lw=3)
    fig.text(0.92, 0.67,r'$Q_1$',ha='center',fontsize=40,color='k')
    fig.text(0.78, 0.7,r'$\vec{p}_1^S$',ha='center',fontsize=40,color='k')

    plt.savefig("rest_frame.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

