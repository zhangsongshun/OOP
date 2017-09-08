class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_student(self):
        return '%s:%s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score
student_list = []
a = Student('li', 92)
b = Student('xu', 94)
c = Student('wu', 96)
student_list.append(a)
student_list.append(b)
student_list.append(c)
for i in student_list:
    print(i.print_student())