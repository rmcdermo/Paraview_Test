#!/usr/bin/python3
#McDermott
#2019-10-08

import numpy as np
import matplotlib.pyplot as plt
from slread import slread

# case parameters (copied from FDS input file)

nx = 20
ny = 20
Lx = 1
Ly = 1
dx = Lx/nx
dy = Ly/ny

# read FDS slice file

slcf = '../fds/test_01.sf'
t_start = 0.
t_end = 10.
nframes = 10

(Q,Time)=slread(slcf,t_start,t_end,nframes)

# create contour image of Quantity

fig = plt.figure()

x = np.arange(0., Lx+dx, dx)
y = np.arange(0., Ly+dy, dy)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, Q[:,:,1], 10, cmap=plt.get_cmap('hot'))

plt.show(block=False)
