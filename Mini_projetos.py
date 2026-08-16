import pandas as pd

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


