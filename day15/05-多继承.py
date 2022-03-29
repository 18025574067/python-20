# 定义父类Parent
class Parent(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        print("Parent的init结束被调用")


# 定义子类 Son1 -->继承 --> Parent
class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        super().__init__(name, *args, **kwargs)
        print("Son1的init结束被调用")


# 定义子类 Son2 --> 继承 --> Parent
class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print("Son2的init结束被调用")


# 定义子类 Grandson --> 继承 --> Son1 / son2
class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        # Son1.__init__(self, name, age)
        # Son2.__init__(self, name, gender)
        super().__init__(name, age, gender)
        print("Grandson的init结束被调用")


gs = Grandson("grandson", 18, "男")
print(Grandson.mro())
























