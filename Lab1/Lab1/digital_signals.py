import math

class DigitalSignal:
    x_sample = None
    y_sample = None
    x_recon = None
    y_recon = None
    dt = 0.05
    num_samples = 100
    global_limit = num_samples * dt/2
    title = 'signal'
    k_limit = 100
    ideal_samples = 1000

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

    sigma = 0.7
    amplitude = 1

    def signal(self, x):
        return self.amplitude*math.exp(-x**2/self.sigma**2)
