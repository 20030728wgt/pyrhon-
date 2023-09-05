class type1(type):
    def __init__(cls, class_name, class_bases, class_dic):  # 初始化类
        super().__init__(cls)
        if '_' in class_name:
            raise NameError('名字不能有下划线')
        if not class_dic.get('__doc__'):
            raise SyntaxError('要有文档')

    def __new__(cls, *args, **kwargs):  # 造类
        return super().__new__(cls, *args, **kwargs)

    # def __call__(cls, *args, **kwargs):  # 返回对象
    #     full_obj = cls.__new__(cls)
    #     cls.__init__(full_obj, *args, **kwargs)
    #     return full_obj


class Full(object, metaclass=type1):
    """
    hhh
    """

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)


obj = Full('wgt', 23)
print(obj.get_name())
