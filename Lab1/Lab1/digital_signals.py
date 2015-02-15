import math


class DigitalSignal:
    x_sample, y_sample = None, None
    x_recon, y_recon = None, None
    dt = 0.01
    num_samples = 500
    global_limit = num_samples * dt/2
    title = 'signal'
    k_limit = 1000
    ideal_samples = 1000


class ImpulseSignal(DigitalSignal):
    impulse_limit = 1
    amplitude = 1

    def __init__(self):
        self.title = 'Impulse signal'

    def signal(self, x):
        return self.amplitude if -self.impulse_limit <= x <= self.impulse_limit else 0


class GaussianSignal(DigitalSignal):
    sigma = 0.7
    amplitude = 1

    def __init__(self):
        self.title = 'Gaussian signal'

    def signal(self, x):
        return self.amplitude*math.exp(-x**2/self.sigma**2)
