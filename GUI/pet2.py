#Class

class Pet():
    name = None
    fullness = 0

    def __init__(self, name):
        self.name = name

    def eat(self,food):
        print(self.name + " is eating " + food + "... ")
        if food == "carrots":
            self.fullness = self.fullness + 10
        elif food == "grass":
            self.fullness = self.fullness + 3
        elif food == "water":
            self.fullness = self.fullness + 1

        print(self.name, + "is now" + self.fullness, + "percent full")

# Start of Program
        
pet_owner_name = input("What is your name?")
print("Welcome,", pet_owner_name)

pet_1 = Pet("Rocky")
