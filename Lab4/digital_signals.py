import math


class DigitalSignal:
    """
    Class represents settings for discretization of a signal

    x_dft, y_dft - samples of signal
    w_dft, f_dft - frequency, DFT points
    dft_samples - number of samples taken
    dt - distance between points in reconstructed signal
    global_limit - left and right limits of the signal on plot
    title - title of plot
    """

    x_dft, y_dft = None, None
    w_dft, f_dft = None, None
    dft_samples = 100
    dt = 0.1

    global_limit = dft_samples * dt/2
    title = 'signal'


class ImpulseSignal(DigitalSignal):
    """
    impulse_limit - left and right boundaries of an impulse signal
    amplitude - amplitude of a signal
    """

    impulse_left_limit = -1
    impulse_right_limit = 1
    amplitude = 1

    def __init__(self):
        self.title = 'Impulse signal'

    def signal(self, x):
        return self.amplitude if self.impulse_left_limit <= x <= self.impulse_right_limit else 0


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
