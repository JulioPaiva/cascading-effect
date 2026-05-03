# 🌪️ Cascading Effect — Simulação de Interações Sociais

Uma simulação interativa que demonstra como pequenas ações individuais podem 
gerar grandes efeitos ao longo do tempo — inspirada na **Teoria do Caos** e no 
conceito de efeito cascata.

---

## 🧠 Ideia do Projeto

Este projeto modela um ambiente com múltiplos agentes (pessoas), onde cada indivíduo possui:

* Humor
* Energia
* Influência

A cada interação, essas variáveis se propagam entre os agentes, criando **comportamentos emergentes** ao longo do tempo.

👉 Pequenas variações iniciais podem levar a resultados completamente diferentes.

---

## 🎯 Objetivo

Explorar na prática conceitos como:

* Sistemas complexos
* Efeito borboleta
* Propagação de estados
* Comportamento emergente

E, ao mesmo tempo, treinar:

* Programação Orientada a Objetos (POO)
* Modelagem de sistemas
* Visualização de dados

---

## ⚙️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Plotly

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone <repo-url>
cd cascading_effect
```

---

### 2. Instale as dependências (com Poetry)

```bash
poetry install
```

---

### 3. Execute a aplicação

```bash
make run-app
```

---

## 🎮 Como usar

* Escolha o número de pessoas
* Defina o número de interações
* Observe como o sistema evolui ao longo do tempo

📊 O sistema gera:

* Gráfico de evolução do humor por pessoa
* Média do grupo
* Energia média
* Dataset completo das simulações

---

## 🔬 Como funciona (resumo técnico)

Cada `Pessoa` interage com outras:

* O impacto depende de humor, influência e aleatoriedade
* O estado é atualizado a cada iteração
* Os dados são coletados ao longo do tempo

Isso cria um sistema com:

* Sensibilidade a condições iniciais
* Feedback entre agentes
* Evolução dinâmica

## 🧠 Insight

> Você não controla o resultado final, mas influencia profundamente a direção — principalmente nas pequenas coisas.

---

## 📌 Status

✔️ Funcional
🚧 Em evolução

---

## 📄 Licença

MIT
