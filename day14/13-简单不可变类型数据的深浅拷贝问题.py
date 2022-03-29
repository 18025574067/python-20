import copy


def test_copy():
    # 简单不可变的元组
    tuple1 = (1, 2, 3)
    print("tuple1= ", tuple1, id(tuple1))

    # 简单不可变类型的浅拷贝
    # 等价于tuple2 = tuple1
    tuple2 = copy.copy(tuple1)
    print("tuple2= ", tuple2, id(tuple2))


# 简单不可变的元组
tuple1 = (1, 2, 3)
print("tuple1= ", tuple1, id(tuple1))

tuple2 = copy.deepcopy(tuple1)
print("tuple2= ", tuple2, id(tuple2))

