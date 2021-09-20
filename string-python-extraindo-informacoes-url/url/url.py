import re
from decimal import Decimal


# Teste de uma solução diferente para a extração dos parametros da URL


class Url:
  def __init__(self, url):
    self.url = self.sanitize_url(url)
    self.validate_url()
    self.__url_base, self.__url_params = self.get_url_components(url)

  def get_url_components(self, url):
    url_base, *url_params_str = url.split('?')
    url_params_list = []
    
    if (url_params_str): 
      url_params_list = url_params_str.split('&')
    
    url_params = {}

    for param_str in url_params_list:
      param_key, param_value = param_str.split('=')
      url_params[param_key] = param_value

    return [url_base, url_params]

  def sanitize_url(self, url):
    if not url: return ''
    return url.strip()

  def validate_url(self):
    if not self.url:
      raise ValueError('The URL string is empty')

  @property
  def url_base(self):
    return self.__url_base
  
  @property
  def url_params(self):
    return self.__url_params
  


url = Url("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
print(url.url_base)
print(url.url_params)
print(url.url_params['quantidade'])


# Desafio - criar o conversor de moedas

print('-----------------')
print('Desafio conversor')
print('-----------------')

# Real para Dolar
url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Dolar para Real
# url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"

# Real para Real
# url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=real"

# Dolar para Dolar
# url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=dolar"

# Dolar para Euro
# url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=euro"

url_obj = Url(url)

amount = Decimal(url_obj.url_params['quantidade'])
original_currency = url_obj.url_params['moedaOrigem']
desired_currency = url_obj.url_params['moedaDestino']

USD_rates = {
  'dolar': 1,
  'real': Decimal(5.50),
}

BRL_rates = {
  'real': 1,
  'dolar': Decimal(1 / USD_rates['real']),
}

exchange_rates_dict = {
  'dolar': USD_rates,
  'real': BRL_rates,
}

try:
  exchange_rate = exchange_rates_dict[original_currency][desired_currency]

  converted_value = amount * exchange_rate

  converted_value_output = f'{amount} - {original_currency.capitalize()} = {round(converted_value, 2)} - {desired_currency.capitalize()}'

  print(converted_value_output)

except KeyError:
  print(f'Câmbio de {original_currency} para {desired_currency} não está disponível')
