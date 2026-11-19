class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        return f"My name is {self.name}."

    def display_age(self):
        return f"I am {self.age} years old."
    
Person1 = Person("Jorge Jangalay", 30)
print(Person1.display_name())
print(Person1.display_age())











