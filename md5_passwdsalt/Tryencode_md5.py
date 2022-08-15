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
md5_pwd=encode_md5_pwdsalt(pwd,encode_md5_pwd('y'+salt1+'x')+'2020')  ###加密后的值32位
print(md5_pwd)
print(len(md5_pwd))

#哥你明天跑下这条631c976b5e2e456a77a6a50931c578a0:70c7  这条是我猜出来的一个密码，但是刚用程序无法跑出来
start =time.time()
wana_decodestr="631c976b5e2e456a77a6a50931c578a0"
#file_name="E:\Security\Cracer渗透工具包v3.0\Cracer渗透工具\字典生成\自己收集和组合的字典\破解字典\超级字典\超级字典.txt"
file_name="../generate_dict/4位数pass.txt"

file_object = open(file_name)
index=0


for line in file_object.readlines(): # 依次读取每一行
    line = line.strip()    #去掉每行的头尾空白
    passwd =line
    md5_pwd=encode_md5_pwdsalt(str(passwd),encode_md5_pwd('y'+salt1+'x')+'2020')
    ###加密后的值32位
    print('尝试次数:%d %s %s' %(index,passwd,md5_pwd))
    if(md5_pwd==wana_decodestr):
        print("破解成功",passwd)
        break
    index += 1

end=time.time()

print('Running time: %s Seconds'%(end-start))