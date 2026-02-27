import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta=requests.get(url)

    if resposta.status_code != 200:
        print("Erro na requisicao")
        return None
    
    dados=resposta.json()

    if "erro" in dados:
        print("CEP nao encontrado")
        return None
    
    return dados

def mostrar_endereco(dados):
    print("\nEndereço encontrado:")
    print("Rua:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:", dados["localidade"])
    print("Estado:", dados["uf"])

def validar_cep(cep):
    return cep.isdigit() and len(cep) == 8


while True:
    cep = input("\nDigite o CEP (ou 'sair'): ")
    
    if cep.lower() == "sair":
        break
    
    if not validar_cep(cep):
        print("CEP inválido! Digite apenas 8 números.")
        continue
    
    dados = buscar_cep(cep)
    
    if dados:
        mostrar_endereco(dados)
