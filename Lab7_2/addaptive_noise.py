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

    def standart_deviation(self):
        return std(self.y_noise)

# class ImpulseNoise(DigitalNoise):
#     num_impulses = 30
#     amplitude = 0.05
#     title = 'Impulse Noise'
#
#     def __init__(self, n_samples):
#         self.create_noise(n_samples)
#
#     def create_noise(self, samples):
#         self.y_noise = zeros(samples)
#         for i in range(self.num_impulses):
#             point = np.random.randint(0,samples)
#             self.y_noise[point] = self.amplitude

class ImpulseNoise(DigitalNoise):
    min_amplitude = 0
    max_amplitude = 0.05
    title = 'Impulse Noise'

    def __init__(self, n_samples):
        self.create_noise(n_samples)

    def create_noise(self, samples):
        self.y_noise = zeros(samples)
        for point in range(samples):
            amplitude = (self.max_amplitude-self.min_amplitude)*np.random.random_sample() + self.min_amplitude
            self.y_noise[point] += amplitude