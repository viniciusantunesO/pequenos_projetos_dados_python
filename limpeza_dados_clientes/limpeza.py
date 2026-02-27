import pandas as pd
import numpy as np

dados={
    "cliente_id": [1,2,3,4],
    "nome": ["Vini", "Milena", "Guilherme", "Arthur"],
    "idade": [20 ,np.nan, 19, 22],
    "renda": [20000, 15000, np.nan, 12000],
    "estado": ["PR", "SP", "MG", None],
    "score_credito": [700, 680, 720, 800]
}

df= pd.DataFrame(dados)
print("\n ------------------------------------------------------------")
print(df)

print("\n ------------------------------------------------------------")
df.info()

valores_nulos=df.isnull().sum()
print("\n ------------------------------------------------------------")
print(valores_nulos)

media_idade =df["idade"].mean()
df["idade"]=df["idade"].fillna(media_idade) #Se o valor estiver vazio, troque pela media

df["renda"]=df["renda"].fillna(0)

df["estado"]=df["estado"].fillna("Desconhecido")

#converte o tipo 
df["renda"]=df["renda"].astype(float)
df["idade"]=df["idade"].astype(int)

#criando novas colunas
df["renda_anual"]=df["renda"] * 12

#categotia de renda
def categoria_de_renda(valor):
    if valor >= 10000:
        return "Alta"
    elif valor >= 5000:
        return "Média"
    else:
        return "Baixa"
    
df["categoria_renda"]=df["renda"].apply(categoria_de_renda)

#filtrando clientes (clientes com alta renda)
clientes_promissores=df[df["categoria_renda"]=="Alta"]
print("\n ------------------------------------------------------------")
print(clientes_promissores)

#salvando a tabela nova para o arquivo clientes_limpos
df.to_csv("limpeza_dados_clientes/dados/clientes_limpos.csv", index=False)