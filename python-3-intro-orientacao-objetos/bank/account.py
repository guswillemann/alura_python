class Account:
  def __init__(self, number, owner, balance, limit = 1000):
    self.__number = number
    self.__owner = owner
    self.__balance = balance
    self.__limit = limit

  def deposit(self, value):
    self.__balance += value
  
  def withdraw(self, value):
    if (self.__has_avaible_balance(value)):
      self.__balance -= value
    else:
      print('Insufficient balance for the operation')

  def balance_consult(self):
    print(self.__balance)

  def transfer(self, value, account_destiny):
    if (self.__has_avaible_balance(value)):
      self.withdraw(value)
      account_destiny.deposit(value)
    else:
      print('Insufficient balance for the operation')

  def __has_avaible_balance(self, transaction_value):
    available_balance = self.__balance + self.__limit
    return available_balance >= transaction_value

  @property
  def number(self):
    return self.__number

  @property
  def owner(self):
    return self.__owner

  @owner.setter
  def owner(self, owner):
    self.__owner = owner
  
  @property
  def limit(self):
    return self.__limit

  @limit.setter
  def limit(self, limit):
    self.__limit = limit

  @staticmethod
  def bank_code():
    return '001'
  
  @staticmethod
  def bank_code_list():
    return {'BB': '001', 'Caixa': '104', 'Bradescos': '237'}