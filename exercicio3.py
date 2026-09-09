# Além do que já foi pedido lá, medir numericamente a
# velocidade da envoltória e comparar com cg = dω/dk calculado por diferenças finitas.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

t = np.linspace(0, 320, 720)

T1 = 8
T2 = 10

freq_ang_1 = (2*np.pi)/T1
freq_ang_2 = (2*np.pi)/T2

n1 = np.cos(freq_ang_1*t)
n2 = np.cos(freq_ang_2*t)
n_soma = n1+n2

env_cima = 2*np.cos(((freq_ang_1-freq_ang_2)/2)*t)
env_baixo = -2*np.cos(((freq_ang_1-freq_ang_2)/2)*t)

fig, axs = plt.subplots(4, 1, figsize=(10, 8))

axs[0].plot(t, n1)
axs[0].set_ylabel("η1")
axs[0].set_yticks([])

axs[1].plot(t, n2)
axs[1].set_ylabel("η2")
axs[1].set_yticks([])

axs[2].plot(t, n_soma)
axs[2].plot(t, env_cima, linestyle='--', color='r')
axs[2].plot(t, env_baixo, linestyle='--', color='r')
axs[2].set_xlabel("Tempo (s)")
axs[2].set_ylabel("η1+η2")
axs[2].set_yticks([])

# Velocidade da envoltória e comparação com cg = dω/dk calculado por diferenças finitas. 

x = np.linspace(0, 1000, 1000)

L1 = 1.56*(T1**2)
L2 = 1.56*(T2**2)

k1 = (2*np.pi)/L1
k2 = (2*np.pi)/L2

tempo1 = 20
tempo2 = 40

envoltoria1 = 2*np.cos(((k1-k2)*x - (freq_ang_1-freq_ang_2)*tempo1)/2)
envoltoria2 = 2*np.cos(((k1-k2)*x - (freq_ang_1-freq_ang_2)*tempo2)/2)

picos1, _ = find_peaks(envoltoria1)
picos2, _ = find_peaks(envoltoria2)

x_picos1 = x[picos1]
x_picos2 = x[picos2]

cg_env = (x_picos2[0]-x_picos1[0])/(tempo2-tempo1)

print("Velocidade numérica da envoltória:", cg_env, "m/s")

# Calculando cg = dω/dk por diferenças finitas

k0 = (k1 + k2) / 2
g = 9.81

h = 0.0001

omega_k = np.sqrt(g * k0)
omega_kh = np.sqrt(g * (k0 + h))

cg_diferenca = (omega_kh - omega_k) / h

print("Cg por diferenças finitas:", cg_diferenca, "m/s")

axs[3].plot(x, envoltoria1, '--')
axs[3].plot(x, envoltoria2, '--')

axs[3].set_xlabel("x (m)")
axs[3].set_ylabel("η")
axs[3].set_yticks([])
axs[3].grid()

plt.show()
