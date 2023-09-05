# coding: utf-8
# @Author: 小飞有点东西
# Learning_address: https://v.ixigua.com/2asfSbf/


# 封装、继承、多态
# 封装：整合
# 隐藏属性
# 1、隐藏的本质，只是一种改名操作2
# 2、对外不对内
# 3、改名操作，只会在类的定义阶段检查子代码语法的时候执行一次，之后定义的__开头的属性，都不会改名

# class Test:
#     __x = 10    # _Test__x
#
#     def __f1(self): # _Test__f1
#         print('f1')
#
#     def f2(self):
#         print(self.__x)
#         print(self.__f1)
#
#
# Test.__y = 20
# obj = Test()
# print(obj._Test__x)
# print(obj._Test__f1)
# obj.f2()

# print(Test.__dict__)


# class Test:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     @property   # get_age = property(get_age)
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         if type(new_age) is not int:
#             print('你个傻子，必须传整型！')
#             return
#
#         if not 0 <= new_age <= 150:
#             print('你个傻子，年龄必须在0-150岁！')
#             return
#
#         self.__age = new_age
#
#     @age.deleter
#     def age(self):
#         del self.__age

# age = property(get_age, set_age, del_age)


# obj = Test('xxx', 18)
# print(obj.name, obj.age)
# print(obj.get_name())
# print(obj.age)
# obj.age = 20
# print(obj.age)
# del obj.age
# print(obj.age)

# print(obj.get_age)

# print(property)


# class Servant:
#
#     def __run(self):
#         print('跑起来')
#
#     def __pay(self):
#         print('给钱')
#
#     def __take_bun(self):
#         print('拿包子')
#
#     def buy_bun(self):  # 买包子
#         self.__run()
#         self.__pay()
#         self.__take_bun()
#         self.__run()
#
#
# ser = Servant()
# ser.buy_bun()
# ser.


# 继承：创建新类的方式，通过继承创建的类称之为子类，被继承的类称之为父类（基类）
# class Parent1(object):
#     x = 10
#     pass
#
#
# class Parent2(object):
#     pass
#
#
# class Child1(Parent1):  # 单继承
#     pass
#
#
# class Child2(Parent1, Parent2):  # 多继承
#     pass


# print(Parent1.__bases__)
# print(Parent2.__bases__)
# print(Child1.__dict__)

# 在Python2里面，有新式类和经典类的区分
# 新式类：继承了object类的子类，以及继承了这个子类的子子孙孙类
# 经典类：没有继承object类的子类，以及继承了这个子类的子子孙孙类

# 继承的特性：遗传

# 多继承
# 优点：一个子类可以同时遗传多个父类的属性
# 缺点：
# 1、多继承违背了人的思维习惯
# 2、多继承会让代码的可读性变差
# 如果必须用多继承，应该用Mixins

# class Human:
#     star = 'earth'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Chinese(Human):
#     # star = 'earth'
#     nation = 'China'
#
#     def __init__(self, name, age, gender, balance):
#         Human.__init__(self, name, age, gender)
#         self.balance = balance
#
#     def speak_chinese(self):
#         print(f'{self.name}在说普通话')
#
#
# class American(Human):
#     star = 'earthxxx'
#     nation = 'America'
#
#     # def __init__(self, name, age, gender):
#     #     self.name = name
#     #     self.age = age
#     #     self.gender = gender
#
#     def speak_english(self):
#         print(f'{self.name}在说英语')
#
#
# dy_obj = Chinese('董永', 18, '男', 1000)
# print(dy_obj.__dict__)
# print(dy_obj.nation)
# print(dy_obj.star)
# dy_obj.speak_chinese()
#
# iron_man_obj = American('iron_man', 19, '男')
# print(iron_man_obj.__dict__)
# print(iron_man_obj.nation)
# print(iron_man_obj.star)
# iron_man_obj.speak_english()


# 属性查找
# 对象-类-父类-.....object
# class Test1:
#     def __f1(self): # _Test1__f1
#         print('Test1.f1')
#
#     def f2(self):
#         print('Test1.f2')
#         self.__f1() # _Test1__f1
#
#
# class Test2(Test1):
#     def __f1(self): # _Test2__f1
#         print('Test2.f1')
#
#
# obj = Test2()
# obj.f2()


# 多继承属性查找
# 菱形问题（钻石问题）

# MRO列表，C3算法实现
# class A:
#     def f1(self):
#         print('A.f1')
#
#
# class B(A):
#     def f1(self):
#         print('B.f1')
#
#
# class C(A):
#     def f1(self):
#         print('C.f1')
#
#
# class D(B, C):
#     def f2(self):
#         print('D.f2')
#
#
# print(D.mro())
#
# obj = D()
# obj.f1()


