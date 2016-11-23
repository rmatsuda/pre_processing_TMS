import numpy as np
from sklearn.cluster import AffinityPropagation

from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
_SUBJECT = "09"
_MUSCLES = ["ADM", "FCP", "FRC"]
_INTENSITY = ["110", "120"]

for i in _MUSCLES:
    for j in _INTENSITY:
        _PATH = 'data/'+_SUBJECT+"_"+i+"_"+j+".txt"
        print _PATH
        f = np.loadtxt(_PATH)
        X = f[:,0:3]
        af = AffinityPropagation(preference=-50).fit(X)
        cluster_centers_indices = af.cluster_centers_indices_
        labels = af.labels_
        n_clusters_ = len(cluster_centers_indices)

        print('Estimated number of clusters: %d' % n_clusters_)

        x=X[:,0]
        y=X[:,1]
        z=X[:,2]
        w = (np.array([x,y,z,labels])).T
        np.savetxt(_PATH[0:len(_PATH)-4]+'_flag.txt', w, fmt = '%.3f', delimiter='\t')

        fig = plt.figure()

        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters_), colors):
            class_members = labels == k
            cluster_center = X[cluster_centers_indices[k]]
            plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
            plt.plot(cluster_center[0], cluster_center[1], '+', markerfacecolor=col,
                     markeredgecolor='k', markersize=14)
            for x in X[class_members]:
                plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
        plt.show()

# plt.close('all')
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# color=cm.rainbow(np.linspace(0,1,len(X)))
# for i in range (0,len(X),3):
#     ax.scatter(X[i:i+3,0],X[i:i+3,1],X[i:i+3,2],c=color[i])
#
# colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# for k, col in zip(range(n_clusters_), colors):
#     class_members = labels == k
#     cluster_center = X[cluster_centers_indices[k]]
#     plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=14)
#     for x in X[class_members]:
#         plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

# plt.title('Estimated number of clusters: %d' % n_clusters_)

#np.savetxt()

# plt.show()



