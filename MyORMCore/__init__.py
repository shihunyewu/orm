# -*-coding:utf-8 -*-
"""
试验元类
"""

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        """
        :param cls: 当前准备创建的类的对象
        :param name: 类的名字
        :param bases: 类继承的父类集合
        :param attrs: 类的方法集合
        :return:
        """
        attrs['add'] = lambda self, value: self.append(value) # 使用匿名函数表达式
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    """
    当传入关键字参数 metaclass 时
    这指示 Python 解释器在创建MyList时
    要通过 ListMetaclass.__new__() 来创建
    :param list: 父类，python 中是支持多继承的
    """
    pass


if __name__ == '__main__':
    L = MyList()
    L.add(1)
    print(L[0])
    pass
