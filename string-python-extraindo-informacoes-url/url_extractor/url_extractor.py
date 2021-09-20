import re
from decimal import Decimal


class URlExtractor:
  def __init__(self, url):
    self.url = self.sanitize_url(url)
    self.validate_url()

  def sanitize_url(self, url):
    if not url: return ''
    return url.strip()

  def validate_url(self):
    if not self.url:
      raise ValueError('The URL string is empty')

    url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
    match = url_pattern.match(self.url)
    if not match:
      raise ValueError('The URL is not valid')

  def get_url_base(self):
    question_mark_index = self.url.find('?')
    return self.url[:question_mark_index]
  
  def get_url_params(self):
    question_mark_index = self.url.find('?')
    return self.url[question_mark_index+1:]

  def get_param_value(self, param_name):
    params = self.get_url_params()

    param_index = params.find(param_name)
    value_index = param_index + len(param_name) + 1
    ampersand_index = self.get_url_params().find('&', param_index)

    if ampersand_index == -1:
      value = params[value_index:]
    else:
      value = params[value_index:ampersand_index]

    return value

  def __len__(self):
    return len(self.url)

  def __eq__(self, other):
    return self.url == other.url
  
  def __ne__(self, other):
    return self.url != other.url

  def __str__(self):
    return f'{self.url}\nURL base: {self.get_url_base()}\nURL params: {self.get_url_params()}'

url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url_extractor = URlExtractor(url)
url_extractor2 = URlExtractor(url)
value_param_quantidade = url_extractor.get_param_value("quantidade")

print(f'Valor param quantidade: {value_param_quantidade}', end='\n\n')
print(url_extractor, end='\n\n')
print(f'len(url_extractor): {len(url_extractor)}', end='\n\n')
print(f'url_extractor == url_extractor2: {url_extractor == url_extractor2}')


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

url_extractor = URlExtractor(url)

amount = Decimal(url_extractor.get_param_value('quantidade'))
original_currency = url_extractor.get_param_value('moedaOrigem')
desired_currency = url_extractor.get_param_value('moedaDestino')

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
