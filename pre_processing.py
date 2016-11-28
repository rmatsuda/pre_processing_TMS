import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import matplotlib.colors as colors

_SUBJECT = ["01", "02", "03", "04", "05", "08", "09", "10", "11", "12", "13"]
_INTENSITY = ["110", "120"]
_TYPE = ["MNI", "MRI"]
_MUSCLES = ["ADM", "FCP", "FRC"]
_BANDWIDTH = 7
for i in _SUBJECT:
    for j in _INTENSITY:
        for o in _TYPE:
            for l in _MUSCLES:
                # try:
                    print 'data/'+i+"_"+j+"_"+o+"_"+l+".txt"
                    _PATH = 'data/'+i+"_"+j+"_"+o+"_"+l+".txt"
                    #print _PATH
                    f = np.loadtxt(_PATH, delimiter='\t', usecols=[0, 1, 2, 3])
                    ID = np.loadtxt(_PATH, delimiter='\t', usecols=[7], dtype=str)
                    if ID[0] != "":
                        a = f[3:, :]
                    else:
                        a = f[:, :]

                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    #ax.scatter(a[:,0],a[:,1],a[:,2])
                    a[:,3] = 0
                    #create color scale
                    color_norm = colors.Normalize(vmin=0, vmax=len(a) - 1)
                    scalar_map = cm.ScalarMappable(norm=color_norm, cmap='hsv')
                    print len(a)
                    for t in range(0,len(a)):
                        #calculate the Euclidian distance(ED) between all markers
                        #if distance is under a upper, create an ID
                        for u in range(0, len(a)):
                            ED = np.sqrt((a[t,0]-a[u,0])**2+(a[t,1]-a[u,1])**2+(a[t,2]-a[u,2])**2)
                            if ED <= _BANDWIDTH and a[u,3] == 0 :
                                a[u,3] = t
                        #set different colors
                        col = scalar_map.to_rgba(a[t, 3])
                        if (a[t,3] % 3) != 0 and  a[t,3]!= 1:
                            ax.scatter(a[t,0],a[t,1],a[t,2],c=col, marker='x')
                        else:
                            ax.scatter(a[t,0], a[t,1], a[t,2], c=col)

                    ax.legend((a[:,3]), fontsize = 'xx-small')
                    plt.show()
                # except:
                #     print "There is no data for the subject "