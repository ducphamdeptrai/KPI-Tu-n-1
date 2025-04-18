import random
import string

length = 10
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Mật khẩu ngẫu nhiên:", password)
