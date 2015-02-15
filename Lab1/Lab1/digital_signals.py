import math


class DigitalSignal:
    """
    Class represents settings for discretization of a signal

    x_ideal, y_ideal - points for ideal signal
    ideal_samples - number of points in ideal signal
    x_recon, y_recon - points for reconstructed signal
    recon_samples - number of points in reconstructed signal
    dt - distance between points in reconstructed signal
    global_limit - left and right limits of the signal on plot
    title - title of plot
    k_limit - number of points of ideal signal considered during reconstructing of one point of reconstructed signal
    """

    x_ideal, y_ideal = None, None
    ideal_samples = 1000
    x_recon, y_recon = None, None
    recon_samples = 500
    dt = 0.01
    global_limit = recon_samples * dt/2
    title = 'signal'
    k_limit = 1000


class ImpulseSignal(DigitalSignal):
    """
    impulse_limit - left and right boundaries of an impulse signal
    amplitude - amplitude of a signal
    """

    impulse_limit = 1
    amplitude = 1

    def __init__(self):
        self.title = 'Impulse signal'

    def signal(self, x):
        return self.amplitude if -self.impulse_limit <= x <= self.impulse_limit else 0


class GaussianSignal(DigitalSignal):
    """
    sigma - standard deviation of a signal
    amplitude - amplitude of a signal
    """

    sigma = 0.7
    amplitude = 1

    def __init__(self):
        self.title = 'Gaussian signal'

    def signal(self, x):
        return self.amplitude*math.exp(-x**2/self.sigma**2)
