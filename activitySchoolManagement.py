class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

def get_age(self):
    return self.__age 


Person1 = Person("Lina", 20) 
print(f"Name: {Person1.name}") 
print(f"Age: {Person1.get_age()}") 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return self.__age 


Person1 = Person("Lina", 20) 
print(f"Name: {Person1.name}") 
print(f"Age: {Person1.get_age()}") 

#It protects your data and lets you change how the age is calculated or stored later without breaking the rest of the code.