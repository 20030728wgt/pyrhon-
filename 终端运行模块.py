import subprocess

obj = subprocess.Popen('tree',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
res = obj.stdout.read()
print(res.decode('gbk'))
