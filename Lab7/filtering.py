from pylab import *
from digital_signals import *
from addaptive_noise import *
from signal_filters import *

number_of_signals = 2

def main():
    filter = TihonovFilter()

    sig_org = GaussianSignal(2)
    sig_org.make_signal()
    noise_org = ImpulseNoise(GaussianSignal.dft_samples)
    noise_org.make_noise(sig_org)
    #sig_org.noise = noise.y_noise

    sig_cor = GaussianSignal(1)
    sig_cor.make_signal()
    noise_cor = ImpulseNoise(GaussianSignal.dft_samples)
    noise_cor.make_noise(sig_cor)
    #sig_cor.noise = noise.y_noise

    sig_org.make_fourier_transform()
    sig_cor.make_fourier_transform()

    H = filter.filter_signal(sig_org,sig_cor)
    sig_cor.f_dft_filter = sig_cor.f_dft*H
    sig_cor.y_dft_filter = fftpack.ifft(sig_cor.f_dft_filter)

    plot_signal(sig_org, sig_cor, H)


def plot_signal(sig_org, sig_cor, h):
    fig, axes = plt.subplots(4,1)

    #axes.set_title(sg[2].title)
    axes[0].plot(sig_org.x_dft, sig_org.y_dft, 'g', lw=2, label='Original Signal')
    axes[1].plot(sig_cor.x_dft, sig_cor.y_dft, 'r',lw=2, label='Corrupted Signal')
    axes[2].plot(sig_cor.x_dft, sig_cor.y_dft_filter, 'b',lw=2, label='Filter Signal')
    axes[3].plot(sig_cor.x_dft, h, 'b',lw=2, label='H')

    for axis in axes.flat:
        axis.margins(0.05)
        axis.axis('tight')
        axis.grid(True)
        axis.legend(loc=0)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()