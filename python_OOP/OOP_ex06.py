from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """Pet"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """make sound"""
        pass

class Dog(Pet):
    """dog"""
    def make_voice(self):
        print(f'{self._nickname}: woo, woo, woo....')

class Cat(Pet):
    """cat"""
    def make_voice(self):
        print(f'{self._nickname}: mia, mia, mia....')

def main():
    pets = [Dog('旺財'), Cat('Kitty'), Dog("Jacky")]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()