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
mean = []
g=n=h=z=0
for i in _SUBJECT:
    for j in _INTENSITY:
        for o in _TYPE:
            for l in _MUSCLES:
                try:
                    _PATH = 'data/'+i+"_"+j+"_"+o+"_"+l+"_flag_DB.txt"
                    print _PATH
                    f = np.loadtxt(_PATH, delimiter='\t', usecols=[0, 1, 2])
                    ID = np.loadtxt(_PATH, delimiter='\t', usecols=[3])
                    # if ID[0] != "":
                    #     a = f[3:, :]
                    #     a =a[0:30]
                    # else:
                    a = f[:, :]
                        # a = a[0:30]
                    #print a
                    for k in range (0,len(a),3):
                        print ID[k],ID[k+1], ID[k+2]
                        if ID[k] != -1 and ID[k+1] != -1:
                            ED1 = np.sqrt((a[k, 0] - a[k+1, 0]) ** 2 + (a[k, 1] - a[k+1, 1]) ** 2 + (a[k, 2] - a[k+1, 2]) ** 2)
                            if ED1<=10:
                                mean.append(ED1)
                            g=g+1
                        if ID[k] != -1 and ID[k+2] != -1:
                            ED2 = np.sqrt(
                                (a[k, 0] - a[k + 2, 0]) ** 2 + (a[k, 1] - a[k + 2, 1]) ** 2 + (a[k, 2] - a[k + 2, 2]) ** 2)
                            if ED2<=10:
                                mean.append(ED2)
                            h = h+1
                        if ID[k+1] != -1 and ID[k+2] != -1:
                            ED3 = np.sqrt(
                                (a[k + 2, 0] - a[k + 1, 0]) ** 2 + (a[k + 2, 1] - a[k + 1, 1]) ** 2 + (a[k + 2, 2] - a[k + 1, 2]) ** 2)
                            if ED3<=10:
                                mean.append(ED3)
                            n = n+1
                except:
                    print "There is no data for the subject "


print g,h,n,z

print np.mean(mean)
print np.std(mean)

