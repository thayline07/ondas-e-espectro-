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
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

Instale as dependências:

```bash
pip install numpy matplotlib scipy
```
## ▶️ Como executar

Cada exercício possui seu próprio arquivo Python.
Exemplo:
´´´bash
python exercicio1.py
´´´

Consulte a seção correspondente abaixo para saber o objetivo de cada exercício e como executá-lo.

## 📚 Exercícios
### Exercício 1 — Relação de dispersão
#### Objetivo

Reproduzir a Figura 6 do material em Python utilizando duas ondas com períodos
`T1 = 8 s` e `T2 = 9 s`.

Em seguida, o período `T2` deve ser alterado para `8,2 s` e `10 s`,
comparando o comportamento dos grupos de ondas em cada caso.

#### Como funciona

O código calcula a frequência angular de cada onda a partir de:

\[
\omega = \frac{2\pi}{T}
\]

e gera as ondas utilizando:

\[
\eta(t) = \cos(\omega t)
\]

As ondas são então somadas para observar a formação dos grupos:

\[
\eta_{\text{soma}} = \eta_1 + \eta_2
\]

Também é calculada a envoltória do grupo, representada pelas curvas
tracejadas no gráfico.

#### Período de batimento

Antes de executar cada caso, deve ser calculado o período de batimento
`Tbat` pela equação (11) do material:

\[
T_{bat} = \frac{1}{|f_1-f_2|}
\]

A partir de `Tbat`, é possível estimar quantas ondas individuais existem
aproximadamente em cada grupo.

Os três casos analisados são:

- `T1 = 8 s` e `T2 = 9 s`
- `T1 = 8 s` e `T2 = 8,2 s`
- `T1 = 8 s` e `T2 = 10 s`

O último caso exige uma alteração na janela de tempo do gráfico para que
os grupos possam ser visualizados adequadamente.

#### Execução

Execute o arquivo correspondente ao exercício:

```bash
python exercicio1.py

### Exercício 2 — Onda simples

Descrição do exercício e instruções de execução.

### Exercício 3 — Grupos de ondas

Descrição do exercício e instruções de execução.

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
