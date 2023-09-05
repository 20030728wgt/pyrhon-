import configparser

config = configparser.ConfigParser()
config.read(r'E:\桌面\wgt python\文件处理\test.ini', encoding='utf-8')
print(config.sections())
print(config.options('name'))
print(config.items('name'))
delay = config.get('name', 'name1')
print(delay)

