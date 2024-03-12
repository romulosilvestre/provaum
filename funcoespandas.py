import pandas as pd
from colorama import Fore
from emailaut3 import EmailAut3

corpo_email = []
def pegar():

    dados = pd.read_csv('housing.csv')
    print("**********MOSTRANDO OS DADOS*********\n")
    print(dados)
    print(f"\nTotal de Registros:{len(dados)}\n")

    # Loop para percorrer cada linha do DataFrame
    print("******Mostrando cada linha do DataFrame*****")
    for indice, registro in dados.iterrows():
       print(f"{indice}--{registro}")
       print(f"****{Fore.RED}PROXIMA LINHA****{Fore.RESET}")
    print("******Realizando o filtro no DataFrame*****")
    #Realizar o filtro
    # Filtrar os dados com base nas condições especificadas
    dados_filtrados = dados.query('10000 <= area <= 10999 and 5000000 <= price <= 5999999 and bedrooms > 2')

    # Verificar se existem linhas que satisfazem as condições
    if len(dados_filtrados) > 0:
        print("\n******Mostrando os dados filtrados*****")
        print(dados_filtrados)
    else:
        print("\nNenhum registro encontrado que satisfaça as condições.")

    print(f"\nTotal de Registros FIltrados: {len(dados_filtrados)}\n")

#Formatando a saída.
    print("******Formatando a saida*****")

    # Definição das condições
    condicoes = (dados['area'].between(10000, 10999) &
                 dados['price'].between(5000000, 5999999) &
                 (dados['bedrooms'] > 2))

    # Filtragem dos dados
    dados_filtrados = dados[condicoes]

    if not dados_filtrados.empty:
        print("\n****** Mostrando os dados filtrados ******\n")

        # Pesquisar o significado de cada série (coluna)
        significado_series = {
            'area': 'Área da propriedade',
            'preco': 'Preço da propriedade',
            'quartos': 'Número de quartos na propriedade'
        }

        # Iterar sobre os registros filtrados e formatar o texto

        for indice, registro in dados_filtrados.iterrows():
            print("Registro: ", indice)
            for serie, valor in registro.items():
                if serie in significado_series:
                     print(f"{significado_series[serie]}: {valor}")

    else:
        print("\nNenhum registro encontrado que satisfaça as condições.\n")
print("instânciando para mandar o email")

def main():
     enviando = EmailAut3(destinatario="xxxxxxxxx@gmail.com",
                                assunto="xxxxxxxxxxx",
                                conteudo=f"{corpo_email}",
                                anexos=0)

     print("enviando ...")
     enviando.envio()

if __name__ == "__main__":
    main()
