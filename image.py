#!python
#!/usr/bin/env python

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy
from numpy import random as rng

def PairIndices(z):
    r = len(z)
    c = len(z[0])
    pairs = []
    for i in range(0, r):
        for j in range(0, c):
            if j != (c-1):
                pairs.append(((i,j),(i,j+1)))

            if i != (r-1):
                pairs.append(((i,j),(i+1,j)))

    return pairs

def Energy(z, x, h, beta, nu):
    term1 = h * numpy.sum(z.flatten())
    zpairs = []
    for pair in PairIndices(z):
        i1,j1 = pair[0]
        i2,j2 = pair[1]
        zpairs.append((z[i1][j1], z[i2][j2]))

    term2 = -beta * numpy.sum([z1*z2 for z1,z2 in zpairs])
    term3 = -nu * numpy.sum([zi*xi for zi,xi in zip(z.flatten(), x.flatten())])
    return term1 + term2 + term3

mat = loadmat('data/hw1_images.mat')
z = mat['origImg']
x = mat['noisyImg']

# corrupt x even more
# nrows = len(x)
# ncols = len(x[0])
# for r in range(0,nrows):
#     for c in range(0, ncols):
#         if rng.random() < 0.3:
#             x[r][c] *= -1

plt.subplot(2, 2, 1)
plt.imshow(z, cmap="gray")

plt.subplot(2, 2, 2)
plt.imshow(x, cmap="gray")

# plt.show()

# sx = z

# plt.subplot(2, 2,3)
# plt.imshow(sx, cmap="gray")

h = 1
beta = 10
nu = 1
energy = Energy(z, x, h, beta, nu)
print("Initial energy = {0}".format(energy))

# estimate z with y - initialize to noisy value (x)
y = x
r = len(y)
c = len(y[0])
counter = 0
# iterate and denoise the image
for i in range(5):
    print("iteration: {0}".format(counter))
    counter += 1
    for iRow in range(0, r):
        for iCol in range(0, c):
            # val
            curVal = y[iRow][iCol]
            newVal = -1 * curVal

            # edge pair product
            curPair = 0
            newPair = 0
            if iRow != (r-1):
                curPair += curVal * y[iRow+1][iCol]
                newPair += newVal * y[iRow+1][iCol]

            if iCol != (c-1):
                curPair += curVal * y[iRow][iCol+1]
                newPair += newVal * y[iRow][iCol+1]

            # product of noisy val
            curProd = curVal * x[iRow][iCol]
            newProd = newVal * x[iRow][iCol]

            # delta energy
            delta_term1 = h * (newVal - curVal)
            delta_term2 = -beta * (newPair - curPair)
            delta_term3 = -nu * (newProd - curProd)

            delta_energy = delta_term1 + delta_term2 + delta_term3
            if delta_energy < 0:
                energy += delta_energy
                y[iRow][iCol] = newVal

    print("total energy: {0}".format(energy))

# plot y
plt.subplot(2, 2, 3)
plt.imshow(y, cmap="gray")

plt.show()
