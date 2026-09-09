import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma


def jonswap_normalizado(f, Hs_desejado, Tp, gamma):
    g = 9.81
    fp = 1.0 / Tp

    sigma_j = np.where(f <= fp, 0.07, 0.09)

    alpha_temp = 1.0

    E_pm = (
        alpha_temp
        * ((g**2) / (((2 * np.pi)**4) * f**5))
        * np.exp((-5 / 4) * ((fp / f)**4))
    )

    r = np.exp(
        -((f - fp)**2)
        / (2 * (sigma_j**2) * (fp**2))
    )

    E_temp = E_pm * (gamma**r)

    m0_inicial = np.trapezoid(E_temp, x=f)

    m0_alvo = (Hs_desejado / 4.0)**2

    E_normalizado = E_temp * (m0_alvo / m0_inicial)

    return E_normalizado


def normalizacao(s):
    return gamma(s + 1) / (
        2 * np.sqrt(np.pi) * gamma(s + 0.5)
    )


def espalhamento(theta, s, theta0):
    A = normalizacao(s)

    D = A * np.cos(
        (theta - theta0) / 2
    )**(2 * s)

    return D


f = np.linspace(0.02, 0.30, 200)

theta = np.linspace(0, 2 * np.pi, 360)

gamma_j = 3.3


Hs_marulho = 2.5
Tp_marulho = 14
s_marulho = 25

theta0_marulho = np.deg2rad(30)


Hs_vaga = 2.0
Tp_vaga = 5
s_vaga = 4

theta0_vaga = np.deg2rad(120)


E_marulho = jonswap_normalizado(
    f,
    Hs_marulho,
    Tp_marulho,
    gamma_j
)

E_vaga = jonswap_normalizado(
    f,
    Hs_vaga,
    Tp_vaga,
    gamma_j
)


D_marulho = espalhamento(
    theta,
    s_marulho,
    theta0_marulho
)

D_vaga = espalhamento(
    theta,
    s_vaga,
    theta0_vaga
)


E_marulho_direcional = np.zeros(
    (len(f), len(theta))
)

E_vaga_direcional = np.zeros(
    (len(f), len(theta))
)


for i in range(len(f)):

    E_marulho_direcional[i, :] = (
        E_marulho[i] * D_marulho
    )

    E_vaga_direcional[i, :] = (
        E_vaga[i] * D_vaga
    )


E_total = (
    E_marulho_direcional
    + E_vaga_direcional
)


E_total_f = (
    E_marulho
    + E_vaga
)


plt.figure(figsize=(8, 5))

plt.plot(
    f,
    E_total_f,
    label='total'
)

plt.plot(
    f,
    E_marulho,
    '--',
    label='marulho (swell)'
)

plt.plot(
    f,
    E_vaga,
    '-.',
    label='vaga (wind sea)'
)

plt.xlabel('f (Hz)')
plt.ylabel('E(f) (m²/Hz)')

plt.title('Espectro bimodal em frequência')

plt.legend()
plt.grid()

plt.show()


F, THETA = np.meshgrid(
    f,
    theta,
    indexing='ij'
)

fig, ax = plt.subplots(
    subplot_kw={'projection': 'polar'},
    figsize=(7, 7)
)

pcm = ax.pcolormesh(
    THETA,
    F,
    E_total,
    shading='auto'
)


ax.set_theta_zero_location('N')

ax.set_theta_direction(-1)

ax.set_title(
    'E(f, θ) bimodal',
    pad=20
)

plt.colorbar(
    pcm,
    ax=ax,
    label='E(f, θ)'
)

plt.show()