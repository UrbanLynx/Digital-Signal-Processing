import numpy as np


class ImpulseNoise:
    num_impulses = 10
    min_amplitude = 0.5
    max_amplitude = 1

    def make_noise(self, sig):
        for i in range(self.num_impulses):
            amplitude = (self.max_amplitude-self.min_amplitude)*np.random.random_sample() + self.min_amplitude
            point = np.random.randint(0,sig.dft_samples)
            sig.y_dft[point] += amplitude


class GaussianNoise:
    mu = 0
    sigma = 0.4
    scale = 0.3

    def make_noise(self, sig):
        for i in range(sig.dft_samples):
            sig.y_dft[i] += self.scale*(self.sigma*np.random.randn() + self.mu)
