class Full:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 100:
            print('输入错误')
            return
        else:
            self.__age = new_age

    @age.deleter
    def age(self):
        del self.__age

    # age = property(get_age,set_age,delete_age)  # 放入函数顺序必须是查，改，删可以用语法糖


full1 = Full('A货', 16)
print(full1.age)
print(full1.get_name())
full1.age = 12
print(full1.age)
