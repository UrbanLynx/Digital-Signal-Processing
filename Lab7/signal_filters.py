from pylab import *
from scipy import optimize as op
import cmath as cm


class TihonovFilter:
    title = 'Tihonov Filter'

    # def filter_signal(self, sig_org, sig_cor):
    #     alpha = self.calculate_alpha(sig_org, sig_cor)
    #     hs = [self.calculate_h(k,alpha[k],sig_org, sig_cor) for k in range(0,sig_org.dft_samples)]
    #     return hs

    def filter_signal(self, sig_org, sig_cor):
        alpha = self.calculate_alpha(sig_org, sig_cor)
        hs = [self.calculate_h(k,alpha,sig_org, sig_cor) for k in range(0,sig_org.dft_samples)]
        return hs

    def calculate_h(self, k, alpha, sig_org, sig_cor):
        dx = sig_org.dt
        N = sig_org.dft_samples
        T = N
        return dx/N * sum([(cm.exp(complex(0,2*math.pi*k*m/N)) * sig_cor.f_dft[m].conjugate() * sig_org.f_dft[m]) /
                           ((sig_cor.f_dft[m].real**2 * dx**2 + alpha*(1 + (2*math.pi*m/T)**2))**2) for m in range(0,N-1)])

    # def calculate_alpha(self, sig_org, sig_cor):
    #     alphas = [op.bisect(self.p,0,1,args=(sig_org, sig_cor, n)) for n in range(sig_org.dft_samples)]
    #     return alphas
    def calculate_alpha(self, sig_org, sig_cor):
        return op.bisect(self.p,0,1,args=(sig_org, sig_cor))

    # TODO: maybe remove sample_n from noise
    # def p(self,alpha,sig_org, sig_cor, sample_n):
    #     return self.beta(alpha,sig_org, sig_cor) - \
    #            (sig_cor.noise[sample_n] + sig_org.noise[sample_n]*math.sqrt(self.gamma(alpha,sig_org, sig_cor)))**2
    def p(self,alpha,sig_org, sig_cor):
        return self.beta(alpha,sig_org, sig_cor) - \
               (sig_cor.noise + sig_org.noise*math.sqrt(self.gamma(alpha,sig_org, sig_cor)))**2

    def beta(self,alpha,sig_org, sig_cor):
        dx = sig_org.dt
        N = sig_org.dft_samples
        T = N
        return dx/N * sum([(alpha**2 * (1+(2*math.pi*m/T)**2) * sig_org.f_dft[m].real**2)/
                           ((sig_cor.f_dft[m].real**2 * dx**2 + alpha*(1 + (2*math.pi*m/T)**2))**2) for m in range(0,N-1)])


    def gamma(self,alpha,sig_org, sig_cor):
        dx = sig_org.dt
        N = sig_org.dft_samples
        T = N
        return dx/N * sum([(sig_cor.f_dft[m].real**2 * dx**2 * sig_org.f_dft[m].real**2 * (1+(2*math.pi*m/T)**2)) /
                           ((sig_cor.f_dft[m].real**2 * dx**2 + alpha*(1 + (2*math.pi*m/T)**2))**2) for m in range(0,N-1)])

    # def find_root(self, func, left, right, *args):
    #     error = 0.001
    #     root = (right-left)/2
    #     y = func(root,*args)
    #     while y > error:
    #         root = (cur_root - prev_root)/2
    #         y = func(root,*args)
    #         if
    #
    #     return root

