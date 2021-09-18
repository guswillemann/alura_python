class Date:
  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year

  def formated(self):
    return '{:0>2}/{:0>2}/{:0>4}'.format(self.day,self.month,self.year)