url = 'bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

url = url.strip()

if url == '':
  raise ValueError('A URL está vazia')

question_mark_index = url.find('?')
url_base = url[:question_mark_index]
url_params = url[question_mark_index+1:]

param = 'quantidade'
param_index = url_params.find(param)
value_index = param_index + len(param) + 1
ampersand_index = url_params.find('&', param_index)

if ampersand_index == -1:
  value = url_params[value_index:]
else:
  value = url_params[value_index:ampersand_index]

print(value)











# url_base, url_params_str = url.split('?')
# url_params_list = url_params_str.split('&')
# url_params = {}

# for param_str in url_params_list:
#   param_key, param_value = param_str.split('=')
#   url_params[param_key] = param_value

# t_var = url_params
# print(t_var)