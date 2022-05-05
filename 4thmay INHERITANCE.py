class parent:

  def __init__ (self, name, place):
    self.name= name
    self.place= place

  def parentfunction(self):

    print("name=", self.name)
    print("place=", self.place)
    print("_______")

class child(parent):

  def childfunction(self):
    print("name=", self.name)

obj= child("dhoni", "jharkahnad")
obj.parentfunction()
obj.childfunction()
