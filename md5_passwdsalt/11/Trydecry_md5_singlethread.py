import itertools as its
import queue
import string
import threading
import time
import re
from hashlib import md5
from tqdm import tqdm
start=time.time()


alpha_all = string.ascii_letters
num = string.digits
special = string.punctuation
words=alpha_all+num+special
#words=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#派出了回车换行字符
print(words)
#time.sleep(20)
###
def encode_md5_pwdsalt(pwd, salt):
    md5_pwd = md5()
    md5_pwd.update((str(pwd) + salt).encode("utf-8"))  # md5.update  会将每次字符串拼接
    return md5_pwd.hexdigest()
def encode_md5_pwd(pwd):
    md5_pwd = md5()
    md5_pwd.update(pwd.encode("utf-8"))
    return md5_pwd.hexdigest()

####下面这两个是要填写的东西，其他东西不用修改
# salt1= '70c7'   #4位salt
# wana_decodestr="631c976b5e2e456a77a6a50931c578a0"
#16b48558acfda39108bc04f305002068:8e70
# b786420f34cd38cb33d829f99fa74075:e705
# 6147eb5576ddcbfece68e95e4e96d24a:23de

salt1= '8e70'
wana_decodestr1='16b48558acfda39108bc04f305002068'
salt2='e705'
wana_decodestr2='b786420f34cd38cb33d829f99fa74075'
salt3='23de'
wana_decodestr3='6147eb5576ddcbfece68e95e4e96d24a'
##
pwd = '123456'
md5_pwd=encode_md5_pwdsalt(pwd,encode_md5_pwd('y'+'70c7'+'x')+'2020')  ###加密后的值32位
print(md5_pwd)
print(len(md5_pwd))
# time.sleep(20)
#哥你明天跑下这条631c976b5e2e456a77a6a50931c578a0:70c7  这条是我猜出来的一个密码，但是刚用程序无法跑出来
####直接生成位数并且decry
#单条破解
def is_vaild(oneline:str):#生成的字典是否有效
    try:
        passwd = oneline
        print(passwd)
        if (encode_md5_pwdsalt(str(passwd), encode_md5_pwd('y' + salt1 + 'x') + '2020') == wana_decodestr1):
            print("破解成功", passwd)
            dic = open("破解成功.txt", "w+")
            dic.write(passwd)
            dic.close()
            global flag
            flag = False
    except:
        return



def password_list():
    for pwd in r:
        yield(''.join(pwd))
        # print(''.join(pwd))



flag=True
total=len(words) **5
for weishu in range(5,6):
    print(weishu)
    r= its.product(words,repeat=weishu)
    print(weishu)
    threads=[]
    # for pwd in r:
    #     oneline=(''.join(pwd))
    #     print(oneline)
    for pwd in tqdm(password_list(),total=total):
        threads.append(threading.Thread(target=is_vaild,args=(pwd)))
    for thread in threads:
        if flag:
            thread.start()
            thread.join()






        # if(re.match("^(?:(?=.*[a-zA-Z])(?=.*[0-9])).{%d}$" %weishu,str(oneline))!=None):
        #     # re.mateh更快，匹配含有字母+数字6-20位
        #     # print(str(oneline))
        #     passwd = oneline
        #     md5_pwd1 = encode_md5_pwdsalt(str(passwd), encode_md5_pwd('y' + salt1 + 'x') + '2020')
        #     # print('尝试次数:%d %s %s' % (index, passwd, md5_pwd1))
        #     if (md5_pwd == wana_decodestr1):
        #         print("破解成功", passwd)
        #         break
        #     index += 1
        #     # print("便利一般")




end=time.time()

print('Running time: %s Seconds'%(end-start))

