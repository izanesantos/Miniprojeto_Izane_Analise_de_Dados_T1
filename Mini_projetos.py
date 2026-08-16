# ============================================================
# MINI-PROJETO - ANÁLISE DE DADOS COM PYTHON
# ============================================================
# Objetivo:
# Realizar uma análise exploratória de uma base de dados
# de varejo utilizando Pandas, Matplotlib e Seaborn.
# ============================================================


# Importação das bibliotecas utilizadas no projeto
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. IMPORTAÇÃO DA BASE DE DADOS
# ============================================================

# Carrega a base de dados já limpa utilizando o Pandas.
# O separador ";" é utilizado porque a base está nesse formato.
df = pd.read_csv("LIMPEZA/Base_Varejo_Limpa.csv", sep=";")


# Exibe as cinco primeiras linhas para verificar se os dados
# foram carregados corretamente.
print(df.head())


# ============================================================
# 2. ANÁLISE INICIAL DOS DADOS
# ============================================================

print("\n===== ANÁLISE DOS DADOS =====")


# Exibe a quantidade total de registros da base.
print("\nQuantidade de registros:")
print(df.shape[0])


# Exibe a quantidade de colunas existentes na base.
print("\nQuantidade de colunas:")
print(df.shape[1])


# Exibe um resumo estatístico das colunas numéricas,
# incluindo contagem, média, desvio padrão, mínimo,
# quartis e máximo.
print("\nResumo estatístico:")
print(df.describe())


# ============================================================
# 3. ANÁLISE DAS CATEGORIAS DE PRODUTOS
# ============================================================

print("\n===== QUANTIDADE DE VENDAS POR CATEGORIA =====")

# Conta quantos registros existem em cada categoria
# de produto.
print(df["PR_CAT"].value_counts())


# Exibe o nome de todas as colunas disponíveis na base.
print("\n===== COLUNAS DA BASE =====")
print(df.columns.tolist())


# ============================================================
# 4. ANÁLISE POR GÊNERO
# ============================================================

print("\n===== VENDAS POR GÊNERO =====")

# Conta a quantidade de registros para cada gênero.
print(df["CL_GENERO"].value_counts())


# ============================================================
# 5. ANÁLISE POR ESTADO CIVIL
# ============================================================

print("\n===== VENDAS POR ESTADO CIVIL =====")

# Conta a quantidade de registros para cada código
# de estado civil.
print(df["CL_EC"].value_counts())


# ============================================================
# 6. ANÁLISE POR SEGMENTO
# ============================================================

print("\n===== VENDAS POR SEGMENTO =====")

# Conta a quantidade de registros para cada segmento.
print(df["CL_SEG"].value_counts())


# ============================================================
# 7. CRUZAMENTO ENTRE GÊNERO E CATEGORIA
# ============================================================

print("\n===== GÊNERO POR CATEGORIA =====")

# Cria uma tabela cruzando gênero e categoria de produto.
# Isso permite comparar a quantidade de registros de homens
# e mulheres dentro de cada categoria.
genero_categoria = pd.crosstab(
    df["CL_GENERO"],
    df["PR_CAT"]
)

print(genero_categoria)


# ============================================================
# 8. ESTATÍSTICA - NÚMERO DE FILHOS
# ============================================================

print("\n===== ESTATÍSTICA - NÚMERO DE FILHOS =====")

# Calcula a média do número de filhos.
print("Média:", df["CL_FHL"].mean())

# Calcula a mediana do número de filhos.
print("Mediana:", df["CL_FHL"].median())

# Identifica a moda, ou seja, o valor que mais se repete.
print("Moda:", df["CL_FHL"].mode()[0])

# Calcula o desvio padrão.
print("Desvio padrão:", df["CL_FHL"].std())

# Identifica o maior número de filhos encontrado.
print("Máximo:", df["CL_FHL"].max())

# Identifica o menor número de filhos encontrado.
print("Mínimo:", df["CL_FHL"].min())

# Conta a quantidade de registros válidos.
print("Contagem:", df["CL_FHL"].count())


# Calcula os quartis:
# 25% = primeiro quartil
# 50% = mediana
# 75% = terceiro quartil
print("\nQuartis:")
print(df["CL_FHL"].quantile([0.25, 0.50, 0.75]))


# ============================================================
# 9. AGRUPAMENTO POR CATEGORIA
# ============================================================

print("\n===== AGRUPAMENTO POR CATEGORIA =====")

# Agrupa os registros por categoria e conta a quantidade
# de ocorrências de cada uma.
# sort_values() organiza do maior para o menor resultado.
agrupamento_categoria = (
    df.groupby("PR_CAT")
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_categoria)


