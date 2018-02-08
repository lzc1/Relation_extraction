


class Person(object):
    name = '黎明'
    gender = '男'
    def __init__(self):
        self.age = 20
        self.height = 170

    def info(self):
        print('age:',self.age,' height:',self.height)

class Student(Person):
    def __init__(self):
        super(Student,self).__init__()
        self.grade = 7

if __name__ == '__main__':
    print(Person.gender)
    p = Person()
    print(p.age)
    print(p.name)
    stu = Student()
    print(stu.grade)