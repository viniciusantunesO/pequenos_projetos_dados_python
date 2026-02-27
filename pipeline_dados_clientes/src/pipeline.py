import pandas as pd

#Carrega um csv do arquivo e transforma em dataframe do pandas
def carrega_dados(caminho):
    return pd.read_csv(caminho)

#trata dados faltantes
def limpar_dados(df):
    df["renda"]=df["renda"].fillna(0)
    df["idade"]=df["idade"].fillna(df["idade"].mean())
    df["estado"]=df["estado"].fillna("Desconhecido")

    return df


def categoria(valor):
    if valor >= 10000:
        return "Alta"
    elif valor >= 5000:
        return "Média"
    else:
        return "Baixa"


#Cria novas tabelas a partir das existentes, converte dados brutos em informaçoes uteis
def transformar_dados(df):
    df["renda_anual"]=df["renda"]*12
    df["categoria_renda"]= df["renda"].apply(categoria)

    return df


#Trasforma o dataframe final em um arquivo csv
def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)

def main():
    caminho_entrada="pipeline_dados_clientes/data/clientes_brutos.csv"
    caminho_saida="pipeline_dados_clientes/data/clientes_tratados.csv"

    df= carrega_dados(caminho_entrada)
    df= limpar_dados(df)
    df= transformar_dados(df)
    salvar_dados(df, caminho_saida)


if __name__ == "__main__":
    main()