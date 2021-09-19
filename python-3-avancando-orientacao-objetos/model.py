class Performance:
  def __init__(self, name, year):
      self.__name = self.__format_name(name)
      self.year = year
      self.__likes = 0

  def __format_name(self, name):
    return name.title()

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, new_name):
    self.__name = self.__format_name(new_name)

  @property
  def likes(self):
    return self.__likes

  def add_like(self):
    self.__likes += 1
  
  def remove_like(self):
    self.__likes -= 1

  def __str__(self, details):
    return f'{self.name} | {details} | likes: {self.likes}'



class Movie(Performance):
  def __init__(self, name, year, duration):
    super().__init__(name, year)
    self.duration = duration

  def __str__(self):
    return super().__str__(f'{self.duration} min')



class Show(Performance):
  def __init__(self, name, year, seasons):
    super().__init__(name, year)
    self.seasons = seasons

  def __str__(self):
    season_text = 'seasons' if self.seasons > 1 else 'season'
    return super().__str__(f'{self.seasons} {season_text}')



class Playlist:
  def __init__(self, name, initial_list = []):
    self.name = name
    self.__list = list(initial_list)

  def __getitem__(self, item):
    return self.__list[item]

  def __len__(self):
    return len(self.__list)

  def add(self, performance):
    self.__list.append(performance)
  
  def remove(self, performance):
    self.__list.remove(performance)
  


avengers = Movie('avengers - infinity war', 2018, 160)
atlanta = Show('atlanta', 2018, 2)

avengers.add_like()
avengers.add_like()
avengers.add_like()

atlanta.add_like()
atlanta.add_like()

playlist = Playlist('weekend', [avengers, atlanta])

for performance in playlist:
  print(performance)
