# -*- coding: utf-8 -*-
import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

class EmailAut2:

    def __init__(self, destinatario, assunto, conteudo, anexos):
        self.destinatario = destinatario
        self.assunto = assunto
        self.conteudo = conteudo
        self.anexos = anexos
        self.arquivos = []
        pasta = "Email/Anexos"
        if self.anexos == 1:
            for arquivo in os.listdir(pasta):
                caminho_completo = os.path.join(pasta, arquivo)
                self.arquivos.append(caminho_completo)

    def envio(self):
        msg = MIMEMultipart()
        msg['From'] = "instrutor.romulo@gmail.com"
        password = "pusrrnrdpqoqwfmt"
        msg['Subject'] = self.assunto
        msg['To'] = self.destinatario
        msg.attach(MIMEText(self.conteudo, 'plain'))

        if self.anexos == 1:
            for arquivo in self.arquivos:
                with open(arquivo, 'rb') as file:
                    nome_arquivo = os.path.basename(arquivo)
                    if 'github' in nome_arquivo:
                        continue
                    attachment = MIMEApplication(file.read(), 'octet-stream')
                    attachment.add_header('Content-Disposition', 'attachment', filename=nome_arquivo)
                    msg.attach(attachment)

        try:

            # Configura integração com Gmail usando TLS na porta 587
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print(f'Email enviado para {self.destinatario}')
        except Exception as e:
            print(f'Erro ao enviar o e-mail: {e}')
        finally:
            s.quit()
