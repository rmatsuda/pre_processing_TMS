import numpy as np
from sklearn.cluster import MeanShift

from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
_SUBJECT = ["01", "02", "03", "04", "05", "08", "09", "10", "11", "12", "13"]
_INTENSITY = ["110", "120"]
_TYPE = ["MNI", "MRI"]
_MUSCLES = ["ADM", "FCP", "FRC"]
_BANDWIDTH = 5
for i in _SUBJECT:
    for j in _INTENSITY:
        for o in _TYPE:
            for l in _MUSCLES:
                try:
                    print 'data/'+i+"_"+j+"_"+o+"_"+l+".txt"
                    _PATH = 'data/'+i+"_"+j+"_"+o+"_"+l+".txt"
                    #print _PATH
                    f = np.loadtxt(_PATH, delimiter='\t', usecols=[0, 1, 2])
                    ID = np.loadtxt(_PATH, delimiter='\t', usecols=[7], dtype=str)
                    if ID[0] != "":
                        X = f[3:, :]
                    else:
                        X = f[:, :]

                    af = MeanShift(bandwidth = _BANDWIDTH).fit(X)
                    cluster_centers = af.cluster_centers_

                    labels = af.labels_
                    print labels
                    n_clusters_ = len(cluster_centers )

                    print('Estimated number of clusters: %d' % n_clusters_)

                    x=X[:,0]
                    y=X[:,1]
                    z=X[:,2]
                    w = (np.array([x,y,z,labels])).T
                    np.savetxt(_PATH[0:len(_PATH)-4]+'_flag_MS.txt', w, fmt = '%.3f', delimiter='\t')

                    plt.figure(1)
                    plt.clf()

                    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
                    for k, col in zip(range(n_clusters_), colors):
                        my_members = labels == k
                        cluster_center = cluster_centers[k]
                        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
                        plt.plot(cluster_center[0], cluster_center[1], '+', markerfacecolor=col,
                                 markeredgecolor='k', markersize=14)
                    plt.title('Estimated number of clusters: %d' % n_clusters_)
                    plt.show()
                except:
                    print "There is no data for the subject "