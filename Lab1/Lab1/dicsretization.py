from pylab import *
from digital_signals import *

def main():
    imp_sig = ImpulseSignal()
    discretize_impulse(imp_sig)

    gaus_sig = GaussianSignal()
    discretize_impulse(gaus_sig)

    plot_signal((imp_sig,gaus_sig))


def discretize_impulse(sg):
    signal_vectorized = vectorize(sg.signal)
    kotelnikov_vectorized = vectorize(kotelnikov)

    sg.x_sample = linspace(-sg.global_limit, sg.global_limit, sg.ideal_samples)
    sg.y_sample = signal_vectorized(sg.x_sample)

    sg.x_recon = linspace(-sg.global_limit, sg.global_limit, sg.num_samples)
    sg.y_recon = kotelnikov_vectorized(sg,sg.x_recon)


def kotelnikov(sig, t):
    return sum([sig.signal(k*sig.dt) * my_sinc(math.pi/sig.dt*(t-k*sig.dt))
                for k in range(-sig.k_limit, sig.k_limit, 1)])


def my_sinc(x):
    return math.sin(x) / x if x != 0 else 1.0


def plot_signal(signals):
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