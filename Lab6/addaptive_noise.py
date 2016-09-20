from pylab import *
import numpy as np


class DigitalNoise:
    y_noise = None
    f_noise = None

    def make_noise(self,sig):
        for n, point in enumerate(self.y_noise):
            sig.y_dft[n] += point

    def make_fourier_transform(self):
        self.f_noise = fftpack.fft(self.y_noise)


class ImpulseNoise(DigitalNoise):
    num_impulses = 7
    min_amplitude = 0.5
    max_amplitude = 1
    title = 'Impulse Noise'

    def __init__(self, n_samples):
        self.create_noise(n_samples)

    def create_noise(self, samples):
        self.y_noise = zeros(samples)
        for i in range(self.num_impulses):
            amplitude = (self.max_amplitude-self.min_amplitude)*np.random.random_sample() + self.min_amplitude
            point = np.random.randint(0,samples)
            self.y_noise[point] += amplitude


class GaussianNoise(DigitalNoise):
    mu = 0
    sigma = 0.4
    scale = 0.3
    title = 'Gaussian Noise'

    def __init__(self, samples):
        self.create_noise(samples)

    def create_noise(self, samples):
        self.y_noise = zeros(samples)
        for i in range(samples):
            self.y_noise[i] += self.scale*(self.sigma*np.random.randn() + self.mu)
