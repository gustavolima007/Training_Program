name = input('What is you name?\n')
passwd = input('Put your password: \n')

name_len = len(name)
passwd_len = len(passwd)

hidden_password = passwd_len * '*'

print(f'{name}, your password {hidden_password} is {passwd_len} letters long')
