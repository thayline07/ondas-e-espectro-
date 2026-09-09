import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros da onda
A = 1
T = 8
L = 100

# Frequência angular e número de onda
omega = 2*np.pi/T
k = 2*np.pi/L

# Velocidade da onda
c = omega/k

print("Velocidade da onda:", c, "m/s")

# Eixo x
x = np.linspace(0, 1000, 1000)

# Função da onda
def onda(x, t):
    return A*np.cos(k*x - omega*t)

# Criação da figura
fig, ax = plt.subplots(figsize=(10, 4))

linha, = ax.plot(x, onda(x, 0))

ax.set_xlim(0, 1000)
ax.set_ylim(-1.2, 1.2)

ax.set_xlabel("x (m)")
ax.set_ylabel("η(x,t)")

ax.grid()

# Função que atualiza a onda
def atualizar(t):
    linha.set_ydata(onda(x, t))
    ax.set_title(f"Onda simples — t = {t:.1f} s")
    return linha,

# Criação da animação
animacao = FuncAnimation(
    fig,
    atualizar,
    frames=np.linspace(0, 80, 200),
    interval=400
)

plt.show()