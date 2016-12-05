#!/usr/bin/python  
# -*- coding: utf-8 -*-  
####课上的
user = raw_input('user:')
pwd = raw_input('pwd:')
f = open('/home/wangyw/1.txt')
arr = f.read().split('\n')
#print arr
f.close

user_exists = False
for u in arr:
    temp = u.split(':')
#    print temp
    if temp[1] == user or temp[0] == user:
        if temp[2] == pwd:
            msg = 'login success'
        else:
            msg = 'pwd wrong'
        user_exists = True
        print msg
        break
if not user_exists:
    print 'user not exits'
