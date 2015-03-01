from pylab import *


class DigitalFilter:

    def filter_signal(self, n_samples, dt):
        H = zeros(n_samples)
        for k in range(n_samples):
            f = k / dt / n_samples if k < n_samples / 2 else (n_samples - k) / dt / n_samples
            H[k] = self.filter_func(f,dt)
        return H


class ButterworthLowIir(DigitalFilter):
    border = 1
    title = 'Butterworth Low IIR'

    def filter_func(self, f, dt):
        return math.sqrt(1 / (1 + (math.sin(math.pi * f * dt) / math.sin(math.pi * self.border * dt)) ** 4))


class ButterworthLowFir(DigitalFilter):
    border = 1.4
    n = 2
    title = 'Butterworth Low FIR'

    def filter_func(self, f, dt):
        return 1 / (1 + (f / self.border) ** (2 * self.n))


class GaussianLowFir(DigitalFilter):
    sigma = 3
    title = 'Gaussian Low FIR'

    def filter_func(self, f, dt):
        return math.exp(-f ** 2 / (2*self.sigma ** 2))


class ButterworthHighIir(DigitalFilter):
    border = 1
    title = 'Butterworth High IIR'

    def filter_func(self, f, dt):
        return math.sqrt(1/(1 + (math.sin(math.pi*f*dt + math.pi/2)/math.sin(math.pi*self.border * dt))**4))


class ButterworthHighFir(DigitalFilter):
    border = 1.4
    n = 2
    title = 'Butterworth High FIR'

    def filter_func(self, f, dt):
        return 1 / (1 + (self.border / f) ** (2 * self.n)) if f != 0 else 0


class GaussianHighFir(DigitalFilter):
    sigma = 3
    title = 'Gaussian High FIR'

    def filter_func(self, f, dt):
        return 1 - math.exp(-f ** 2 / (2*self.sigma ** 2))