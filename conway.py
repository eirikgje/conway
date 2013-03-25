import numpy as np
from pylab import *
#import matplotlib.pyplot as plt
import time

ion()
hold(False)

#def map_to_neigh(num):
#    if num == 0: 
#        return (1, 0)
#    if num == 1:
#        return (1, 1)
#    if num == 2:
#        return (0, 1)
#    if num == 3:
#        return (-1, 1)
#    if num == 4:
#        return (0, -1)
#    if num == 5:
#        return (-1, 0)
#    if num == 6:
#        return (-1, -1)
#    if num == 7:
#        return (1, -1)
numcells = 10
numstarts = 2000

living = np.zeros((numcells, numcells), dtype=int).flatten()
living_next = np.zeros((numcells, numcells), dtype=int).flatten()

#start = (np.random.rand(numstarts) * numcells **2).astype(int)
#start = np.array([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38]) + 5 * numcells + 1
start = np.array([2*numcells, 2 * numcells + 1, 2 * numcells + 2, numcells + 2, 1]) + 8
living[start] = 1

#np.save('conway_state.npy', living)

#living[xstart, ystart] = True
m = imshow(np.reshape(living, (numcells, numcells)), interpolation='none')
draw()
time.sleep(0.1)

#neighbors = np.zeros((8, numcells, numcells), dtype=int)

while True:
    for i in xrange(1, numcells * numcells - 1):
        num_neighbors = 0
        num_neighbors += np.sum(np.roll(living, -numcells)[i-1:i+2])
        num_neighbors += np.sum(np.roll(living, numcells)[i-1:i+2])
        num_neighbors += living[i-1] + living[i+1]
        living_next[i] = (living[i] and (num_neighbors == 2 or num_neighbors == 3)) or (not living[i] and num_neighbors == 3)
    for i in (0, numcells * numcells -1):
#    i = numcells * numcells - 1
        num_neighbors = 0
        if i == 0:
            num_neighbors += np.sum(living[numcells*numcells - numcells - 1:numcells *numcells - numcells + 2])
            num_neighbors += np.sum(living[numcells - 1:numcells+2])
            num_neighbors += living[-1] + living[1]
        else:
            num_neighbors += np.sum(living[i - numcells-1:i-numcells + 2])
            num_neighbors += living[i-1] + living[0]
            num_neighbors += np.sum(living[numcells-1:numcells+2])
        living_next[i] = (living[i] and (num_neighbors == 2 or num_neighbors == 3)) or (not living[i] and num_neighbors == 3)
    living = living_next.copy()
    m.set_data(np.reshape(living, (numcells, numcells)))
    draw()
    time.sleep(0.1)

#for k in xrange(100):
#    for i in xrange(numcells):
#        for j in xrange(numcells):
#            num_neighbors = 0
#            for l in xrange(8):
#                nums = np.array(map_to_neigh(l))
#                nums[0] += i
#                nums[1] += j
#                if any(nums < 0) or any(nums > numcells-1):
#                    continue
#                if living[nums[0], nums[1]]: num_neighbors += 1
#            if living[i, j]:
#                if num_neighbors != 2:
#                    living[i, j] = False
#            else:
#                if num_neighbors == 3:
#                    living[i, j] = True
#    print np.sum(living)
#    m.set_data(living)
#    draw()
#    time.sleep(0.20)

    
#    living = cells.copy()
#    dead = np.logical_not(living)
#    neigh1 = cells[1:, :]
#    neigh2 = cells[:-1, :]
#    neigh3 = cells[:, 1:]
#    neigh4 = cells[:, :-1]
#    live_oneneighbor[1:-1, 1:-1] = living[1:-1, 1:-1] & (neigh1 | neigh2 | neigh3 | neigh4)
#    live_oneneighbor[0, :] = living[0, :] & neigh1[0, :]
#    live_oneneighbor[-1, :] = living[-1, :] & neigh2[-1, :]
#    live_oneneighbor[:, 0] = living[:, 0] & neigh3[:, 0]
#    live_oneneighbor[:, -1] = living[:, -1] & neigh4[:, -1]
#    live_zeroneighbor[1:-1, 1:-1] = living[1:-1, 1:-1] & np.logical_not((neigh1 | neigh2 | neigh3 | neigh4))
