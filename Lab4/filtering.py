from pylab import *
from digital_signals import *
from addaptive_noise import *
from signal_filters import *


def main():
    systems_list = get_signal_systems()

    for component in systems_list:
        noise_filter_signal(component[0],component[1],component[2])

    plot_signal(systems_list)


def get_signal_systems():
    import itertools
    n = GaussianSignal.dft_samples
    sig_list = [GaussianSignal() for k in range(6)]
    noise_list = [ImpulseNoise(n),GaussianNoise(n)]
    filter_list = [ButterworthLowIir(), ButterworthLowFir(), GaussianLowFir()]
    systems_list = list(itertools.product(noise_list, filter_list))
    systems_list = zip(sig_list,zip(*systems_list)[0],zip(*systems_list)[1])

    return systems_list


def noise_filter_signal(sig, noise, sig_filter):
    sig.make_signal()
    noise.make_noise(sig)
    sig.make_fourier_transform()
    H = sig_filter.filter_signal(sig.dft_samples,sig.dt)
    sig.f_dft_filter = sig.f_dft*H
    sig.y_dft_filter = fftpack.ifft(sig.f_dft_filter)


def plot_signal(systems):
    num = len(systems)/2
    fig, axes = plt.subplots(2, num)

    for axis,sg in zip(axes.flat,systems):
        axis.set_title(sg[2].title)
        axis.plot(sg[0].x_dft, sg[0].y_dft, 'g', label='Signal')
        axis.plot(sg[0].x_dft, sg[0].y_dft_filter, 'r', lw=2, label='Filter')

        axis.margins(0.05)
        axis.axis('tight')
        axis.grid(True)
        axis.legend(loc=0)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()