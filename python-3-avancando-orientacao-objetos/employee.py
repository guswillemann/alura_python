class Employee:
  def __init__(self, name):
    self.name = name.capitalize()
  
  def log_hours(self, hours):
    print(f'Logged {hours} hours.')

  def display_tasks(self):
    print('Did a lot of stuff...')

class Caelum(Employee):
  def display_tasks(self):
    print('Did a lot of stuff, Caelumer')

  def get_mounth_courses(self, mounth=None):
    print(f'Showing courses - {mounth}' if mounth else 'Showing current mounth courses')

class Alura(Employee):
  def display_tasks(self):
    print('Did a lot of stuff, Alurete!')

  def get_non_answered_questions(self):
    print('Showing non answered forum questions')



class Junior(Alura):
  pass

class Pleno(Alura, Caelum):
  pass
        


class Hipster:
  def __str__(self):
    return f'Hipster {self.name}'


jose = Junior('jose')
jose.get_non_answered_questions()

luan = Pleno('luan')
luan.get_non_answered_questions()
luan.get_mounth_courses()

luan.display_tasks()

print(luan)