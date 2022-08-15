import itertools as its
import string
import time
import re

start=time.time()


alpha_all = string.ascii_letters
num = string.digits
special = string.punctuation
words=alpha_all+num+special
#words=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#派出了回车换行字符
print(words)
#time.sleep(20)
weishu=6
r = its.product(words,repeat=weishu)  #这个地方设置几位数，生成几位数字典
dic = open("%d位数pass.txt" %weishu,"w")
print(r)

for i in r:
    oneline = "".join(i)
    # m1 = re.search(r'\d+', oneline)   #是否含有数字  re.search 找不到返回none
    # m2 = re.search(r'[a-z]+', oneline, re.I)   #含有字母
    # m3 = re.search(r'[^a-z0-9]+', oneline, re.I)  #匹配含有特殊字符的

    #这里要求数字+字母或者符号  m1 and m2 成立即可
    # if m1 and m2 :
    #     print( "强。"+oneline)
    # else:
    #     print( "弱。"+oneline)
    if(re.match("^(?:(?=.*[a-zA-Z])(?=.*[0-9])).{%d}$" %weishu,str(oneline))!=None):
        #re.mateh更快，匹配含有字母+数字
        print(str(oneline))
        dic.write("".join(i))   # jion空格链接
        dic.write("".join("\n"))
     #   print(i)
dic.close()

end=time.time()

print('Running time: %s Seconds'%(end-start))

###
'''
lengths=8
dictionaries=words
for i in range(len(lengths)):
    r = its.product(dictionaries, repeat=lengths[i])
    for pwd in tqdm(password_list(), total=total):
        if extract(zfile, pwd):
            break
'''