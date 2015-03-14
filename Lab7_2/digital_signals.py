import math
from pylab import *


class GaussianSignal:
    """
    Class represents settings for discretization of a signal

    x_dft, y_dft - samples of signal
    w_dft, f_dft - frequency, DFT points
    dft_samples - number of samples taken
    dt - distance between points in reconstructed signal
    global_limit - left and right limits of the signal on plot
    title - title of plot
    """

    x_dft, y_dft, y_dft_filter = None, None, None
    w_dft, f_dft, f_dft_filter = None, None, None
    dft_samples = 400
    dt = 0.025
    noise = 0.05

    global_limit = dft_samples * dt / 2
    title = 'Gaussian signal'

    amplitude = 1
    sigma = 1

    def __init__(self, sigma):
        self.sigma = sigma

    def make_signal(self):
        signal_vectorized = vectorize(self.signal)
        self.x_dft = linspace(-self.global_limit, self.global_limit, self.dft_samples)
        self.y_dft = signal_vectorized(self.x_dft)

    def make_fourier_transform(self):
        self.w_dft = linspace(0, 1.0 / (2.0 * self.dt), self.dft_samples)
        self.f_dft = fftpack.fft(self.y_dft)

    def signal(self, x):
        return self.amplitude * math.exp(-x ** 2 / self.sigma ** 2)