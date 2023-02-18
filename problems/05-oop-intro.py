"""
1. Inheritance
2. Polymorphism
  2.1 Overriding (Child)
3. Abstraction
4. Encapsulation

Target: School
Student:
  1. Name
  2. Id
  3. Section
Teacher:
  1. Name
  2. Id
  3. Class
"""

class Person:
  # property
  name: str
  idx: int

  # consrtuctor
  def __init__(self, name, idx) -> None:
    self.name = name
    self.idx = idx
  
  # methods
  def capitalize_name(self) -> str:
    return self.name.upper()

  # dunder methods
  def __str__(self) -> str:
    return self.name

# inheritance
class Student(Person):
  section: str

  # abstraction
  def set_section(self, idx):
    if idx < 50:
      return 'A'
    else:
      return 'B'

  def __init__(self, name, idx) -> None:
    super().__init__(name, idx)
    self.section = self.set_section(idx)
  
  # polymorphism (overriding) 
  def __str__(self) -> str:
    return f'{self.idx} - {self.name} - {self.section}'

    
std1 = Student('Nazib', 49)
std2 = Student('Nazib er Ex', 51)