import bcrypt

password = '123456'
wann_hased = b'$2y$10$kJvELo9fqaEJe7dYN3HEee77hpez3PvhNCD11Wtj1eqNw0Mj08IVG'
knowsalt = b'$2y$10$kJvELo9fqaEJe7dYN3HEee'
test123456bcrypt= b'$2y$10$kJvELo9fqaEJe7dYN3HEeebHjupGwGybsMfo1Y7DN9LK0wbu4IDii'
###读取字典
file_name="E:\字典\weakpass_3\weakpass_3"
file_object = open(file_name)
index=0
for line in file_object.readlines(): # 依次读取每一行
    line = line.strip()    #去掉每行的头尾空白
    passwd =line
    hashedtry = bcrypt.hashpw(passwd.encode(), knowsalt)
    print('尝试次数:%d %s' %(index,passwd))
    if(hashedtry==knowsalt):   #比较字典生成的值是否正确
        print(passwd)
        break
    index += 1


# 加密过程

'''
hashed1 = bcrypt.hashpw(password.encode(), knowsalt)

print(password.encode())
print(salt)
# b'$2b$12$BlfmESsgNnsQFCmpUnhDWO'

print(hashed1)

# b'$2b$12$BlfmESsgNnsQFCmpUnhDWO2RbacoHJViT8AZR1qh3DDOHnZxB.J5q'

# 校验过程
ret = bcrypt.checkpw(password.encode(), hashed1)

print(ret) # True
'''