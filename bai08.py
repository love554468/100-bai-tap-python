# class hellu(object):
#     def __init__(self) -> None:
#         super().__init__()
#         self.s = 0
#     def setVal(self):
#         self.s = 3
#         return self.s

# a = hellu()

# print(a.setVal())

class Person:
 # Định nghĩa lớp "name"
 name = "Person"
 # Code by Quantrimang.com
 def __init__(self, xx = None):
 # self.name là biến instance
    self.name = xx

jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))