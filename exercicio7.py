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


# -----------------------------
# Normalização
# -----------------------------
def normalizacao(s):
    return gamma(s + 1) / (2 * np.sqrt(np.pi) * gamma(s + 0.5))


# -----------------------------
# Espalhamento direcional
# -----------------------------
def espalhamento(theta, s, theta0):
    A = normalizacao(s)
    D = A * np.cos((theta - theta0) / 2)**(2*s)
    return D


# -----------------------------
# Dados
# -----------------------------
theta = np.linspace(0, 2*np.pi, 1000)

theta0 = 0
valores_s = [1, 4, 10, 25]

# -----------------------------
# JONSWAP
# -----------------------------
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


# -----------------------------
# Gráficos
# -----------------------------
fig, axes = plt.subplots(
    2, 2,
    figsize=(10, 9),
    subplot_kw={'projection': 'polar'}
)

for ax, s in zip(axes.flat, valores_s):

    D = espalhamento(theta, s, theta0)

    # E(f, theta) = E(f) D(theta)
    E_direcional = E_fp * D

    ax.plot(theta, E_direcional, linewidth=2)

    ax.set_title(
        f'$s = {s}$',
        fontsize=13,
        pad=15
    )

    # mesma escala para todos os gráficos
    ax.set_ylim(0, E_fp)

    # direção média
    ax.plot(
        [theta0, theta0],
        [0, E_fp],
        linestyle='--',
        linewidth=1
    )

    ax.grid(True, alpha=0.4)


fig.suptitle(
    f'Espalhamento direcional de $E(f,\\theta)$ para $f_p = {fp:.3f}$ Hz',
    fontsize=15
)

plt.tight_layout()
plt.show()