"""
简单学生类
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_av(self):
        if self.age >= 18:
            print('%s正在看岛国' % self.name)
        elif self.age < 18:
            print('%s只能看熊出没' % self.name)


def main():
    stu1 = Student('胡斐', 23)
    stu1.study('Python设计')
    stu1.watch_av()

    stu2 = Student('菜花', 17)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()
