# -*- coding: utf-8 -*-
#%% basic
class Matematik:

    def topla(self,sayi1,sayi2): #self yazma nedenimiz self java c# gibi dillerde gerekmiyor ancak pythonda lazım
        return sayi1 + sayi2     #self class yapılırsa fonks.larda self eklenmelidir.
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
matematik = Matematik()
matematik2 = Matematik()
print("Sonuç = " + str(matematik.carp(5,145)))

#%% init kısmı
class Matematik:
    def __init__(self,sayi1,sayi2): #__init__ komutu java c#da daha çok lazım olacak ondan şuan için önemli
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        return self.sayi1 + self.sayi2    
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
matematik = Matematik(2,78)
matematik2 = Matematik(3,76)
print("Sonuç = " + str(matematik2.carp()))

#%% Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastNam = lastName
        self.age = age
        
        
person1 = Person("Şükrü", "Şimşek", 23)
print(person1.firstName)
print(person1.age)

#%%
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
ahmet = Worker()

mehmet = Customer()


#%%

class Person:
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
 
    def print(self):
        print(self.name, self.surname, self.age, self.salary)
 
class Employee(Person):
    def __init__(self,name,surname,age,salary):
        super().__init__(name,surname,age,salary)
 
a = Employee("Şükrü","Şimşek",23,"10000TL")
a.print()
