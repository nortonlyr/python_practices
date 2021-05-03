class Person(object):
    """person"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self.age = age

    def play(self):
        print(f'{self._name} is playing')

    def watch_tv(self):
        if self._age >= 18:
            print(f'{self._name} can watching romantic drama.')
        else:
            print(f"{self._name} can't watch.")


class Student(Person):
    """Student"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self._grade}的{self._name}正在學習{course}')


class Teacher(Person):
    """teacher"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f'{self._name}{self._title}正在講{course}')


def main():
    stu = Student('張三', 15, '高一')
    stu.study('數學')
    stu.watch_tv()
    t = Teacher('老王', 40, '教授')
    t.teach('Python面嚮對象設計')
    t.watch_tv()

if __name__ == '__main__':
    main()