import numpy as np
from sklearn.cluster import DBSCAN

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
        db = DBSCAN(eps=_BANDWIDTH, min_samples=2).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

        print('Estimated number of clusters: %d' % n_clusters_)

        x=X[:,0]
        y=X[:,1]
        z=X[:,2]
        w = (np.array([x,y,z,labels])).T
        np.savetxt(_PATH[0:len(_PATH)-4]+'_flag_DB.txt', w, fmt = '%.3f', delimiter='\t')

        # Black removed and is used for noise instead.
        unique_labels = set(labels)
        colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = 'k'

            class_member_mask = (labels == k)

            xy = X[class_member_mask & core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=14)

            xy = X[class_member_mask & ~core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=6)

        plt.title('Estimated number of clusters: %d' % n_clusters_)
        plt.show()