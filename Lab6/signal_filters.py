from pylab import *


class WinnerFilter:
    title = 'Winner Filter'

    def filter_signal(self, sig, noise):
        noise.make_fourier_transform()
        H = (sig.f_dft**2 - noise.f_noise**2) / (sig.f_dft**2)
        return H
