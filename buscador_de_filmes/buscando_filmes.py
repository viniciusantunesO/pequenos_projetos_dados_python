import requests

CHAVE="api-key"

def buscar_filme(filme):
    url=f"http://www.omdbapi.com/?t={filme}&apikey={CHAVE}"

    resposta=requests.get(url)

    if resposta.status_code != 200:
        print("Erro na requisicao")
        return None

    dados=resposta.json()

    if dados["Response"] == "False":
        print("Filme não encontrado!")
        return None

    return dados

def dados_filme(dados):
    print("\n=== FILME ENCONTRADO ===")
    print("Título:", dados["Title"])
    print("Ano:", dados["Year"])
    print("Gênero:", dados["Genre"])
    print("Diretor:", dados["Director"])
    print("Nota IMDb:", dados["imdbRating"])
    print("Sinopse:", dados["Plot"])

while True:
    titulo = input("\nDigite o nome do filme (ou 'sair'): ")
    
    if titulo.lower() == "sair":
        break
    
    dados = buscar_filme(titulo)
    
    if dados:
        dados_filme(dados)

  

