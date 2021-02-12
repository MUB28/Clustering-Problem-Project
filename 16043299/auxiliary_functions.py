from math import sqrt
from random import randrange


def magnitude(m, p, x):
    return sqrt((p[0]-m[x][0])**2 + (p[1]-m[x][1])**2)

