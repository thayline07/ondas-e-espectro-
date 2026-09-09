#Implemente a fórmula (19) em Python, com a normalização por  Hs . Reproduza a Figura 12. Depois verifique numericamente que  4√m0  devolve exatamente o  Hs  que você pediu.

import numpy as np
import matplotlib.pyplot as plt

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

N = 200
f_grafico = np.linspace(0.01, 0.4, N)

# gráfico a
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)

gammas = [1.0, 2.0, 3.3, 7.0]
for g in gammas:
    E_a = jonswap_normalizado(f_grafico, 2.5, 10.0, g)
    plt.plot(f_grafico, E_a, label=f'γ = {g}')

plt.title("(a) variando γ (Hs = 2,5m, Tp = 10s)")
plt.xlabel('$f$ (Hz)')
plt.ylabel('$E(f)$ ($m^2$/Hz)')
plt.legend()


# gráfico b
plt.subplot(1, 2, 2)

periodos = [6.0, 8.0, 10.0, 14.0]
for tp in periodos:
    E_b = jonswap_normalizado(f_grafico, 2.5, tp, 3.3)
    plt.plot(f_grafico, E_b, label=f'Tp = {tp} s')

plt.title('(b) variando Tp (Hs = 2,5 m, γ = 3,3)')
plt.xlabel('$f$ (Hz)')
plt.ylabel('$E(f)$ ($m^2$/Hz)')
plt.legend()


# teste
Hs_pedido = 2.5
E_teste = jonswap_normalizado(f_grafico, Hs_pedido, 10.0, 3.3)

m0_final = np.trapezoid(E_teste, x=f_grafico)
Hs_calculado = 4 * np.sqrt(m0_final)

print(f"Hs pedido: {Hs_pedido} m")
print(f"Hs real: {Hs_calculado} m")
