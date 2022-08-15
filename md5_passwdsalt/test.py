from hashlib import md5
import time
start=time.time()

'''
function create_password($plaintext, $salt)
{
    $salt = md5('y' . $salt . 'x');
    $salt .= '2020';
    return md5($plaintext . $salt);
}
'''
def encode_md5_pwdsalt(pwd, salt):
    md5_pwd = md5()
    md5_pwd.update((str(pwd) + salt).encode("utf-8"))  # md5.update  会将每次字符串拼接
    return md5_pwd.hexdigest()

def encode_md5_pwd(pwd):
    md5_pwd = md5()
    md5_pwd.update(pwd.encode("utf-8"))
    return md5_pwd.hexdigest()


pwd = '123456'
wana_md5='631c976b5e2e456a77a6a50931c578a0'
salt1= '70c7'   #4位salt
print(salt1)
md5_pwd=encode_md5_pwdsalt(pwd,encode_md5_pwd('y'+salt1+'x')+'2020')  ###加密后的值32位
print(md5_pwd)