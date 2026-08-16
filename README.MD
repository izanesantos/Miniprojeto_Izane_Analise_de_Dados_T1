#  Mini-Projeto — Análise de Dados com Python

##  Objetivo

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (AED) utilizando Python e Pandas sobre uma base de dados de varejo.

Foram realizadas etapas de importação, verificação, limpeza, análise estatística, agrupamentos e visualização dos dados, buscando identificar padrões no comportamento das vendas e dos clientes.

## Sobre a Base de Dados

A base utilizada foi a `Varejo.csv`.

Após o processo de limpeza, a base ficou com:

- 733.447 registros
- 10 colunas

As principais informações disponíveis são:

- Data da compra
- Identificador da compra
- Identificador do cliente
- Gênero
- Estado civil
- Número de filhos
- Segmento
- Identificador do produto
- Categoria do produto
- Nome do produto

##  Limpeza dos Dados

Durante a preparação da base foram realizadas verificações e tratamentos dos dados.

Foram analisados:

- Valores nulos
- Registros duplicados
- Tipos das colunas
- Formato das datas
- Consistência das informações

Também foi realizada a remoção de registros duplicados e criada uma base final limpa chamada `df_limpo.csv`.

##  Análise Exploratória

Foram realizadas análises para compreender a distribuição dos registros entre categorias, gêneros, segmentos e produtos.

### Categorias

A categoria com maior quantidade de registros foi:

**ALIMENTOS — 384.197 registros**

Representando aproximadamente 52,4% da base.

### Gênero

O gênero F apresentou:

**382.427 registros**

Enquanto o gênero M apresentou:

**351.020 registros**

### Número de filhos

A análise da coluna `CL_FHL` apresentou:

- Média: 1,15
- Mediana: 0
- Moda: 0
- Desvio padrão: 1,42
- Mínimo: 0
- Máximo: 4

##  Visualizações

Foram criados gráficos utilizando Matplotlib e Seaborn para facilitar a interpretação dos resultados.

Os gráficos analisaram:

- Quantidade de registros por categoria
- Quantidade de registros por gênero e categoria
- Distribuição do número de filhos

##  Principais Insights

1. A categoria **ALIMENTOS** apresentou 384.197 registros, representando aproximadamente 52,4% da base.

2. O gênero **F** apresentou 382.427 registros, representando aproximadamente 52,1% da base.

3. A categoria **ALIMENTOS** apresentou a maior quantidade de registros para os dois gêneros: 200.274 para F e 183.923 para M.

4. O número de filhos apresentou média de aproximadamente 1,15, enquanto a mediana e a moda foram iguais a 0.

5. **PRESUNTO COZIDO** foi o produto mais frequente, com 12.719 registros.

##  Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Git
- GitHub

## ▶ Como Executar o Projeto

1. Clone este repositório.
2. Tenha o Python instalado.
3. Instale as bibliotecas necessárias:

```bash
pip install pandas matplotlib seaborn