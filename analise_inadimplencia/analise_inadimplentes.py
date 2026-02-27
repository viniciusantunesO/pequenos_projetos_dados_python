import pandas as pd

dados = {
    "cliente_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "renda": [1800, 2500, 3200, 1500, 4200, 6000, 2200, 3500, 5000, 2800],
    "divida": [500, 1200, 800, 2000, 1000, 3500, 1800, 900, 4500, 600],
    "score_credito": [520, 610, 650, 480, 720, 690, 560, 680, 590, 640],
    "inadimplente": [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
}

df=pd.DataFrame(dados)
print(df)

#Score medio dos inadimplentes
ola=df.groupby("inadimplente")["score_credito"].mean()
print(ola)#vimos q quem é inadimplente tem score menor

media_score=df["score_credito"].mean()
print(media_score)

#Respondendo a pergunta: Quem tem o maior risco?
df["relacao_divida_renda"]=df["divida"]/df["renda"]
df["risco"]=df["relacao_divida_renda"] * (media_score - df["score_credito"])

nao_inadimplente=df[df["inadimplente"]==0]#filtra, mostrabdo so quem nao é inadimplente

maiores_riscos=nao_inadimplente.sort_values("risco", ascending=False)# ordena do maior risco para o menor

print(maiores_riscos)
