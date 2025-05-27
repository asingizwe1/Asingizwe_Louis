#Ability of different objects to take on same methods in different ways
#POLYMORPHISM
class Animal:#super/base class
    def speak(self):
        print("Animal speaks")
#child
class Eagle(Animal):#sub/derived class
    def speak(self):
        print("Eagle says: Screech!")

class falcon(Animal):#sub/derived class
    def speak(self):
        print("Eagle says: falc!")


#animal is like a placeholder for any class that inherits from Animal
def test_polymorphism(animal):
    animal.speak()  # Calls the speak method of the specific animal type


#creating objects for the different classes
eagle = Eagle()
falcon = falcon()

#calling test_polymorphism with different animal types
test_polymorphism(eagle) 
test_polymorphism(falcon) 