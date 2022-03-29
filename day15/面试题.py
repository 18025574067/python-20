class A(object):
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print("B")


class C(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")


d = D()
print(D.__mro__)
# D, B, C, A
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)







