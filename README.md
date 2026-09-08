# Ondas em Água e Espectro de Ondas

Repositório com as implementações em Python dos exercícios propostos na Seção 16 do material **"Ondas em água e espectro de ondas"**.

## 📋 Sobre o projeto

Este projeto reúne os códigos desenvolvidos para os exercícios relacionados à análise e simulação de ondas, incluindo relações de dispersão, grupos de ondas, espectros de energia e síntese de séries temporais.

## ⚙️ Requisitos

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/thayline07/ondas-e-espectro-.git
cd ondas-e-espectro-
```

Instale as dependências:

```bash
pip install numpy matplotlib scipy
```
## ▶️ Como executar

Cada exercício possui seu próprio arquivo Python.
Exemplo:
```bash
python exercicio1.py
```

Consulte a seção correspondente abaixo para saber o objetivo de cada exercício e como executá-lo.

## 📚 Exercícios
### Exercício 1 — Relação de dispersão

#### Objetivo

Implementar uma função que determine o comprimento de onda \(L\) a partir do período \(T\) e da profundidade \(d\), resolvendo numericamente a relação de dispersão.

Também são analisados diferentes valores de profundidade para verificar o comportamento do comprimento de onda e da velocidade de fase, reproduzindo a Figura 4 do material.

#### Como funciona

A função `comprimento_de_onda(T, d)` começa com uma estimativa inicial para o comprimento de onda e, por meio de iterações, atualiza esse valor utilizando a relação de dispersão.

A cada iteração, o número de onda é calculado por

$$ 
k = \frac{2\pi}{L} 
$$

e um novo valor de \(L\) é obtido a partir de

$$ 
L = \frac{gT^2}{2\pi}\tanh(kd). 
$$

Depois de determinar \(L\), a velocidade de fase é calculada por

$$
c = \frac{L}{T}.
$$

Por fim, o programa calcula esses valores para diferentes períodos e profundidades e gera os gráficos de \(c\) e \(L\) em função de \(T\).

---

### Exercício 2 — Onda simples

Descrição do exercício e instruções de execução.

---

### Exercício 3 — Grupos de ondas

#### Objetivo

Reproduzir a Figura 6 em Python utilizando duas ondas com $T_1=8s$ e $T_2=9s$. Em seguida, analisar o comportamento dos grupos de ondas alterando $T_2$ para $8,2s$ e $10s$.

Antes de executar cada caso, deve ser calculado o período de batimento $T_{bat}$ e utilizada essa informação para prever a quantidade de ondas em cada grupo.

#### Como funciona

O programa calcula a frequência angular de cada onda a partir do seu período:

$$
\omega = \frac{2\pi}{T}. 
$$

As ondas são então representadas por funções cossenoidais:

$$
\eta(t)=\cos(\omega t)
$$

e somadas para observar a formação dos grupos:

$$
\eta_{\mathrm{soma}}=\eta_1+\eta_2.
$$

A envoltória do grupo também é calculada e apresentada no gráfico por meio de curvas tracejadas. A comparação entre os diferentes valores de \(T_2\) permite observar como a diferença entre os períodos das ondas altera o período de batimento e, consequentemente, o tamanho dos grupos.

### Exercício 4 — Espectro JONSWAP

Descrição do exercício e instruções de execução.

### Exercício 5 — Momentos espectrais

Descrição do exercício e instruções de execução.

### Exercício 6 — Síntese e análise de ondas

Descrição do exercício e instruções de execução.

### Exercício 7 — Espalhamento direcional

Descrição do exercício e instruções de execução.

### Exercício 8 — Espectro bimodal

Descrição do exercício e instruções de execução.

## 👩‍💻 Autoria

Projeto desenvolvido como parte das atividades de Iniciação Científica.
