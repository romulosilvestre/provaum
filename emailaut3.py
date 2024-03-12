# -*- coding: utf-8 -*-

import smtplib
import email.message
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import pandas as pd
from colorama import Fore



# Módulo para envio envio de e-mail com os documentos ao cliente
# Os documentos devem ser anexados dentro da pasta Email/Anexos
# Após o envio os documentos são apagados


class EmailAut3:


    def __init__(self, destinatario, assunto, conteudo, anexos):
        self.destinatario = destinatario
        self.assunto = assunto
        self.conteudo = conteudo

        # Se anexos for igual a 1, o e-mail será enviado com os anexos
        self.anexos = anexos

        self.arquivos = []
        pasta = "Email/Anexos"
        if self.anexos == 1:
            for arquivo in os.listdir(pasta):
                caminho_completo = os.path.join(pasta, arquivo)
                self.arquivos.append(caminho_completo)

    def envio(self):
        msg = MIMEMultipart()
        msg.add_header('Content-Type', 'text/html')

        msg['From'] = "instrutor.romulo@gmail.com"
        password = "pusrrnrdpqoqwfmt"

        msg['Subject'] = self.assunto
        msg['To'] = self.destinatario
        msg.attach(MIMEText(self.conteudo, 'plain'))  # Adiciona o conteúdo do e-mail como parte da mensagem

        # Inclusão dos anexos
        if self.anexos == 1:
            for arquivo in self.arquivos:

                with open(arquivo, 'rb') as file:
                    nome_arquivo = os.path.basename(arquivo)

                    if 'github' in nome_arquivo:
                        continue

                    attachment = MIMEApplication(file.read(), 'octet-stream')
                    attachment.add_header('Content-Disposition', 'attachment', filename=nome_arquivo)
                    msg.attach(attachment)

        # Configura integração com Gmail
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        time.sleep(3)
        print(f'Email enviado para {self.destinatario}')
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
    enviando = EmailAut3(destinatario="romulogurgeldf@gmail.com",
                         assunto="Novo e-mail",
                         conteudo="oi de novo kkkk",
                         anexos=0)
    enviando.envio()

if __name__ == '__main__':
    main()