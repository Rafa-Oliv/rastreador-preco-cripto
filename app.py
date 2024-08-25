import smtplib
import requests
import schedule
from time import sleep
from datetime import datetime
from email.message import EmailMessage
from settings import password, sender
from email_validator import validate_email

class BTCBRLQuotation:

    def __init__(self):
        
        self.URL = 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
        self.limit = None
        self.email = None

    def current_datetime(self):
        
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime

    def get_user_info(self):
        
        # Obter dados do usuario, limite  do btc e email
        while True:
            try:
                self.limit = float(input('Digite o limite máximo do BTC-BRL para receber um alerta para compra: '))
                break
            except ValueError:
                print('Digite apenas números e coloque ponto, no lugar da vírgula\n')
                sleep(1)

        while True:
            try:
                email = input('Digite um email para receber o alerta: ')
                valid = validate_email(email)
                self.email = valid.email
                break
            except:
                print('Digite um email válido\n')
                sleep(1)

    def send_email(self, recipient, message):

        
        try:
            print('Enviando email ...')
            # configurações de login para envio da mensagem
            EMAIL_ADDRESS = sender
            EMAIL_PASSWORD = password

            # cria o email
            mail = EmailMessage()
            mail['Subject'] = 'COTAÇÃO BTC-BRL'
            mail['From'] = EMAIL_ADDRESS
            mail['To'] = recipient
            mail.add_header('Content-Type', 'text/html')
            mail.set_payload(message.encode('utf-8'))

            # envia o email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
                email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                email.send_message(mail)
            print('Email enviado !!')
            print(100*'-')
            
        except:
            
            print(f'Erro ao enviar o email {self.current_datetime()}')
            print(100*'-')

    def fetch_quotation(self):
        
        # chamada para a api
        self.response = requests.get(self.URL)
        try:
            if self.response.status_code == 200:
                # O preço de compra do Bitcoin (quanto você pagaria para comprar um Bitcoin.
                self.purchase_price = float(self.response.json()['BTCBRL']['bid'])
                formatted_price = f'{self.purchase_price:.2f}'
                formatted_limit = f'{self.limit:.2f}'

                if self.purchase_price < self.limit:
                    self.message = f'Cotação para compra do BTC-BRL às {self.current_datetime()}: R$ {formatted_price}\nValor abaixo de: R$ {formatted_limit}'
                    self.send_email(self.email, self.message)
            else:
                print(f'Não foi possível obter a cotação do BTC-BRL\n{self.current_datetime()}')
                print(100*'-')
        except:
            print(f'Não foi possível obter a cotação do BTC-BRL\n{self.current_datetime()}')
            print(100*'-')
            

#instanciando a classe e chamando os métodos
            
bot = BTCBRLQuotation()

bot.get_user_info()

bot.fetch_quotation()

schedule.every(10).minutes.do(bot.fetch_quotation)

while True:
    
    schedule.run_pending()
    
    sleep(2)
