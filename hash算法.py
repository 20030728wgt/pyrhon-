import hashlib

while True:
    users_names = input('请输入你的账户:')
    users_mimas = input('请输入你的密码:')
    res_new = hashlib.sha224(users_mimas.encode('utf-8'))
    res_new.update(users_mimas.encode('utf-8'))
    with open(r'/算法/记录账户密码文件.txt', mode='r') as f:
        content = f.readline()
        if content == res_new.hexdigest():
            print('登录成功')
            f.close()
            break
        else:
            print('密码错误')
