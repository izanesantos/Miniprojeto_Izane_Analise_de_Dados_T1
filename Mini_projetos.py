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



