import itertools as its
import string
import time
import re

start=time.time()


alpha_all = string.ascii_letters
num = string.digits
special = string.punctuation
words=alpha_all+num+special
print(words)
r = its.product(words,repeat=2)
dic = open("pass1.txt","a")
print(r)
printTip = "密码强度："
for i in r:
    oneline = "".join(i)
    m1 = re.search(r'\d+', oneline)
    m2 = re.search(r'[a-z]+', oneline, re.I)
    m3 = re.search(r'[^a-z0-9]+', oneline, re.I)
    print(m1)
    if m1 and m2 and m3:
        printTip = printTip + "强。"+oneline
    else:
        printTip = printTip + "中。"+oneline

    if(re.match("^(?![A-Za-z]+$).$",str(oneline))==None):

        print(str(oneline))
        dic.write("".join(i))   # jion空格链接
        dic.write("".join("\n"))
     #   print(i)
dic.close()

end=time.time()

print('Running time: %s Seconds'%(end-start))