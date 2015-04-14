from pylab import *
from scipy import optimize as op
import cmath as cm
import numpy as np
from scipy import optimize as op

def lab7():
    t = arange(-5,5,0.01)
    dt = t[1] - t[0]
    N = len(t)
    T = t[N-1] - t[0]

    u1 = np.exp(-(t/1) ** 2)
    for i in range(6):
        amplitude = 0.7*np.random.random_sample()
        point = np.random.randint(0,N)
        u1[point] += amplitude

    eps_r = 4
    eps = 0.0001

    def smooth_signal(u, smth_area):
        uk = zeros(N)
        for i in range(0,N-1):
            if i<eps_r:
                area = u[0:eps_r*2+1]
                area = np.delete(area,i,0)
            elif i>N-eps_r-1:
                area = u[N-eps_r*2-1:N]
                area = np.delete(area,i-N+1+eps_r*2,0)
            else:
                area = u[i-eps_r:i+eps_r+1]
                area = np.delete(area,eps_r,0)

            if check_smth(u[i],area,smth_area):
                uk[i] = u[i]
            else:
                uk[i] = smth_area(area)
        return uk

    def check_smth(vk,area,smth_area):
        return abs(vk - smth_area(area)) < eps

    def mean(area):
        return sum(area)/(len(area))

    def med(area):
        return np.median(area)

    umean = smooth_signal(u1,mean)
    umed = smooth_signal(u1,med)


    fig, axes = plt.subplots(3)

    axes[0].plot(t, u1, label='signal')
    axes[1].plot(t, umean, label='mean')
    axes[2].plot(t, umed, label='median')

    for axis in axes:
        axis.grid(True)
        axis.legend(loc=0)

    plt.show()

lab7()