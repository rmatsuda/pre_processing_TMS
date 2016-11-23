import numpy as np
from sklearn.cluster import MeanShift

from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
_SUBJECT = "09"
_MUSCLES = ["ADM", "FCP", "FRC"]
_INTENSITY = ["110", "120"]
_BANDWIDTH = 5.5
for i in _MUSCLES:
    for j in _INTENSITY:
        _PATH = 'data/'+_SUBJECT+"_"+i+"_"+j+".txt"
        print _PATH
        f = np.loadtxt(_PATH)
        X = f[:,0:3]

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