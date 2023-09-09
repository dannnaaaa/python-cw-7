class person :
    name = "john"
    age = 22

    def is_adult (self):
        if self.age > 18:
            print("You have too much responsibilities")

        else:
            print("lucky")


first_person = person()
print(person.name)
print(person.age)
first_person.is_adult()


class person2:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name} , and I am {self.age} years old . "
    

second_person = person2('Anwar', 25)
print(second_person)