# 非菱形继承
# class A:
#     def f2(self):
#         print('A.f1')
#
#
# class B:
#     def f1(self):
#         print('B.f1')
#
#
# class C(A):
#     def f2(self):
#         print('C.f1')
#
#
# class D(B):
#     def f1(self):
#         print('D.f1')
#
#
# class E:
#     def f1(self):
#         print('E.f1')
#
#
# class F(C, D, E):
#     def f2(self):
#         print('F.f2')
#
#
# # print(F.mro())
#
# obj = F()
# obj.f1()


# 菱形继承
# 经典类：深度优先查找，找第一条分支的时候，就要找共同的父类
# 新式类：广度优先查找，找完最后一条分支之后，才找共同的父类
# class Z:
#     def f1(self):
#         print('Z.f1')
#
#
# class A(Z):
#     def f2(self):
#         print('A.f1')
#
#
# class B(Z):
#     def f2(self):
#         print('B.f1')
#
#
# class C(A):
#     def f2(self):
#         print('C.f1')
#
#
# class D(B):
#     def f2(self):
#         print('D.f1')
#
#
# class E(Z):
#     def f2(self):
#         print('E.f1')
#
#
# class F(C, D, E):
#     def f2(self):
#         print('F.f2')
#
#
# print(F.mro())
#
# obj = F()
# obj.f1()


#
# 注意：
# 1、继承结构不要太复杂
# 2、满足什么 “是” 什么的关系

# MixIns机制
# MixIn able ible
# class Fowl:  # 家禽类
#     pass
#
# class SwimMixIn:
#     def swimming(self):
#         pass
#
# class Chicken(Fowl):  # 鸡
#     pass
#
# class Duck(SwimMixIn, Fowl):  # 鸭
#     pass
#
# class Goose(SwimMixIn, Fowl):  # 鹅
#     pass
#
# # import socketserver
#
# # 什么 “是” 什么的关系
# # 'is-a'关系


# class Human:
#     star = 'earth'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Chinese(Human):
#     nation = 'China'
#
#     def __init__(self, name, age, gender, balance):
#         # Human.__init__(self, name, age, gender)
#         # super(Chinese, self).__init__(name, age, gender)
#         super().__init__(name, age, gender)
#         self.balance = balance
#
#     def speak_chinese(self):
#         print(f'{self.name}在说普通话')
#
#
# obj = Chinese('大仙', 18, 'female', 2500)
# print(Chinese.mro())
# print(obj.__dict__)


# class A:
#     def f1(self):
#         print('A.f1')
#         super().f1()
#
# class B:
#     def f1(self):
#         print('B.f1')
#
# class C(A, B):
#     pass
#
# obj = C()
# obj.f1()
# print(C.mro())


# 多态
# 汽车：奔驰、理想、奥拓
# class Car:
#     def run(self):
#         print('开始跑', end=' ')
#
# class Benz(Car):
#     def run(self):
#         super().run()
#         print('加98号汽油')
#
# class Lx(Car):
#     def run(self):
#         super().run()
#         print('充电')
#
# class Auto(Car):
#     def run(self):
#         super().run()
#         print('加92号汽油')
#
# car1 = Benz()
# car2 = Lx()
# car3 = Auto()
# car1.run()
# car2.run()
# car3.run()
#
# def drive_car(car):
#     car.run()
#
# drive_car(car1)
# drive_car(car2)
# drive_car(car3)


# print('abc'.__len__())
# print([1, 2, 3].__len__())
# print({'a': 1, 'b': 2}.__len__())

# def my_len(obj):
#     return obj.__len__()
#
# print(my_len('abc'))
# print(my_len([1,2,3]))
# print(my_len({'a':1,'b':2}))
# __iter__()
# for


# class Car:
#     def run(self):
#         print('开始跑', end=' ')

# class Benz:
#     def run(self):
#         print('加98号汽油')
#
# class Lx:
#     def run(self):
#         print('充电')
#
# class Auto:
#     def run(self):
#         print('加92号汽油')
#
# car1 = Benz()
# car2 = Lx()
# car3 = Auto()
# car1.run()
# car2.run()
# car3.run()

# 鸭子类型
# linux：一切皆文件

# class Disk:
#     def read(self):
#         print('Disk.read')
#
#     def write(self):
#         print('Disk.write')
#
# class Memory:
#     def read(self):
#         print('Memory.read')
#
#     def write(self):
#         print('Memory.write')
#
# class Txt:
#     def read(self):
#         print('Txt.read')
#
#     def write(self):
#         print('Txt.write')

# 抽象基类
# import abc
#
# class Car(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def run(self):
#         pass
#
#
# class Benz(Car):
#     def run(self):
#         pass
#
# class Lx(Car):
#     def run(self):
#         pass
#
# class Auto(Car):
#     def run(self):
#         pass
#
# car1 = Benz()
# car2 = Lx()
# car3 = Auto()
# car1.run()
# car2.run()
# car3.run()