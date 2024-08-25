# rastreador-preco-cripto


Este projeto é um script em Python que verifica a cotação do Bitcoin em relação ao Real (BTC-BRL) e envia um alerta por e-mail quando a cotação está abaixo de um limite especificado pelo usuário. O script usa a API da AwesomeAPI para obter a cotação do BTC-BRL e o servidor SMTP do Gmail para enviar e-mails.

## Funcionalidades

- Obtém a cotação atual do BTC-BRL.
- Envia um alerta por e-mail se a cotação estiver abaixo do limite especificado.
- Executa a verificação a cada 10 minutos.

## Crie o arquivo settings.py
Esse arquivo terá a senha(password), que você precisará criar com o link
[https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords), para permitir que seu email
seja acessado pelo seu código.
sender é o email que você configurou com o link acima.

password = 'Sua senha'
sender = 'Seu email'
