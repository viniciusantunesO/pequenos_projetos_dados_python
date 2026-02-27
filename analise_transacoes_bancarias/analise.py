import pandas as pd #serve para trabalhar com tabelas
import numpy as np #ajuda a criar nmumeros aleatorios

#Aqui estamos inventando dados / 20 compras aleatorias feita por 6 pessoas
np.random.seed(1)
dados={
    "Cliente_id": np.random.randint(1,6,20),
    "Estado": np.random.choice(["PR", "SP", "MG", "SC"], 20),
    "Categoria": np.random.choice(["Alimentacao", "Lazer", "Transporte"], 20),
     "Valor": np.random.uniform(1, 500, 20)
    }

#Vamos trabnsformar os dados em uma tabela(dataframe) usando pandas
df=pd.DataFrame(dados)
print("\n -------------TABELA-------------")
print(df)

#Entender as tabelas
print("\n -------------INFORMACOES DA TABELA-------------")
df.info()

#ver se tem dados nulos
df.isnull().sum()

#ve quanto cada cliente gastou no total
total_por_cliente= df.groupby("Cliente_id")["Valor"].sum()
print("\n -------------QUANTO CADA CLIENTE GASTOU-------------")
print(total_por_cliente)

#quem gastou mais
cliente_top=total_por_cliente.idxmax() #cliente q mais gastou
valor_top=total_por_cliente.max() #valor total do cliente q mais gastou

print("\n -------------QUEM GASTOU MAIS-------------")
print(cliente_top, valor_top)

#media de gastos por estado
media_estado= df.groupby("Estado")["Valor"].mean()
print("\n -------------MEDIA DE GASTO POR ESTADO-------------")
print(media_estado)

#gastos por categorias
gasto_categorias= df.groupby("Categoria")["Valor"].sum()
print("\n -------------GASTO POR CATEGORIA-------------")
print(gasto_categorias)

#cria uma coluna nova para classificar os gastos
df["nivel_gastos"]= pd.cut(
    df["Valor"],
    bins=[0,100,300,1000], #intervalos
    labels=["Baixo", "Medio", "Alto"] #rotulos
)


#procurando gastos fora do padrao
Q1 = df["Valor"].quantile(0.25)
Q3 = df["Valor"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["Valor"] > Q3 + 1.5 * IQR)
]

print(outliers)
print("\n -------------TABELA FINAL-------------")
print(df)
