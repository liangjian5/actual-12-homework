#coding=utf-8
a=0
b=0
num=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in num:
    if i>a:
        a=i
for x in num:
    if x>b and x!=a:
        b=x
print a,b
