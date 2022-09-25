class People:
  def __init__(self, name, age, pasw):
    self.__name = name
    self.__age = age
    self.__password = pasw

  #get Password
  @property
  def password(self):
    return self.__password
  
  #get Age
  @property
  def age(self):
    return self.__age

  
  @age.setter
  def age(self, age):
    self.__age = age
  
  def __str__(self):
    return f"""
- Player Name: {self.__name}
- Player age: {self.__name} 
    """