import numpy as np
from sklearn.cluster import DBSCAN

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
_BANDWIDTH = 10
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

                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    for k, col in zip(unique_labels, colors):
                        if k == -1:
                            # Black used for noise.
                            col = 'k'

                        class_member_mask = (labels == k)

                        xy = X[class_member_mask & core_samples_mask]
                        #ax.scatter(xy[:, 0], xy[:, 1], xy[:, 2], 'o', col)
                        plt.plot(xy[:, 0], xy[:, 1],xy[:, 2], 'o', markerfacecolor=col,
                                 markeredgecolor='k', markersize=8)

                        xy = X[class_member_mask & ~core_samples_mask]
                        #ax.scatter(xy[:, 0], xy[:, 1], xy[:, 2], 'o', col)
                        plt.plot(xy[:, 0], xy[:, 1],xy[:, 2], 'o', markerfacecolor=col,
                                 markeredgecolor='k', markersize=6)

                    plt.title('Estimated number of clusters: %d' % n_clusters_)
                    plt.show()
                except:
                    print "There is no data for the subject "