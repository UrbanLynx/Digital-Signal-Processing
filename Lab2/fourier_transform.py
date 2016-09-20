from pylab import *
from digital_signals import *
from cmath import exp, pi

def main():
    imp_sig = ImpulseSignal()
    make_fourier_transform(imp_sig)

    gaus_sig = GaussianSignal()
    make_fourier_transform(gaus_sig)

    plot_signal((imp_sig,gaus_sig))


def make_fourier_transform(sig):
    """
    make fourie transform of a signal

    sig - signal
    """
    signal_vectorized = vectorize(sig.signal)

    sig.x_ideal = linspace(-sig.global_limit, sig.global_limit, sig.ideal_samples)
    sig.y_ideal = signal_vectorized(sig.x_ideal)

    sig.x_dft = linspace(-sig.global_limit, sig.global_limit, sig.dft_samples)
    sig.y_dft = signal_vectorized(sig.x_dft)
    sig.y_dft_twin = remove_twin(sig)

    sig.w_dft = linspace(0, 1.0/(2.0*sig.dt), sig.dft_samples)
    sig.f_dft = abs(array(compute_dft(sig.y_dft)))
    sig.f_dft_twin = abs(array(compute_dft(sig.y_dft_twin)))

    sig.f_fft = abs(fftpack.fft(sig.y_dft))
    sig.f_fft_twin = abs(fftpack.fft(sig.y_dft_twin))


def remove_twin(sig):
    """
    transform samples to remove twin effect on signal specter

    sig - signal
    """
    result = []
    for i in range(sig.dft_samples):
        result.append(sig.y_dft[i]*((-1+0j)**i))
    return array(result)


def compute_dft(y_data):
    """
    compute Discrete Fourier Transform

    y_data - samples of a signal
    """
    n = len(y_data)
    output = [complex(0)] * n
    for k in range(n):  # For each output element
        s = complex(0)
        for t in range(n):  # For each y_data element
            s += y_data[t] * exp(-2j * pi * t * k / n)
        output[k] = s
    return output


def plot_signal(signals):
    """
    Plots signals

    signals - list of DigitalSignal objects for plotting
    """
    num = len(signals)

    fig, axes = plt.subplots(num, 3)
    for n,sg in enumerate(signals):
        axes[n,0].set_title(sg.title)
        axes[n,0].plot(sg.x_ideal, sg.y_ideal, 'r', label='Signal')

        axes[n,1].set_title('DFT and FFT')
        axes[n,1].plot(arange(0,sg.dft_samples), sg.f_dft, 'b', label='DFT')
        axes[n,1].plot(arange(0,sg.dft_samples), sg.f_fft, 'g', label='FFT')

        axes[n,2].set_title('DFT and FFT without twin effect')
        axes[n,2].plot(arange(0,sg.dft_samples), sg.f_dft_twin, 'b', label='DFT')
        axes[n,2].plot(arange(0,sg.dft_samples), sg.f_fft_twin, 'g', label='FFT')

        for axis in axes[n]:
            axis.margins(0.05)
            axis.axis('tight')
            axis.grid(True)
            axis.legend(loc=0);

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()