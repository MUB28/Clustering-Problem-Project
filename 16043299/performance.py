import numpy as np 
import matplotlib.pyplot as plt 
from clustering import cluster
from clustering_numpy import cluster as cn
import datetime

def samples(n):

    x = np.random.rand(n)
    y = np.random.rand(n)

    data = []
    for i in range(n):
        data.append((x[i],y[i]))    

  
    return data

x = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


y = []
z = []

for i in x :

    cf = samples(i)
    start = datetime.datetime.now()
    cluster(cf)  
    finish = datetime.datetime.now()
    z.append((finish-start).total_seconds())

for i in x :

    cf = samples(i)
   
    begin = datetime.datetime.now()
    cn(cf)  
    end = datetime.datetime.now()
    y.append((end-begin).total_seconds())

plt.plot(x,y, label = 'Clustering function with numpy') 
plt.plot(x,z, label = 'Clustering function without numpy')
plt.xlabel('Sample size')
plt.ylabel('Time taken')
plt.title('Performance')
plt.legend()
plt.show()

