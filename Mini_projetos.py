import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("LIMPEZA/Base_Varejo_Limpa.csv", sep=";")

print(df.head())

print("\n===== ANÁLISE DOS DADOS =====")

print("\nQuantidade de registros:")
print(df.shape[0])

print("\nQuantidade de colunas:")
print(df.shape[1])

print("\nResumo estatístico:")
print(df.describe())

print("\n===== QUANTIDADE DE VENDAS POR CATEGORIA =====")

print(df["PR_CAT"].value_counts())

print("\n===== COLUNAS DA BASE =====")
print(df.columns.tolist())

print("\n===== VENDAS POR GÊNERO =====")

print(df["CL_GENERO"].value_counts())

print("\n===== VENDAS POR ESTADO CIVIL =====")

print(df["CL_EC"].value_counts())

print("\n===== VENDAS POR SEGMENTO =====")

print(df["CL_SEG"].value_counts())

print("\n===== GÊNERO POR CATEGORIA =====")

genero_categoria = pd.crosstab(df["CL_GENERO"], df["PR_CAT"])

print(genero_categoria)

print("\n===== ESTATÍSTICA - NÚMERO DE FILHOS =====")

print("Média:", df["CL_FHL"].mean())
print("Mediana:", df["CL_FHL"].median())
print("Moda:", df["CL_FHL"].mode()[0])
print("Desvio padrão:", df["CL_FHL"].std())
print("Máximo:", df["CL_FHL"].max())
print("Mínimo:", df["CL_FHL"].min())
print("Contagem:", df["CL_FHL"].count())

print("\nQuartis:")
print(df["CL_FHL"].quantile([0.25, 0.50, 0.75]))

print("\n===== AGRUPAMENTO POR CATEGORIA =====")

agrupamento_categoria = df.groupby("PR_CAT").size().sort_values(ascending=False)

print(agrupamento_categoria)

print("\n===== AGRUPAMENTO POR GÊNERO =====")

agrupamento_genero = df.groupby("CL_GENERO").size().sort_values(ascending=False)

print(agrupamento_genero)

print("\n===== AGRUPAMENTO: GÊNERO X CATEGORIA =====")

agrupamento_genero_categoria = (
    df.groupby(["CL_GENERO", "PR_CAT"])
      .size()
      .sort_values(ascending=False)
)

print(agrupamento_genero_categoria)

print("\n===== PRODUTOS MAIS FREQUENTES =====")

produtos_frequentes = (
    df.groupby("PR_NOME")
      .size()
      .sort_values(ascending=False)
)

print(produtos_frequentes.head(10))

#Visualização dos dados
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="PR_CAT",
    order=df["PR_CAT"].value_counts().index
)

plt.title("Quantidade de registros por categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de registros")

plt.show()

genero_categoria = pd.crosstab(df["CL_GENERO"], df["PR_CAT"])

dados_grafico = genero_categoria.reset_index().melt(
    id_vars="CL_GENERO",
    var_name="PR_CAT",
    value_name="QUANTIDADE"
)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=dados_grafico,
    x="PR_CAT",
    y="QUANTIDADE",
    hue="CL_GENERO"
)

plt.title("Quantidade de registros por gênero e categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de registros")

plt.show()

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="CL_FHL"
)

plt.title("Distribuição do número de filhos")
plt.xlabel("Número de filhos")
plt.ylabel("Quantidade de registros")

plt.show()


print("\n===== CONCLUSÕES DA ANÁLISE =====")

print("1. A categoria ALIMENTOS apresentou 384.197 registros, "
      "representando aproximadamente 52,4% da base.")

print("2. O gênero F apresentou 382.427 registros, "
      "representando aproximadamente 52,1% da base.")

print("3. A categoria ALIMENTOS apresentou a maior quantidade de registros "
      "para os dois gêneros: 200.274 para F e 183.923 para M.")

print("4. O número de filhos apresentou média de aproximadamente 1,15, "
      "enquanto a mediana e a moda foram iguais a 0.")

print("5. PRESUNTO COZIDO foi o produto mais frequente, "
      "com 12.719 registros.")