from pylab import *


class ButterworthLowIir:
    border = 1
    title = 'Butterworth Low IIR'

    def filter_signal(self, n_samples, dt):
        H = zeros(n_samples)
        for k in range(n_samples):
            f = k / dt / n_samples if k < n_samples / 2 else (n_samples - k) / dt / n_samples
            H[k] = math.sqrt(1 / (1 + (math.sin(math.pi * f * dt) / math.sin(math.pi * self.border * dt)) ** 4))
        return H

class ButterworthLowFir:
    border = 1.4
    n = 2
    title = 'Butterworth Low FIR'

    def filter_signal(self, n_samples, dt):
        H = zeros(n_samples)
        for k in range(n_samples):
            f = k / dt / n_samples if k < n_samples / 2 else (n_samples - k) / dt / n_samples
            H[k] = 1 / (1 + (f / self.border) ** (2 * self.n))
        return H


class GaussianLowFir:
    sigma = 3
    title = 'Gaussian Low FIR'

    def filter_signal(self, n_samples, dt):
        H = zeros(n_samples)
        for k in range(n_samples):
            f = k / dt / n_samples if k < n_samples / 2 else (n_samples - k) / dt / n_samples
            H[k] = math.exp(-f ** 2 / self.sigma ** 2)
        return H