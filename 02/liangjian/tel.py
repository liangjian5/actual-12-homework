#coding=utf-8

f = open('user.txt')
arr = f.read().split('\n')
f.close()
user = '1111'
pwd = 'pwd'
user_exists = False
for i in arr:
     temp = i.split(':')
     if temp[1] == user or temp[0] == user:
         if temp[2] == pwd:
             msg = 'success!'
         else:
             msg = 'wrong pwd'
         user_exists = True
         print msg
         break
if not user_exists:
     print 'no user exists'

# f = open(文件地址)，返回一个文件描述符
# f.read() 读取文件所有内容
# # f.readline() 读取一行
# f.close() 关闭文件