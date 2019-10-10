#!/usr/bin/python3
#McDermott
#2019-10-08

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import cm
from slread import slread
plt.rcParams['animation.ffmpeg_path'] = '/Applications/ffmpeg'
FFwriter = animation.FFMpegWriter(fps=30)

# case parameters (copied from FDS input file)

nx = 20
ny = 20
Lx = 1
Ly = 1
dx = Lx/nx
dy = Ly/ny

# read FDS cell centered slice file

slcf = '../fds/test_02.sf'
t_start = 0.
t_end = 10.
nframes = 10

(Q,Time)=slread(slcf,t_start,t_end,nframes)

# cell center locations mesh

xc = np.arange(dx/2, Lx+dx/2, dx)
yc = np.arange(dy/2, Ly+dy/2, dy)
XC, YC = np.meshgrid(xc, yc)

# mesh face locations

xf = np.arange(0, Lx+dx, dx)
yf = np.arange(0, Ly+dy, dy)
XF, YF = np.meshgrid(xf, yf)

# create movie from slice file

fig = plt.figure()

ims = []
for i in range(nframes):
    im=plt.imshow(Q[1:nx+1,1:ny+1,i], origin="lower", cmap=plt.get_cmap('jet'), interpolation="nearest", extent=[0,Lx,0,Ly], animated=True)
    if i==0:
        plt.colorbar()
    plt.plot(XF, YF, 'k-', lw=0.5, alpha=0.5)
    plt.plot(XF.T, YF.T, 'k-', lw=0.5, alpha=0.5)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

ani.save("movie.mp4", writer=FFwriter)

plt.show(block=False)



