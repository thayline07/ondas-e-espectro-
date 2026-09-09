import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

N = 200
f = np.linspace(0.02, 0.30, N)

g = 9.81
alpha = 0.0081
fp = 0.1

gamma = 3.3
sigma_j = np.where(f <= fp, 0.07, 0.09)

# Espectro JONSWAP
E_pm = alpha * ((g**2) / (((2*np.pi)**4) * f**5)) * np.exp((-5/4) * ((fp/f)**4))

r = np.exp(-((f-fp)**2) / (2*(sigma_j**2)*(fp**2)))

E = E_pm * (gamma**r)

# Sinal
fases = np.random.uniform(0, 2*np.pi, N)

df = f[1] - f[0]

a = np.sqrt(2 * E * df)

t = np.arange(0, 900, 1.0)

eta = np.zeros_like(t)

for i in range(N):
    omega_i = 2 * np.pi * f[i]
    eta += a[i] * np.cos(omega_i * t + fases[i])


# Estimativa do espectro a partir de eta
dt = t[1] - t[0]
fs = 1 / dt

f_welch, E_welch = welch(eta, fs=fs)


# Gráfico
plt.figure(figsize=(8, 5))

plt.plot(f, E, label='JONSWAP original')
plt.plot(f_welch, E_welch, label='Espectro estimado - Welch')

plt.xlabel('Frequência (Hz)')
plt.ylabel('E(f) (m²/Hz)')
plt.title('Comparação entre espectros')
plt.xlim(0.02, 0.30)
plt.legend()
plt.grid()

plt.show()