# -*- coding: cp1251 -*-

from collections import namedtuple
from pylab import *

class DigitalSignal:
    x_sample = None
    y_sample = None
    x_recon = None
    y_recon = None
    dt = 0.1
    num_samples = 100
    global_limit = num_samples * dt/2
    title = 'signal'
    k_limit = 100
    t_samples = 5000

class ImpulseSignal(DigitalSignal):
    def __init__(self):
        self.title = 'Impulse signal'

    impulse_limit = 1
    amplitude = 1

    def signal(self, x):
        return self.amplitude if -self.impulse_limit <= x <= self.impulse_limit else 0


class GaussianSignal(DigitalSignal):
    def __init__(self):
        self.title = 'Gaussian signal'

    sigma = 0.2
    amplitude = 1

    def signal(self, x):
        return self.amplitude*math.exp(-x**2/self.sigma**2)


def kotelnikov(sig, t):
    sum = 0
    for k in range(-sig.k_limit, sig.k_limit, 1):
        sum += sig.signal(k*sig.dt) * my_sinc(math.pi/sig.dt*(t-k*sig.dt))
    return sum


def my_sinc(x):
    if x != 0:
        return math.sin(x) / x
    else:
        return 1.0

def discretize_impulse(sg, axes):
    signal_vectorized = vectorize(sg.signal)
    kotelnikov_vectorized = vectorize(kotelnikov)

    sg.x_sample = linspace(-sg.global_limit, sg.global_limit, sg.num_samples)
    sg.y_sample = signal_vectorized(sg.x_sample)

    sg.x_recon = linspace(-sg.global_limit, sg.global_limit, sg.t_samples) # TODO: number to var
    """sg.y_recon = list()
    for t in sg.x_recon:
        sg.y_recon.append(kotelnikov(sg,t))
    sg.y_recon = array(sg.y_recon)"""
    sg.y_recon = kotelnikov_vectorized(sg,sg.x_recon)

    axes.plot(sg.x_sample,sg.y_sample,'r', marker='o', markersize=4)
    axes.plot(sg.x_recon, sg.y_recon, 'g')
    axes.axis('tight')
    axes.set_title(sg.title)


def main():
    fig, axes = plt.subplots(1,2)
    axes[0].margins(0.05)
    axes[1].margins(0.05)

    imp_sig = ImpulseSignal()
    discretize_impulse(imp_sig,axes[0])

    gaus_sig = GaussianSignal()
    discretize_impulse(gaus_sig,axes[1])

    plt.tight_layout()
    plt.show()


main()





def discretize_impulse1():
    dt = input('Enter step of discretization: ')
    num_samples = input('Enter number of samples: ')
    impulse_left_limit = input('Enter left limit of impulse: ')
    impulse_right_limit = - impulse_left_limit
    amplitude = input('Enter amplitude of impulse: ')

    global_segment = num_samples * dt
    global_left_limit = -global_segment/2
    global_right_limit = global_segment/2

    x = linspace(global_left_limit,global_right_limit,num_samples)
    impulse_vectorized = vectorize(impulse_signal)
    y = impulse_vectorized(x,amplitude,impulse_left_limit,impulse_right_limit)

    Plot_data = namedtuple('Plot_data','x0','y0','x1','y1','title','bottom','top')
    data = Plot_data(x,y,'Impulse Signal',)