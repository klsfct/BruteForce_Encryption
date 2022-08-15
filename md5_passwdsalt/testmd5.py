#哥你明天跑下这条631c976b5e2e456a77a6a50931c578a0:70c7  这条是我猜出来的一个密码，但是刚用程序无法跑出来

from hashlib import md5
import time


def encode_md5_pwdsalt(pwd, salt):
    md5_pwd = md5()
    md5_pwd.update((str(pwd) + salt).encode("utf-8"))  # md5.update  会将每次字符串拼接
    return md5_pwd.hexdigest()

def encode_md5_pwd(pwd):
    md5_pwd = md5()
    md5_pwd.update(pwd.encode("utf-8"))
    return md5_pwd.hexdigest()


pwd = '123456'
salt1= '70c7'   #4位salt
salt1= 'y'+salt1+'x'+'2020'
print(salt1)
md5_pwd=encode_md5_pwdsalt(pwd,salt1)  ###加密后的值32位
print(md5_pwd)
print(len(md5_pwd))
print(encode_md5_pwd(pwd))
print(len("631c976b5e2e456a77a6a50931c578a0"))
