import hashlib

users_name = input('请输入你的账户:')
users_mima = input('请输入你的密码:')
f = open(r'/算法/记录账户密码文件.txt', mode='a')
hash_res = hashlib.sha224(users_name.encode('utf-8'))  # 加盐处理过的
hash_res.update(users_mima.encode('utf-8'))  # 只能传二进制
f.write(hash_res.hexdigest())
f.close()
