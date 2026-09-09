# Função que resolve (3) por iteração, com critério de
# parada por tolerância. Gerar a Figura 4 e verificar os limites assintóticos.

import math
import numpy as np
import matplotlib.pyplot as plt

T = 10
d_values = [5, 20, 100, 1000]
g = 9.81

def comprimento_de_onda(T, d):

    L0 = g*(T**2)/(2*math.pi)
    L = L0

    for i in range(100):
        k = 2 * math.pi / L
        L_novo = (g*(T**2)) / (2*math.pi) * math.tanh(k*d)

        L = L_novo
    return L_novo

# Graficos
T_values = np.linspace(2, 20, 150)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))


# Graf 1 - velocidade de fase:
for d in d_values:
    L_values = np.array([
        comprimento_de_onda(T, d) for T in T_values
    ])

    c_values = L_values / T_values
    axes[0].plot(T_values, c_values, label=f'd = {d} m')

axes[0].set_xlabel("Período T (s)")
axes[0].set_ylabel("c (m/s)")
axes[0].legend()
axes[0].grid()


#Graf 2 - comprimento de onda
for d in d_values:
    L_values = np.array([
        comprimento_de_onda(T, d) for T in T_values
    ])

    axes[1].plot(T_values, L_values)

axes[1].set_xlabel("Período T (s)")
axes[1].set_ylabel("L(m)")
axes[1].legend()
axes[1].grid()

plt.show()