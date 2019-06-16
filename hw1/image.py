#!python
#!/usr/bin/env python

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy

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

def ImageErrorRate(orig, estimate):
    r = len(orig)
    c = len(orig[0])
    err = 0
    for i in range(0, r):
        for j in range(0, c):
            if estimate[i][j] != orig[i][j]:
                err = err + 1

    return (err / (r*c))

mat = loadmat('data/hw1_images.mat')
z = mat['origImg']
x = mat['noisyImg']

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.imshow(z, cmap="gray")
ax1.set_ylabel("Original Image")

ax2.imshow(x, cmap="gray")
ax2.set_ylabel("Noisy Image")

# sx = z

# plt.subplot(2, 2,3)
# plt.imshow(sx, cmap="gray")

h = 1
beta = 7
nu = 10
energy = Energy(z, x, h, beta, nu)
print("Initial energy = {0}".format(energy))

# estimate z with y - initialize to noisy value (x)
y = x
r = len(y)
c = len(y[0])
counter = 0
# iterate and denoise the image
for i in range(10):
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

err = ImageErrorRate(z, y)
print("Error rate: {0}".format(err))

# plot y
ax3.imshow(y, cmap="gray")
ax3.set_ylabel("Denoised Image")

plt.show()
