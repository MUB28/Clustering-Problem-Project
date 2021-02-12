from math import sqrt
from random import randrange
from auxiliary_functions import magnitude
from argparse import ArgumentParser



def cluster(data, iters = 10):

    clusters = 3

    

    random = randrange(len(data))

    m = [data[randrange(len(data))], data[randrange(len(data))], data[randrange(len(data))]]

    alloc = [None]*len(data)
    n = 0
    while n < iters:
        for i in data:
            p = i
            rank = data.index(i)
            d = [None] * clusters
            d[0] = magnitude(m, p, 0)
            d[1] = magnitude(m, p, 1)
            d[2] = magnitude(m, p, 2)
            alloc[rank] = d.index(min(d))
        for i in range(clusters):
            alloc_data = [p for j, p in enumerate(data) if alloc[j] == i]
            new_mean = (sum([a[0] for a in alloc_data]) / len(alloc_data), sum([a[1] for a in alloc_data]) / len(alloc_data))
            m[i] = new_mean
        n = n +1

    for i in range(clusters):
      alloc_data=[p for j, p in enumerate(data) if alloc[j] == i]
      print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_data)) + " points.")

if __name__ == "__main__":
    
    parser = ArgumentParser(description='clustering')

    parser.add_argument('samples_file', type=str,
                        help='Gives the pathname to the samples CSV file.')
    parser.add_argument('--iters',default = 10, type=int,
                        help='Gives the number of iterations the code runs for.')
    

    argument = parser.parse_args()
    lines = open(argument.samples_file, 'r').readlines()
    data = []

    for line in lines: data.append(tuple(map(float, line.strip().split(','))))
    cluster(data,argument.iters)