filename='D:\pythonlearn\Eric\pi_million_digits.txt'
with open(filename) as file_object:
    #for line in file_object:
        #print(line.rstrip())
    #读取方法A
    #============================
    #contents=file_object.read()
    #print(contents)
    #读取方法B
    #============================
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string[:52])
print(len(pi_string))
birthday='931225'
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appears in the first million digits of pi!')
