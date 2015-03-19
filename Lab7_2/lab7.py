from pylab import *
from scipy import optimize as op
import cmath as cm
import numpy as np
from scipy import optimize as op

def lab7():
    t = arange(-5,5,0.05)
    dt = t[1] - t[0]
    N = len(t)
    T = t[N-1] - t[0]

    u1 = np.exp(-(t/1) ** 2)
    u2 = np.exp(-(t/2) ** 2)
    delta = ((-1 + 2*np.random.rand(1,N)) * max(np.abs(u1)) * 0.0575)[0]
    epsilon = ((-1 + 2*np.random.rand(1,N)) * max(np.abs(u1)) * 0.0575)[0]

    u1s = fftpack.fft(u1)
    u2s = fftpack.fft(u2)

    def rho(alpha):
        m = arange(0,N,1)
        zetta = 1 + (2*math.pi*m/T) ** 2
        beta = dt / N * sum(alpha**2 * zetta * abs(u1s)**2 / (abs(u2s)**2 * dt**2 + alpha*zetta)**2)
        gamma = dt / N * sum(abs(u2s)**2 * dt**2 * abs(u1s)**2 * zetta / (abs(u2s)**2 * dt**2 + alpha*(1 - 2*math.pi*m/T)**2)**2)
        return beta - (std(delta) + std(epsilon)*np.sqrt(gamma))**2

    alpha = op.bisect(rho,0.001,1)

    def H(k):
        k = array([k]).T
        m = arange(0,N,1)
        h = dt / N * np.sum(np.exp(2*math.pi*1j*k*m/N) * tile(u1s * u1s.conj() / (abs(u2s)**2 * dt**2 +
                    alpha*(1 + (2*math.pi*m/T)**2)), (N,1)),1)
        return h.real

    fig, axes = plt.subplots()

    axes.plot(t, u1, label='u1')
    axes.plot(t, u2, label='u2')
    axes.plot(t, delta, label='delta')
    axes.plot(t, epsilon, label='epsilon')
    axes.plot(t, real(fftpack.ifft(u2s * H(arange(0,N,1)))), label='filter')
    axes.grid(True)
    axes.legend(loc=0)

    plt.show()

lab7()