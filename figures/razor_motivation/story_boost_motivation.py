import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Ellipse

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_axes((0.12, 0.12, 0.8, 0.8))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.tick_params(labelsize=15)
    ax.set_ylim([0, 400])

    # draw diagonal
    t = np.arange(800)
    diagonal = t
    plt.plot(t,diagonal,color='gray',linestyle='--')
    fig.text(0.43, 0.9,
             'mSTOP - mLSP = 0',
             ha='center',fontsize=15,color='gray',rotation=55)

    # draw diagonal
    t2 = np.arange(800)
    l2 = t-175
    plt.plot(t2,l2,color='gray',linestyle='--')
    fig.text(0.51, 0.9,
             'mSTOP - mLSP = mW',
             ha='center',fontsize=15,color='gray',rotation=55)

    # draw diagonal
    t3 = np.arange(800)
    l3 = t-80
    plt.plot(t3,l3,color='gray',linestyle='--')
    fig.text(0.6, 0.9,
             'mSTOP - mLSP = mTOP',
             ha='center',fontsize=15,color='gray',rotation=55)

    # draw limits
    verts = [(200, 0),
             (500, 350),
             (600, 250),
             (650, 0),
             (200, 0)]
    codes = [mpath.Path.MOVETO,
             mpath.Path.CURVE4,
             mpath.Path.CURVE4,
             mpath.Path.CURVE4,
             mpath.Path.CLOSEPOLY]
    path = mpath.Path(verts,codes)
    patch = mpatches.PathPatch(path, facecolor='OrangeRed', alpha=0.2)
    ax.add_patch(patch)    

    # draw limits
    verts = [(100, 0),
             (350, 250),
             (400, 250),
             (150, 0),
             (100, 0)]
    codes = [mpath.Path.MOVETO,
             mpath.Path.CURVE4,
             mpath.Path.CURVE4,
             mpath.Path.CURVE4,
             mpath.Path.CLOSEPOLY]
    path = mpath.Path(verts,codes)
    patch = mpatches.PathPatch(path, facecolor='OrangeRed', alpha=0.2)
    ax.add_patch(patch)    

    # draw ellipses around interesting regions
    el1 = Ellipse(xy=(145,100),width=250,height=48,angle=45,lw=3,fc='None',edgecolor='b')
    ax.add_patch(el1)

    el2 = Ellipse(xy=(650,100),width=160,height=190,angle=0,lw=3,fc='None',edgecolor='g')
    ax.add_patch(el2)

    el3 = Ellipse(xy=(275,100),width=255,height=30,angle=45,lw=3,fc='None',edgecolor='DarkMagenta')
    ax.add_patch(el3)

    plt.xlabel('stop mass (GeV)',fontsize=20)
    plt.ylabel('LSP mass (GeV)',fontsize=20)

    plt.annotate(
        'COMPRESSED\nSPECTRUM',
        xy=(140,100), arrowprops=dict(arrowstyle='->'), xytext=(40, 300),fontsize=20)

    plt.annotate(
        'HIGH MASS',
        xy=(650,150), arrowprops=dict(arrowstyle='->'), xytext=(650,250),fontsize=20)

    plt.annotate(
        'STEALTHY',
        xy=(300,125), arrowprops=dict(arrowstyle='->'), xytext=(550,320),fontsize=20)

    fig.text(
        0.55, 0.25,
        'EXCLUDED',
        ha='center',fontsize=20)

    plt.savefig("story_boost_motivation.pdf")

# Somehow needed, otherwise it crashes..
# Haven't figured out why yet
plt.show()    

