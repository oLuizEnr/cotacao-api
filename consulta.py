from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.environ.get('API_KEY')

r = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD').json()

cotacoes = r['conversion_rates']

print(f'O valor do dólar em reais é {cotacoes['BRL']}')

while True:
    resposta = input('Quer verificar a o valor do dólar em outras moedas? (Digite s para ver ou n para encerrar): ').lower()
    if resposta == 's':
        cotacoes.pop('BRL')
        print(f'Os valores do dólar em cada moeda é:')
        for x, y in cotacoes.items():
            print(f'{x}: {y}')
        break
    elif resposta == 'n':
        break
    else:
        print('Opção inválida, por favor digite "s" ou "n".')

print('Obrigado por usar o programa!')