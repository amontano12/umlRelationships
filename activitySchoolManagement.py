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
        
class Student(Person):

    def __init__(self, name, __age):
        super().__init__(name, __age)

    def study(self):
        return f'{self.name} is studying.'

student1 = Student("Lina", 30)
print(student1.get_age())
print(f'Age: {student1.get_age()}')
print(student1.study())

class Teacher(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def teach(self):
        return f'{self.name} is teaching.'

teacher1 = Teacher("Mona", 30)
print(teacher1.get_age())
print(f'Age: {teacher1.get_age()}')
print(teacher1.teach())









Person1 = Person("Lina", 20) 
print(f"Name: {Person1.name}") 
print(f"Age: {Person1.get_age()}\n")

#It protects your data and lets you change how the age is calculated or stored later without breaking the rest of the code.