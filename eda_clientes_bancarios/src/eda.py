import pandas as pd
import matplotlib.pyplot as plt

#carrega os dados do arquivo clientes_limpos
df = pd.read_csv("eda_clientes_bancarios/data/clientes_limpos.csv")

#olhar os dados
print("\n ----------------------------------------------")
print(df.head())#ver exemplos
print("\n ----------------------------------------------")
print(df.info())#tipo de dados
print("\n ----------------------------------------------")
print(df.describe())#resumo estatistico

df["idade"].mean()#idade media
df["renda"].mean()#renda media

df["renda"].max()#renda maxima
df["renda"].min()#renda minima

df.groupby("estado")["renda"].mean()#Em media, quanta cada estado ganha
df.groupby("estado")["cliente_id"].count()#quantos clientes em cada estado

df.sort_values("renda", ascending=False)#clientes q mais ganham primeiros
df.sort_values("renda")#clientes que menos ganham primeiros

df.groupby("categoria_renda")["cliente_id"].count()#quantos clientes tem em cada categoria de renda

#grafico q mostra renda por estado
df.groupby("estado")["renda"].mean().plot(kind="bar")
plt.title("Renda Média por Estado")
plt.xlabel("Estado")
plt.ylabel("Renda Média")
plt.show()

#grafico q mostra renda por Cliente
df.groupby("cliente_id")["renda"].mean().plot(kind="bar")
plt.title("Renda Média por Cliente")
plt.xlabel("Cliente")
plt.ylabel("Renda Média")
plt.show()
