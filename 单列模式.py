# 1, 可以用模块单独拿出来进行实例化
# 2， 类装饰器
# def single_function(cls):
#     obj = None
#
#     def wrapper(*args, **kwargs):
#         nonlocal obj
#         if not obj:
#             obj = cls(*args, **kwargs)
#         return obj
#
#     return wrapper
#
#
# @single_function
# class Full:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name

# 3类的绑定方法
# class Full:
#     obj = None
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     @classmethod
#     def get_single(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = cls(*args, **kwargs)
#         return cls.obj
#
#
# obj = Full.get_single('翁国添', 24)
# 4用__new__的方法
# class Full:
#     obj = None
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = super().__new__(*args, **kwargs)
#         return cls.obj
# 5用元类实现
# class Mytype(type):
#     obj = None
#
#     def __call__(self, *args, **kwargs):
#         if not self.obj:
#             self.obj = super().__call__(*args, **kwargs)
#         return self.obj
#
#
# class Full:
#     obj = None
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
