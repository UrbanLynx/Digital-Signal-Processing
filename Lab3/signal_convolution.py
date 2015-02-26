from pylab import *
from digital_signals import *
from numpy import fft

def main():
    imp_sig = ImpulseSignal()
    make_signal(imp_sig)

    gaus_sig = GaussianSignal()
    make_signal(gaus_sig)

    conv_sig_a = (imp_sig, imp_sig, make_convolution(imp_sig,imp_sig))
    conv_sig_b = (imp_sig, gaus_sig, make_convolution(imp_sig,gaus_sig))
    conv_sig_c = (gaus_sig, gaus_sig, make_convolution(gaus_sig,gaus_sig))

    plot_signals((conv_sig_a,conv_sig_b, conv_sig_c))


def make_signal(sig):
    signal_vectorized = vectorize(sig.signal)
    sig.x_dft = linspace(-sig.global_limit, sig.global_limit, sig.dft_samples)
    sig.y_dft = signal_vectorized(sig.x_dft)
    sig.f_fft = fft.fft(sig.y_dft)


def make_convolution(sig_a, sig_b):
    conv_sig = DigitalSignal()
    conv_sig.f_fft = sig_a.f_fft*sig_b.f_fft
    conv_sig.y_dft = fft.fftshift(fft.ifft(conv_sig.f_fft))*conv_sig.dt/2
    conv_sig.x_dft = sig_a.x_dft
    return conv_sig


# old version with in built convolution
# def make_convolution(sig_a, sig_b):
#     conv_sig = DigitalSignal()
#     conv_sig.y_dft = convolve(sig_a.y_dft, sig_b.y_dft)*conv_sig.dt/2
#     conv_sig.x_dft = linspace(-conv_sig.global_limit*2,conv_sig.global_limit*2,conv_sig.dft_samples*2-1)
#     return conv_sig


def plot_signals(signal_tuples):
    num = len(signal_tuples)

    fig, axes = plt.subplots(num)
    for n,sg in enumerate(signal_tuples):
        axes[n].set_title('{0} and {1}'.format(sg[0].title, sg[1].title))
        axes[n].plot(sg[0].x_dft, sg[0].y_dft, 'r', label=sg[0].title)
        axes[n].plot(sg[1].x_dft, sg[1].y_dft, 'g', label=sg[1].title)
        axes[n].plot(sg[2].x_dft, sg[2].y_dft, 'b', label='Convolution')

    for axis in axes:
        axis.margins(0.05)
        axis.axis('tight')
        axis.grid(True)
        axis.legend(loc=0)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()