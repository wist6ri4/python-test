import secrets

# 英字小文字
lowercase = "abcdefghijklmnopqrstuvwxyz"
# 英字大文字
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 数字
numbers = "1234567890"
# ASCII記号
symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
# パスワードの長さ
length = 32

all_chars = lowercase + uppercase + numbers + symbols

# print
password = ""

for _ in range(length):
    char = secrets.choice(all_chars)
    password += char

print(f"\n{password}\n")