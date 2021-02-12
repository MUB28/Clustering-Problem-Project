from math import *
import numpy as np
from random import *
import datetime
from argparse import ArgumentParser


#start = datetime.datetime.now()

def cluster(ps1, iters = 10):
   

    k=3
    ps = np.array(ps1)    
    

    # I use Pandas to read the content of samples.csv and store the information of the file in an array which I call ps. 

    m=np.array([ps[randrange(len(ps))], ps[randrange(len(ps))], ps[randrange(len(ps))]])
    #Below I have changed alloc from a list to an array
    alloc=np.array([None]*len(ps))
    n=0

    #Below I have replaced the while loop with a for loop to simplify my code.
    #In addition, we used the hypotenuse function from numpy to define d[0], d[1] and d[2] in order to spped up the code and to make it more compact.  
    for j in range(iters):
            for i in range(len(ps)):
                p=ps
                d=np.empty(shape=(3,1))
                a=(p[i]-m[0])
                b=(p[i]-m[1])
                c=(p[i]-m[2])
                d[0]=np.hypot(a[0],a[1])
                d[1]=np.hypot(b[0],b[1])
                d[2]=np.hypot(c[0],c[1])
                alloc[i]=(np.argmin(d,axis=0))

            m[0]=np.sum(ps[np.argwhere(alloc==0)],axis=0)/len(np.argwhere(alloc==0))
            m[1]=np.sum(ps[np.argwhere(alloc==1)],axis=0)/len(np.argwhere(alloc==1))
            m[2]=np.sum(ps[np.argwhere(alloc==2)],axis=0)/len(np.argwhere(alloc==2))  

        # The argwhere function is used to find the indices of array elements that are non-zero, grouped by element.
        # In this case we are looking for the indicies in our alloc array that give us the values we are looking for.


    print("Cluster " + str(0) + " is centred at " + str(m[0]) + " and has " + str(len(np.argwhere(alloc ==0))) + " points.")
    print("Cluster " + str(1) + " is centred at " + str(m[1]) + " and has " + str(len(np.argwhere(alloc ==1))) + " points.")
    print("Cluster " + str(2) + " is centred at " + str(m[2]) + " and has " + str(len(np.argwhere(alloc ==2))) + " points.")

if __name__ == "__main__":
    
     parser = ArgumentParser(description='clustering_numpy')

     parser.add_argument('samples_file', type=str,
                         help='Gives the pathname to the samples CSV file.')
     parser.add_argument('--iters',default = 10, type=int,
                         help='Gives the number of iterations the code runs for.')
    

     arguments=parser.parse_args()

     filename = arguments.samples_file

     lines = open(filename, 'r').readlines()
     ps1 = []

     for line in lines: ps1.append(tuple(map(float, line.strip().split(','))))
     
     cluster(ps1, arguments.iters)



