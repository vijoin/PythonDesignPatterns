# an animal makes its sound in the forest just by passing as a parameter,
# and not by specifying the class.
# It makes easier to call the make_sound method independently from the type of animal
# and easier to add new animals
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Cat(Animal):
    def do_say(self):
        return "I'm a Cat and I say Meaow!!!"


class Dog(Animal):
    def do_say(self):
        return "I'm a Dog and I say Bhow!!!"


# Simply add a new animal here and implement the do_say() method
class Lion(Animal):
    def do_say(self):
        return "I'm a Lion and I say Roar!!!"


class ForestFactory(object):
    def make_sound(self, object_type):
        try:
            return eval(object_type)().do_say()
        except NameError:
            return f"Error 404: {object_type} not found"


if __name__ == "__main__":
    ff = ForestFactory()
    animal = input("Which animal would you like to make the sound?")
    animal_classname_format = animal.title().replace(' ', '') 
    print(ff.make_sound(animal_classname_format))
    print("\nBye.")