from pylab import *
from digital_signals import *
from addaptive_noise import *


def main():
    gaus_sig1 = GaussianSignal()
    gaus_sig2 = GaussianSignal()

    imp_noise = ImpulseNoise()
    gaus_noise = GaussianNoise()

    for sig, noise in zip((gaus_sig1,gaus_sig2),(imp_noise,gaus_noise)):
        make_signal(sig)
        noise.make_noise(sig)
        make_fourier_transform(sig)

    plot_signal((gaus_sig1,gaus_sig2))


def make_signal(sig):
    signal_vectorized = vectorize(sig.signal)
    sig.x_dft = linspace(-sig.global_limit, sig.global_limit, sig.dft_samples)
    sig.y_dft = signal_vectorized(sig.x_dft)


def make_fourier_transform(sig):
    sig.w_dft = linspace(0, 1.0/(2.0*sig.dt), sig.dft_samples)
    sig.f_dft = fftpack.fft(sig.y_dft)


def plot_signal(signals):
    num = len(signals)

    fig, axes = plt.subplots(num, 2)
    for n,sg in enumerate(signals):
        axes[n,0].set_title(sg.title)
        axes[n,0].plot(sg.x_dft, sg.y_dft, 'r', label='Signal')

        axes[n,1].set_title('DFT')
        axes[n,1].plot(arange(0,sg.dft_samples), sg.f_dft, 'b', label='DFT')

        for axis in axes[n]:
            axis.margins(0.05)
            axis.axis('tight')
            axis.grid(True)
            axis.legend(loc=0);

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()