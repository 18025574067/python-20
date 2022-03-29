class Parent(object):
    def __init__(self, name):
        self.name = name
        print("Parent的init结束被调用")


class Son1(Parent):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
        print("Son1的init结束被调用")


class Grandson(Son1):
    def __init__(self, name, age, gender):
        self.gender = gender
        super().__init__(name, age)
        print("Grandson的init结束被调用")


gs = Grandson("grandson", 12, "男")
print(Grandson.__mro__)
print("姓名", gs.name)
print("年龄", gs.age)
print("性别", gs.gender)


