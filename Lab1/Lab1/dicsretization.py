from pylab import *
from digital_signals import *

def main():
    imp_sig = ImpulseSignal()
    discretize_signal(imp_sig)

    gaus_sig = GaussianSignal()
    discretize_signal(gaus_sig)

    plot_signal((imp_sig,gaus_sig))


def discretize_signal(sig):
    """
    Calculate ideal and reconstructed signals

    sig - DigitalSignal object
    """
    signal_vectorized = vectorize(sig.signal)
    kotelnikov_vectorized = vectorize(kotelnikov)

    sig.x_sample = linspace(-sig.global_limit, sig.global_limit, sig.ideal_samples)
    sig.y_sample = signal_vectorized(sig.x_sample)

    sig.x_recon = linspace(-sig.global_limit, sig.global_limit, sig.recon_samples)
    sig.y_recon = kotelnikov_vectorized(sig,sig.x_recon)


def kotelnikov(sig, t):
    """
    Reconstruct Y for argument t and signal sig

    sig - DigitalSignal object
    """
    return sum([sig.signal(k*sig.dt) * my_sinc(math.pi/sig.dt*(t-k*sig.dt))
                for k in range(-sig.k_limit, sig.k_limit, 1)])


def my_sinc(x):
    return math.sin(x) / x if x != 0 else 1.0


def plot_signal(signals):
    """
    Plots signals

    signals - list of DigitalSignal objects for plotting
    """
    num = len(signals)
    fig, axes = plt.subplots(1, num)
    for axis, sg in zip(axes, signals):
        axis.margins(0.05)
        axis.plot(sg.x_sample, sg.y_sample, 'r', lw=2)
        axis.plot(sg.x_recon, sg.y_recon, 'g', marker='o', markersize=4)
        axis.axis('tight')
        axis.grid(True)
        axis.set_title(sg.title)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()