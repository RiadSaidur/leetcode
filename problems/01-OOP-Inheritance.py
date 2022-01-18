# 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻:
# Design TomCruise class and DulquerSalman class which inherit from Actor 
# class so that the following code provides the expected output.
# You can not change any of the given code. Do not modify the given parent 
# class.
# Note: add_movie() method in both child classes should work for any number 
# of parameters and assume parameters will be even numbers.

# class Actor:
#    def __init__(self, name, rating, industry):
#      self.name = name
#      self.rating = rating
#      self.industry = industry

#    def add_movie(self, *info):
#      pass

#    def __str__(self):
#      s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: 
# {self.industry}"
#      return s

# # Write your codes here.
# tom_cruise = TomCruise("Tom Cruise", 9.5, "Hollywood", 0)
# tom_cruise.add_movie("Knight & Day", "Action", "Top Gun", "Action", "Jerry 
# Maguire", "Romance", "Jack Reacher", "Thriller", "The Firm", "Thriller")
# print('1.------------------------------------')
# print(tom_cruise.oscar_status())
# print('2.------------------------------------')
# print(tom_cruise)
# print('3.====================================')
# dulquer_salman = DulquerSalman("Dulquer Salman", 9, "Malayalam", 5)
# dulquer_salman.add_movie("Thriller", "Bangalore Days", "Romance", "Ustad 
# Hotel", "Thriller", "Charlie", "Action", "Kurup", "Action", "Vikramadithyan")
# print('4.------------------------------------')
# print(dulquer_salman.award_status())
# print('5.------------------------------------')
# print(dulquer_salman)

# OUTPUT:
# 1.------------------------------------
# Tom Cruise has won 0 Oscar(s)!!!
# 2.------------------------------------
# Actor Details:
# Name: Tom Cruise
# Rating: 9.5
# Industry: Hollywood
# Oscar Win: 0
# Movies:
# Action: ['Knight & Day', 'Top Gun']
# Romance: ['Jerry Maguire']
# Thriller: ['Jack Reacher', 'The Firm']
# 3.====================================
# 4.------------------------------------
# Dulquer Salman has won 5 award(s)!!!
# 5.------------------------------------
# Actor Details:
# Name: Dulquer Salman
# Rating: 9
# Industry: Malayalam
# Award Win: 5
# Movies:
# Thriller: ['Bangalore Days', 'Charlie']
# Romance: ['Ustad Hotel']
# Action: ['Kurup', 'Vikramadithyan']

class Actor:
  def __init__(self, name, rating, industry):
    self.name = name
    self.rating = rating
    self.industry = industry
    self.movies = {}

  def add_movie(self, *info):
    pass

  def __str__(self):
    s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}"
    return s

class TomCruise(Actor):
  def __init__(self, name, rating, industry, oscar):
    super().__init__(name, rating, industry)
    self.oscar = oscar
  
  def add_movie(self, *info):
    for i in range(1, len(info), 2):
      try:
        self.movies[info[i]] = [*self.movies[info[i]], info[i-1]]
      except KeyError:
        self.movies[info[i]] = [info[i-1]]
  
  def oscar_status(self):
    return f"Tom Cruise has won {self.oscar} Oscar(s)!!!"
  
  def __str__(self):
    s = f"Actor Details:\nName: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}\nOscar Win: {self.oscar}\nMovies:\n"
    for category, movie in self.movies.items():
      s = s + f'{category}: {movie}\n'
    return s

class DulquerSalman(Actor):
  def __init__(self, name, rating, industry, awards):
      super().__init__(name, rating, industry)
      self.awards = awards
  
  def add_movie(self, *info):
    for i in range(0, len(info), 2):
      try:
        self.movies[info[i]] = [*self.movies[info[i]], info[i+1]]
      except KeyError:
        self.movies[info[i]] = [info[i+1]]
      

  def award_status(self):
    return f"Dulquer Salman has won {self.awards} award(s)!!!"

  def __str__(self):
    s = f"Actor Details:\nName: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}\nAwards Win: {self.awards}\nMovies:\n"
    for category, movie in self.movies.items():
      s = s + f'{category}: {movie}\n'
    return s

tom_cruise = TomCruise("Tom Cruise", 9.5, "Hollywood", 0)
tom_cruise.add_movie("Knight & Day", "Action", "Top Gun", "Action", "Jerry Maguire", "Romance", "Jack Reacher", "Thriller", "The Firm", "Thriller")
print('1.------------------------------------')
print(tom_cruise.oscar_status())
print('2.------------------------------------')
print(tom_cruise)
print('3.====================================')
dulquer_salman = DulquerSalman("Dulquer Salman", 9, "Malayalam", 5)
dulquer_salman.add_movie("Thriller", "Bangalore Days", "Romance", "Ustad Hotel", "Thriller", "Charlie", "Action", "Kurup", "Action", "Vikramadithyan")
print('4.------------------------------------')
print(dulquer_salman.award_status())
print('5.------------------------------------')
print(dulquer_salman)