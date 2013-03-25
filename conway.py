import numpy as np
from pylab import *
#import matplotlib.pyplot as plt
import time

ion()
hold(False)

numcells = 100
numstarts = 2000

nind = np.arange(numcells*numcells)
nind = np.reshape(nind, (numcells, numcells))
neighbors = np.zeros((numcells, numcells, 8), dtype=int)
for i in xrange(1, numcells - 1):
    for j in xrange(1, numcells - 1):
        neighbors[i, j, 0] = nind[i+1, j]
        neighbors[i, j, 1] = nind[i+1, j+1]
        neighbors[i, j, 2] = nind[i, j+1]
        neighbors[i, j, 3] = nind[i-1, j + 1]
        neighbors[i, j, 4] = nind[i-1, j]
        neighbors[i, j, 5] = nind[i -1, j - 1]
        neighbors[i, j, 6] = nind[i, j-1]
        neighbors[i, j, 7] = nind[i+1, j-1]
for i in xrange(1, numcells - 1):
    neighbors[i, 0, 0] = nind[i+1, 0]
    neighbors[i, 0, 1] = nind[i+1, 1]
    neighbors[i, 0, 2] = nind[i, 1]
    neighbors[i, 0, 3] = nind[i-1, 1]
    neighbors[i, 0, 4] = nind[i-1, 0]
    neighbors[i, 0, 5] = nind[i-1, -1]
    neighbors[i, 0, 6] = nind[i, -1]
    neighbors[i, 0, 7] = nind[i+1, -1]
    neighbors[i, -1, 0] = nind[i+1, -1]
    neighbors[i, -1, 1] = nind[i+1, 0]
    neighbors[i, -1, 2] = nind[i, 0]
    neighbors[i, -1, 3] = nind[i-1, 0]
    neighbors[i, -1, 4] = nind[i-1, -1]
    neighbors[i, -1, 5] = nind[i-1, -2]
    neighbors[i, -1, 6] = nind[i, -2]
    neighbors[i, -1, 7] = nind[i+1, -2]
    neighbors[0, i, 0] = nind[-1, i]
    neighbors[0, i, 1] = nind[-1, i+1]
    neighbors[0, i, 2] = nind[0, i+1]
    neighbors[0, i, 3] = nind[1, i+1]
    neighbors[0, i, 4] = nind[1, i]
    neighbors[0, i, 5] = nind[1, i-1]
    neighbors[0, i, 6] = nind[0, i-1]
    neighbors[0, i, 7] = nind[-1,i-1]
    neighbors[-1, i, 0] = nind[-2, i]
    neighbors[-1, i, 1] = nind[-2, i+1]
    neighbors[-1, i, 2] = nind[-1, i+1]
    neighbors[-1, i, 3] = nind[0, i+1]
    neighbors[-1, i, 4] = nind[0, i]
    neighbors[-1, i, 5] = nind[0, i-1]
    neighbors[-1, i, 6] = nind[-1, i-1]
    neighbors[-1, i, 7] = nind[-2, i-1]
#corners
neighbors[0, 0, 0] = nind[-1, 0]
neighbors[0, 0, 1] = nind[-1, 1]
neighbors[0, 0, 2] = nind[0, 1]
neighbors[0, 0, 3] = nind[1, 1]
neighbors[0, 0, 4] = nind[1, 0]
neighbors[0, 0, 5] = nind[1, -1]
neighbors[0, 0, 6] = nind[0, -1]
neighbors[0, 0, 7] = nind[-1, -1]
neighbors[0, -1, 0] = nind[-1, -1]
neighbors[0, -1, 1] = nind[-1, 0]
neighbors[0, -1, 2] = nind[0, 0]
neighbors[0, -1, 3] = nind[1, 0]
neighbors[0, -1, 4] = nind[1, -1]
neighbors[0, -1, 5] = nind[1, -2]
neighbors[0, -1, 6] = nind[0, -2]
neighbors[0, -1, 7] = nind[-1, -2]
neighbors[-1, 0, 0] = nind[-2, 0]
neighbors[-1, 0, 1] = nind[-2, 1]
neighbors[-1, 0, 2] = nind[-1, 1]
neighbors[-1, 0, 3] = nind[0, 1]
neighbors[-1, 0, 4] = nind[0, 0]
neighbors[-1, 0, 5] = nind[0, -1]
neighbors[-1, 0, 6] = nind[-1, -1]
neighbors[-1, 0, 7] = nind[-2, -1]
neighbors[-1, -1, 0] = nind[-2, -1]
neighbors[-1, -1, 1] = nind[-2, 0]
neighbors[-1, -1, 2] = nind[-1, 0]
neighbors[-1, -1, 3] = nind[0, 0]
neighbors[-1, -1, 4] = nind[0, -1]
neighbors[-1, -1, 5] = nind[0, -2]
neighbors[-1, -1, 6] = nind[-1, -2]
neighbors[-1, -1, 7] = nind[-2, -2]

living = np.zeros((numcells, numcells), dtype=int)
living_next = np.zeros((numcells, numcells), dtype=int)

#start = (np.random.rand(numstarts) * numcells **2).astype(int)
#start = np.array([[2, 0], [2, 1], [2, 2], [1, 2], [0, 1]])

#Slider
#start = [(2, 0), (2, 1), (2, 2), (1, 2), (0, 1)]
#for i in range(len(start)):
#    living[start[i]] = 1


#Block-laying switch engine (will go on indefinitely with an infinitely large grid)
start = np.array([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38])
for i in start:
    living[25, i] = 1

#np.save('conway_state.npy', living)

m = imshow(np.reshape(living, (numcells, numcells)), interpolation='none')
draw()
time.sleep(2)

#neighbors = np.zeros((8, numcells, numcells), dtype=int)

while True:
    for i in xrange(numcells):
        for j in xrange(numcells):
            num_neighbors = np.sum(living.flatten()[neighbors[i, j]])
            living_next[i, j] = (living[i, j] and (num_neighbors == 2 or num_neighbors == 3)) or (not living[i, j] and num_neighbors == 3)
    living = living_next.copy()
    m.set_data(living)
    draw()
    time.sleep(0.1)
