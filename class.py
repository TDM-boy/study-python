class human:
    def __init__(self, name, sex, weigh):
        self.sex = sex
        self.name = name
        self.__weigh = weigh
    def print_name(self):
        print("human name:%s" % (self.name))

class humans:
    def __init__(self, name, sex, weigh):
        self.sex = sex
        self.name = name
        self.__weigh = weigh
    def print_name(self):
        print("humans name:%s" % (self.name))

class student(humans, human):
    def __init__(self, name, sex, weigh, num):
        human.__init__(self, name, sex, weigh)
        #super(student, self).__init__(name, sex, weigh)
        self.num = num
    def print_name(self):
        human.print_name(self)
        print("student name:%s" % (self.name))
    def print_sex(self) -> str:
        print("studen sex:%s" % (self.sex))
        return self.sex

A = student("XM", "boy", 60, 1)
A.print_name()
super(student, A).print_name()
print(A.print_sex())
