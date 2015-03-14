from pylab import *
from scipy import optimize as op
import cmath as cm
import numpy as np

def lab7():
    t = arange(-5,5,0.05)
    dt = t[1] - t[0]
    N = len(t)
    T = t[N-1] - t[0]

    u1 = np.exp(-(t/1) ** 2)
    u2 = np.exp(-(t/2) ** 2)
    delta = ((-1 + 2*np.random.rand(1,N)) * max(np.abs(u1)) * 0.05)[0]
    epsilon = ((-1 + 2*np.random.rand(1,N)) * max(np.abs(u1)) * 0.05)[0]

    u1s = fftpack.fft(u1)
    u2s = fftpack.fft(u2)

    def rho(alpha):
        m = arange(0,N,1)
        zetta = 1 + (2*math.pi*m/T) ** 2
        beta = dt / N * sum(alpha**2 * zetta * abs(u1s)**2 / (abs(u2s)**2 * dt**2 + alpha*zetta)**2 )
        gamma = dt / N * sum(abs(u2s)**2 * dt**2 * abs(u1s)**2 * zetta / (abs(u2s)**2 * dt**2 + alpha*(1 - 2*math.pi*m/T)**2)**2)
        return beta - (std(delta) + std(epsilon)*np.sqrt(gamma))**2

    alpha = op.fsolve(rho,array([0.5]))[0]

    def H(k):
        #k = np.transpose(k)
        m = arange(0,N,1)
        temp = np.exp(2*math.pi*1j*k*m/N)
        h = zeros(N)
        for i in range(1,N-1):
            h[i] = dt / N * np.sum(np.exp(2*math.pi*1j*k[i]*m/N) * u1s * u1s.conj() / (abs(u2s)**2 * dt**2 +
                    alpha*(1 + (2*math.pi*m/T)**2)))

        # h = dt / N * np.sum(np.exp(2*math.pi*1j*k*m/N) * tile(u1s * u1s.conj() / (abs(u2s)**2 * dt**2 +
        #             alpha*(1 + (2*math.pi*m/T)**2)), (N,1)),1)
        #h = transpose(h)
        return h.real

    fig, axes = plt.subplots(2,1)

    # axes[0].plot(t, u1)
    # axes[0].plot(t, u2)
    # axes[0].plot(t, delta)
    # axes[0].plot(t, epsilon)
    # axes[0].plot(t, real(fftpack.ifft(u2s * H(arange(0,N,1)))))
    #
    # temp = H(arange(0,N,1))
    # axes[1].plot(arange(0,N,1), H(arange(0,N,1)))

    axes[0].plot(t, u1, label='u1')
    axes[0].plot(t, u2, label='u2')
    axes[0].plot(t, delta, label='delta')
    axes[0].plot(t, epsilon, label='epsilon')
    axes[0].plot(t, real(fftpack.ifft(u2s * H(arange(0,N,1)))), label='reconstracted')
    axes[0].grid(True)
    axes[0].legend(loc=0)
    axes[1].plot(arange(0,N,1), H(arange(0,N,1)))

    plt.show()

lab7()