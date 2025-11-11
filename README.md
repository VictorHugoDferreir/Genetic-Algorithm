# Genetic-Algorithm

## 🚀 Algoritmo Genético para Maximização da Função $F(6)$

Este projeto implementa um Algoritmo Genético (AG) em Python para encontrar o máximo global da complexa função real $F_6$. O AG foi cuidadosamente configurado com técnicas clássicas e eficientes para garantir uma convergência robusta e resultados precisos.

### 🎯 Objetivo

O principal objetivo deste algoritmo genético é **maximizar** o valor da função de avaliação $F_6(x, y)$:

$$
F_6(x,y) = 0.5 - \frac{(\sin \sqrt{x^2 + y^2})^2 - 0.5}{(1.0 + 0.001 (x^2 + y^2))^2}
$$

### ⚙️ Configuração do Algoritmo Genético

O AG foi estruturado em módulos claros de População, Avaliação e Reprodução, com as seguintes especificações:

#### 1. Módulo de População

| Parâmetro | Técnica/Valor | Detalhes |
| :--- | :--- | :--- |
| **Tamanho da População** | $100$ | Número de indivíduos (cromossomos) em cada geração. |
| **Técnica de Representação** | Binária $44$ bits | Cada indivíduo é representado por um vetor binário de $44$ bits, o qual é decodificado para obter os valores de $x$ e $y$. |
| **Inicialização** | Aleatória | A população inicial é gerada aleatoriamente. |
| **Técnica de Aptidão** | A aptidão é a avaliação ($F_6$) | O valor retornado pela função $F_6$ é diretamente a medida de aptidão do indivíduo (maximização). |
| **Técnica de Seleção de Genitores** | Roleta | Os indivíduos mais aptos têm maior probabilidade de serem selecionados para a reprodução. |
| **Técnica de Eliminação** | Elimina todos – o mais apto (Elitismo) | Apenas o indivíduo **mais apto** (Elite) da geração anterior é garantido para passar para a próxima geração, preservando o melhor progresso. |

#### 2. Módulo de Reprodução (Operadores)

| Operador | Taxa/Técnica | Descrição |
| :--- | :--- | :--- |
| **Crossover** | $0.65$ (Taxa de Crossover) | Aplicado Crossover de **1 Ponto** para trocar material genético entre os genitores selecionados. |
| **Mutação** | $0.008$ (Taxa de Mutação) | Pequena probabilidade de inversão de um bit no cromossomo, essencial para introduzir diversidade e evitar mínimos locais. |

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal de desenvolvimento.

### 📈 Resultados Esperados

Ao final da execução, espera-se que o algoritmo tenha convergido para um indivíduo cuja avaliação $F_6(x, y)$ esteja próxima do máximo global teórico da função.

* **Output:** O programa deve exibir o indivíduo de maior aptidão (Elite) encontrado a cada geração, incluindo seus valores decodificados de $x$ e $y$, e o valor de $F_6$ alcançado.

