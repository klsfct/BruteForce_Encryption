import bcrypt
########此程序为验证工具
passwd = '123456'
wann_hased = b'$2y$10$9BfmW1FQguCZsNDcXdO.SOYO2tV/t3ZWMLed3KJ7f5rGxG3039Ya6'
knowsalt = b'$2y$10$9BfmW1FQguCZsNDcXdO.SO'
test123456bcrypt= b'$2y$10$kJvELo9fqaEJe7dYN3HEeebHjupGwGybsMfo1Y7DN9LK0wbu4IDii'
###读取字典
file_name="E:\Security\Cracer渗透工具包v3.0\Cracer渗透工具\字典生成\自己收集和组合的字典\破解字典\超级字典\超级字典.txt"
file_object = open(file_name)
index=0
for line in file_object.readlines(): # 依次读取每一行
    line = line.strip()    #去掉每行的头尾空白
    salt = bcrypt.gensalt(rounds=10)  # $10$

    hashedtry = bcrypt.hashpw(passwd.encode(), salt)
    print('尝试次数:%d bcrypt值%s' %(index,hashedtry))

    index += 1


