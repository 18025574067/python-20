import copy


def test():
    A = [1, 2, 3]
    B = [11, 22, 33]
    C = [A, B]
    # [[1, 2, 3], [11, 22, 33]]

    print("A= ", A, id(A))
    print("B= ", B, id(B))
    print("C= ", C, id(C))
    print("C[0]= ", C[0], id(C[0]))

    # 对复杂可变类型的浅拷贝
    # 对C做浅拷贝
    D = copy.copy(C)
    print("D=", D, id(D))
    print("D[0]= ", D[0], id(D[0]))

    # 修改A的值
    A[0] = 10
    print("A= ", A, id(A))
    print("D[0]= ", D[0], id(D[0]))


A = [1, 2, 3]
B = [11, 22, 33]
C = [A, B]
# [[1, 2, 3], [11, 22, 33]]

print("A= ", A, id(A))
print("C= ", C, id(C))
# print("C[0]= ", C[0], id(C[0]))

# 对C做深拷贝
D = copy.deepcopy(C)
print("D= ", D, id(D))
# print("D[0]= ", D[0], id(D[0]))
# print("D[0]= ", id(D[0]), "C[0]= ", id(C[0]), "A= ", id(A))

A[0] = 10
print("D[0]= ", id(D[0]), "C[0]= ", id(C[0]), "A= ", id(A))
print(A, C, D)
