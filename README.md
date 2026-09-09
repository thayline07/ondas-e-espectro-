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

Implementar uma função que determine o comprimento de onda $L$ a partir do período $T$ e da profundidade $d$, resolvendo numericamente a relação de dispersão.

Também são analisados diferentes valores de profundidade para verificar o comportamento do comprimento de onda e da velocidade de fase, reproduzindo a Figura 4 do material.

#### Como funciona

A função `comprimento_de_onda(T, d)` começa com uma estimativa inicial para o comprimento de onda e, por meio de iterações, atualiza esse valor utilizando a relação de dispersão.

A cada iteração, o número de onda é calculado por

$$ 
k = \frac{2\pi}{L} 
$$

e um novo valor de $L$ é obtido a partir de

$$ 
L = \frac{gT^2}{2\pi}\tanh(kd). 
$$

Depois de determinar $L$, a velocidade de fase é calculada por

$$
c = \frac{L}{T}.
$$

Por fim, o programa calcula esses valores para diferentes períodos e profundidades e gera os gráficos de $c$ e $L$ em função de $T$.

---

### Exercício 2 — Onda simples

#### Objetivo

Visualizar a propagação de uma onda simples e verificar que sua velocidade de propagação é dada por $c=\omega/k$.

#### Como funciona

O código define uma onda a partir de sua amplitude, período e comprimento de onda. Em seguida, utiliza **FuncAnimation** para atualizar a onda para diferentes valores de tempo, criando uma animação que permite observar seu deslocamento ao longo do eixo $x$. A velocidade teórica é calculada por $c=\omega/k$ e comparada com o deslocamento observado na animação.

---

### Exercício 3 — Grupos de ondas

#### Objetivo

Reproduzir a Figura 6 em Python utilizando duas ondas com $T_1=8s$ e $T_2=9s$. Em seguida, analisar o comportamento dos grupos de ondas alterando $T_2$ para $8,2s$ e $10s$.

Antes de executar cada caso, deve ser calculado o período de batimento $T_{bat}$ e utilizada essa informação para prever a quantidade de ondas em cada grupo.

Além disso, medir numericamente a velocidade de propagação da envoltória do grupo e compará-la com a velocidade de grupo $cg$, calculada por diferenças finitas.

#### Como funciona

O programa calcula a frequência angular de cada onda a partir do seu período:

$$
\omega = \frac{2\pi}{T}. 
$$

As ondas são então representadas por funções:

$$
\eta(t)=\cos(\omega t)
$$

e somadas para observar a formação dos grupos:

$$
\eta_{\mathrm{soma}}=\eta_1+\eta_2.
$$

A envoltória do grupo também é calculada e apresentada no gráfico por meio de curvas tracejadas. A comparação entre os diferentes valores de $T_2$ permite observar como a diferença entre os períodos das ondas altera o período de batimento e, consequentemente, o tamanho dos grupos.

Para determinar a velocidade da envoltória, são identificados numericamente os máximos da envoltória em dois instantes diferentes. A velocidade é então obtida pela razão entre a variação da posição do máximo e a variação do tempo:

$$ cg,num=(x2-x1)/(t2-t1). $$

Por fim, a velocidade de grupo é calculada por uma diferença finita da relação de dispersão:

$$ cg≈(\omega(k+h)-\omega(k))/h, $$

permitindo comparar o valor teórico com a velocidade medida diretamente no gráfico.

---

### Exercício 4 — Espectro JONSWAP

### Objetivo

Implementar a fórmula (19) do espectro JONSWAP em Python, utilizando a normalização por $H_s$, e reproduzir a Figura 12. Em seguida, verificar numericamente se $4\sqrt{m_0}$ retorna o valor de $H_s$ definido.

### Como funciona

O programa calcula o espectro JONSWAP para diferentes valores de $\gamma$ e $T_p$, normalizando o espectro para o $H_s$ desejado. Os resultados são apresentados em dois gráficos, permitindo observar a influência desses parâmetros no espectro.

Por fim, o momento espectral $m_0$ é calculado numericamente pela integração do espectro, e a altura significativa é obtida por:

$$ H_s=4√m_0. $$

O valor calculado é então comparado com o $H_s$ utilizado na normalização.

---

### Exercício 5 — Momentos espectrais

#### Objetivo

Implementar uma função para calcular os principais momentos espectrais de um espectro JONSWAP e obter os parâmetros $H_s$, $T_p$, $T_{m01}$ e $T_{m02}$.

#### Como funciona

A função recebe o vetor de frequências $f$ e os valores do espectro $E$, calculando numericamente $m_0$, $m_1$ e $m_2$ por integração pelo método dos trapézios. A partir desses momentos, são calculados os parâmetros do estado do mar.

Por fim, a função é testada utilizando um espectro JONSWAP com $H_s$ e $T_p$ conhecidos, verificando se os valores calculados correspondem aos utilizados na construção do espectro.

---

### Exercício 6 — Síntese e análise de ondas

#### Objetivo

Gerar um sinal de elevação da superfície $\eta(t)$ a partir de um espectro JONSWAP com fases aleatórias e, em seguida, estimar novamente o espectro a partir do sinal utilizando o método de Welch.

#### Como funciona

O programa utiliza um espectro JONSWAP e gera um sinal no domínio do tempo por meio da superposição de várias componentes senoidais com fases aleatórias. A partir desse sinal, o espectro é estimado novamente utilizando *scipy.signal.welch*.

Por fim, o espectro estimado é comparado com o espectro JONSWAP original, permitindo verificar se as características espectrais são preservadas durante o processo de síntese e análise. Este exercício completa o ciclo entre o espectro e o sinal no domínio do tempo.

---

### Exercício 7 — Espalhamento direcional

#### Objetivo

Implementar a equação (21) para representar o espalhamento direcional das ondas e gerar o espectro direcional $E(f,\theta)$.

#### Como funciona

O programa calcula a função de espalhamento direcional

$$ D(\theta)=A(s)\cos^{2s}\left(\frac{\theta-\theta_0}{2}\right), $$

utilizando a normalização adequada para que

$$ \int_0^{2\pi}D(\theta)\,d\theta=1. $$

A partir dela, o espectro direcional é obtido por

$$ E(f,\theta)=E(f)D(\theta), $$

distribuindo a energia do espectro JONSWAP de acordo com a direção de propagação. O gráfico polar é utilizado para visualizar como a energia se concentra em torno da direção média $\theta_0$, de acordo com o parâmetro de espalhamento $s$.

Por fim, a normalização é verificada numericamente, confirmando que a integração de $D(\theta)$ em todas as direções resulta em aproximadamente 1.

### Exercício 8 — Espectro bimodal

Descrição do exercício e instruções de execução.

## 👩‍💻 Autoria

Projeto desenvolvido como parte das atividades de Iniciação Científica.
