import numpy as np

def momentos(f, E):
    m0 = np.trapezoid(E, x=f)
    m1 = np.trapezoid(f * E, x=f)
    m2 = np.trapezoid(f**2 * E, x=f)

    Hs = 4 * np.sqrt(m0)

    fp = f[np.argmax(E)]
    Tp = 1 / fp

    Tm01 = m0 / m1
    Tm02 = np.sqrt(m0 / m2)

    return m0, m1, m2, Hs, Tp, Tm01, Tm02


def jonswap_normalizado(f, Hs_desejado, Tp, gamma):
    g = 9.81
    fp = 1 / Tp

    sigma = np.where(f <= fp, 0.07, 0.09)

    E_pm = ((g**2) / ((2*np.pi)**4 * f**5)) * \
           np.exp(-5/4 * (fp/f)**4)

    r = np.exp(-((f - fp)**2) / (2 * sigma**2 * fp**2))

    E = E_pm * gamma**r

    m0_inicial = np.trapezoid(E, x=f)
    m0_alvo = (Hs_desejado / 4)**2

    return E * (m0_alvo / m0_inicial)


# Dados
f = np.arange(0.01, 0.4001, 0.001)

Hs_desejado = 2.5
Tp_desejado = 10.0
gamma = 3.3

E = jonswap_normalizado(f, Hs_desejado, Tp_desejado, gamma)

m0, m1, m2, Hs, Tp, Tm01, Tm02 = momentos(f, E)


print(f"m0   = {m0:.4f} m²")
print(f"m1   = {m1:.4f} m²/Hz")
print(f"m2   = {m2:.4f} m²/Hz²")
print(f"Hs   = {Hs:.4f} m")
print(f"Tp   = {Tp:.4f} s")
print(f"Tm01 = {Tm01:.4f} s")
print(f"Tm02 = {Tm02:.4f} s")

print("\nValores esperados:")
print(f"Hs = {Hs_desejado} m")
print(f"Tp = {Tp_desejado} s")