def login():
    print('登录功能')


def scan():
    print('扫码支付')


def transfer():
    print('转账支付')


func_dic = {'0': [login, '登录功能'],
            '1': [scan, '扫码支付'],
            '2': [transfer, '转账支付']}
while 1:
    print("-"*30)
    for key in func_dic:
        print(key, func_dic[key][1])
    opt = input('请输入要运行的数字:')
    if opt not in func_dic:
        print('此功能不存在')
        continue
    func_dic[opt][0]()
