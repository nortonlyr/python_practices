# reference: https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/09.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E8%BF%9B%E9%98%B6.md

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 訪問器 - getter方法
    @property
    def name(self):
        return self._name

    # 訪問器 - getter方法
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} loves coding.')
        else:
            print(f'{self._name} loves reading.')


def main():
    person = Person('Peter', 22)
    person.play()
    person.age = 10
    person.play()

if __name__ == '__main__':
    main()