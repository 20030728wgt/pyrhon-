class Full:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)

    def interact(self):
        opt = input('>>>')
        if hasattr(self, opt):
            getattr(self, opt)()  # 可以传递第三个参数表示如果没有就执行第三个参数内容
        else:
            print('没有这个功能')


id1 = Full('wgt', '30')
id1.interact()
