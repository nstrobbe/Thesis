import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Ellipse

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_axes((0.12, 0.12, 0.8, 0.8))
    ax.set_ylim([10, 90])
    ax.set_xlim([0, 80])
    plt.axis('off')

    # draw incoming protons
    t = np.arange(0,22)
    ta = np.arange(0,22)
    tb = np.arange(0,22)
    in_p1 = np.array([25+x for x in t])
    in_p1a = np.array([23.5+x for x in ta])
    in_p1b = np.array([26.5+x for x in ta])
    in_p2 = np.array([75-x for x in t])
    in_p2a = np.array([73.5-x for x in ta])
    in_p2b = np.array([76.5-x for x in tb])
    plt.plot(t,in_p1,color='black',linestyle='-',lw=3)
    plt.plot(ta,in_p1a,color='black',linestyle='-',lw=3)
    plt.plot(ta,in_p1b,color='black',linestyle='-',lw=3)
    plt.plot(t,in_p2,color='black',linestyle='-',lw=3)
    plt.plot(ta,in_p2a,color='black',linestyle='-',lw=3)
    plt.plot(tb,in_p2b,color='black',linestyle='-',lw=3)
    fig.text(0.09, 0.77,r'$p$',ha='center',fontsize=40,color='black')
    fig.text(0.09, 0.25,r'$p$',ha='center',fontsize=40,color='black')

    # Draw blob
    blob = Ellipse(xy=(25,50),width=14,height=17,angle=0,lw=1,edgecolor='MediumVioletRed',fc='MediumVioletRed',alpha=1,zorder=5)
    ax.add_patch(blob)

    # draw sparticles
    t1 = np.arange(32,56)
    out_p1 = np.array([54+0.5*(x-t1[0]) for x in t1])
    out_p2 = np.array([46-0.5*(x-t1[0]) for x in t1])
    plt.plot(t1,out_p1,color='RoyalBlue',linestyle='-',lw=3)
    plt.plot(t1,out_p2,color='RoyalBlue',linestyle='-',lw=3)
    fig.text(0.55, 0.67,r'$S_1$',ha='center',fontsize=40,color='black')
    fig.text(0.55, 0.34,r'$S_2$',ha='center',fontsize=40,color='black')

    # draw q1 chi1
    t2 = np.arange(55,75)
    t2_short = np.arange(55,70)
    out_q1 = np.array([out_p1[-1]+1.25*(x-t2[0]) for x in t2_short])
    out_chi1 = np.array([out_p1[-1]-0.5*(x-t2[0]) for x in t2])
    plt.plot(t2_short,out_q1,color='g',linestyle='-',lw=3)
    plt.plot(t2,out_chi1,color='g',linestyle='-',lw=3)
    fig.text(0.87, 0.85,r'$Q_1$',ha='center',fontsize=40,color='black')
    fig.text(0.91, 0.57,r'$\chi_1$',ha='center',fontsize=40,color='black')

    # draw q2 chi2
    out_q2 = np.array([out_p2[-1]+0.5*(x-t2[0]) for x in t2])
    out_chi2 = np.array([out_p2[-1]-1.25*(x-t2[0]) for x in t2_short])
    plt.plot(t2,out_q2,color='g',linestyle='-',lw=3)
    plt.plot(t2_short,out_chi2,color='g',linestyle='-',lw=3)
    fig.text(0.87, 0.15,r'$Q_2$',ha='center',fontsize=40,color='black')
    fig.text(0.91, 0.45,r'$\chi_2$',ha='center',fontsize=40,color='black')


    plt.savefig("signature.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

