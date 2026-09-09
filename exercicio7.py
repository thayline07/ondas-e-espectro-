import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma


def jonswap_normalizado(f, Hs_desejado, Tp, gamma):
    g = 9.81
    fp = 1.0 / Tp

    sigma_j = np.where(f <= fp, 0.07, 0.09)

    alpha_temp = 1.0
    # espectro
    E_pm = alpha_temp*((g**2)/(((2*np.pi)**4)*f**5))*np.exp((-5/4)*((fp/f)**4))
    r = np.exp(-((f-fp)**2)/(2*(sigma_j**2)*(fp**2)))
    E_temp = E_pm*(gamma**r)

    m0_inicial = np.trapezoid(E_temp, x=f)

    m0_alvo = (Hs_desejado / 4.0) ** 2

    E_normalizado = E_temp * (m0_alvo / m0_inicial)

    return E_normalizado


def normalizacao(s):
    return gamma(s + 1) / (2 * np.sqrt(np.pi) * gamma(s + 0.5))


def espalhamento(theta, s, theta0):
    A = normalizacao(s)
    D = A * np.cos((theta - theta0) / 2)**(2*s)
    return D



theta = np.linspace(0, 2*np.pi, 1000)

theta0 = 0
valores_s = [1, 4, 10, 25]


f = np.linspace(0.02, 0.30, 200)

Hs = 2.5
Tp = 10
gamma_j = 3.3

E = jonswap_normalizado(f, Hs, Tp, gamma_j)

# frequência de pico
indice_pico = np.argmax(E)
fp = f[indice_pico]

# valor do espectro na frequência de pico
E_fp = E[indice_pico]


# frequência de pico
indice_pico = np.argmax(E)
fp = f[indice_pico]
E_fp = E[indice_pico]

# intervalo angular
theta = np.linspace(-np.pi/2, np.pi/2, 500)

# espalhamento
s = 4
theta0 = 0

D = espalhamento(theta, s, theta0)

# espectro direcional
E_direcional = E_fp * D

# gráfico
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(theta, E_direcional, linewidth=2)

ax.set_title(f'E(f, θ) para f = {fp:.3f} Hz')

plt.show()