# ============================================================
# 10. AGRUPAMENTO POR GÊNERO
# ============================================================

print("\n===== AGRUPAMENTO POR GÊNERO =====")

# Agrupa os registros por gênero e conta a quantidade
# de ocorrências de cada gênero.
agrupamento_genero = (
    df.groupby("CL_GENERO")
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_genero)


# ============================================================
# 11. AGRUPAMENTO POR GÊNERO E CATEGORIA
# ============================================================

print("\n===== AGRUPAMENTO: GÊNERO X CATEGORIA =====")

# Realiza um agrupamento utilizando duas colunas:
# gênero e categoria.
# O resultado mostra a quantidade de registros para
# cada combinação.
agrupamento_genero_categoria = (
    df.groupby(["CL_GENERO", "PR_CAT"])
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_genero_categoria)


# ============================================================
# 12. PRODUTOS MAIS FREQUENTES
# ============================================================

print("\n===== PRODUTOS MAIS FREQUENTES =====")

# Agrupa os registros pelo nome do produto e conta
# quantas vezes cada produto aparece.
produtos_frequentes = (
    df.groupby("PR_NOME")
      .size()
      .sort_values(ascending=False)
)

# Exibe somente os 10 produtos mais frequentes.
print(produtos_frequentes.head(10))


# ============================================================
# 13. VISUALIZAÇÃO - CATEGORIAS
# ============================================================

# Cria uma área para o primeiro gráfico.
plt.figure(figsize=(10, 6))

# Cria um gráfico de barras mostrando a quantidade
# de registros em cada categoria.
# value_counts() também é utilizado para ordenar
# as categorias da maior para a menor.
sns.countplot(
    data=df,
    x="PR_CAT",
    order=df["PR_CAT"].value_counts().index
)

# Define o título e os nomes dos eixos.
plt.title("Quantidade de registros por categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de registros")

# Exibe o gráfico.
plt.show()


# ============================================================
# 14. VISUALIZAÇÃO - GÊNERO X CATEGORIA
# ============================================================

# Cria novamente a tabela cruzada entre gênero e categoria.
genero_categoria = pd.crosstab(
    df["CL_GENERO"],
    df["PR_CAT"]
)


# Converte a tabela para um formato adequado para
# construção do gráfico.
dados_grafico = genero_categoria.reset_index().melt(
    id_vars="CL_GENERO",
    var_name="PR_CAT",
    value_name="QUANTIDADE"
)


# Define o tamanho do gráfico.
plt.figure(figsize=(10, 6))


# Cria um gráfico comparando os gêneros dentro de cada categoria.
sns.barplot(
    data=dados_grafico,
    x="PR_CAT",
    y="QUANTIDADE",
    hue="CL_GENERO"
)


# Define título e nomes dos eixos.
plt.title("Quantidade de registros por gênero e categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de registros")

# Exibe o gráfico.
plt.show()


# ============================================================
# 15. VISUALIZAÇÃO - NÚMERO DE FILHOS
# ============================================================

# Define o tamanho do gráfico.
plt.figure(figsize=(8, 5))


# Cria um gráfico mostrando a distribuição
# da quantidade de filhos dos clientes.
sns.countplot(
    data=df,
    x="CL_FHL"
)


# Define título e nomes dos eixos.
plt.title("Distribuição do número de filhos")
plt.xlabel("Número de filhos")
plt.ylabel("Quantidade de registros")

# Exibe o gráfico.
plt.show()


# ============================================================
# 16. CONCLUSÕES DA ANÁLISE
# ============================================================

print("\n===== CONCLUSÕES DA ANÁLISE =====")


# Insight 1: categoria com maior quantidade de registros.
print(
    "1. A categoria ALIMENTOS apresentou 384.197 registros, "
    "representando aproximadamente 52,4% da base."
)


# Insight 2: comparação entre os gêneros.
print(
    "2. O gênero F apresentou 382.427 registros, "
    "representando aproximadamente 52,1% da base."
)


# Insight 3: comparação entre gênero e categoria.
print(
    "3. A categoria ALIMENTOS apresentou a maior quantidade "
    "de registros para os dois gêneros: 200.274 para F "
    "e 183.923 para M."
)


# Insight 4: análise do número de filhos.
print(
    "4. O número de filhos apresentou média de aproximadamente "
    "1,15, enquanto a mediana e a moda foram iguais a 0."
)


# Insight 5: produto mais frequente.
print(
    "5. PRESUNTO COZIDO foi o produto mais frequente, "
    "com 12.719 registros."
)