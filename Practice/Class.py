class Person:
    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def get_name(self):
        return self.name
    
    def set_name(self, name:str):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        return self.age
    
    def copy(self):
        new=Person(self.name, self.age, self.address, self.phone_number)
        return new
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nPhone number: {self.phone_number}"


maria = Person("Maria", 25, "Tomares", 672)
print(maria)

copy= maria.copy()
copy.age= 30
print(copy.age)
print(maria.age)





