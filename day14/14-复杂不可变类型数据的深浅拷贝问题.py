import copy


def copy_test():
    A = [1, 2, 3]
    B = [11, 22, 33]

    # 定义元组
    C = (A, B)
    print("C= ", C, id(C))

    # 复杂不可变类型的浅拷贝
    D = copy.copy(C)
    print("D= ", D, id(D))
    print("D[0]= ", id(D[0]), "C[0]= ", id(C[0]), "A=", id(A))

    D[0][0] = 10
    print("D= ", D, id(D))


A = [1, 2, 3]
B = [11, 22, 33]

# 定义元组
C = (A, B)
print("C= ", C, id(C))

# 对C做深拷贝
D = copy.deepcopy(C)
print("D= ", D, id(D))
print("D[0]= ", id(D[0]), "C[0]= ", id(C[0]), "A=", id(A))
# D拷贝自C，也是不可变的，D[0]是一个列表，是可变的，可以通过D[0][0]修改值
# D[0] = [10, 20, 30]
D[0][0] = 10

print("C= ", C, id(C))
print("D= ", D, id(D))

