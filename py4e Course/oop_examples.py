# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:10:08 2020

@author: Tomi
"""

class Student:
    def __init__(self, fname, lname, sub_no):
        self.firstname = fname
        self.lastname = lname
        self.subjectnumber = sub_no
    
    def fullname(self):
        return self.firstname + str(' ') + self.lastname
    
    def double_sub(self):
        return self.subjectnumber * 2

x = Student("John", "Doe", 5)
print(x.fullname())
print(x.double_sub())

class PartyAnimal:
    x = 0
    def __init__(self):
        print('I am initialized at', self.x)
    def party(self):
        self.x = self.x + 1
        print("I am now", self.x)
    def __del__(self):
        print('Class being deleted at', self.x)
an = PartyAnimal()
print('Debug: Hope I assigned it')
an.party()
PartyAnimal.party(an)
print(an)
an = 42
print('assigned an', an)

class PartyAnny:
    x = 0
    name = ''
    def __init__(self, nam):
        print('I am initialised')
        self.name = nam
        print(self.name, nam, 'what am I?')
        
    def party(self):
        self.x = self.x + 1
        print(self.x)
    
    def __del__(self):
        print('Destroying')
s = PartyAnny('Sally')
y = PartyAnny('Yolo')
s.party()
y.party()
s.party()
