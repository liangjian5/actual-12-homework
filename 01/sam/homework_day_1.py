#coding=utf-8
frist_big_num = 0
second_big_num = 0
for num in [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]:
	if frist_big_num < num:
		frist_big_num = num

for num in [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]:
	if second_big_num < num and second_big_num < frist_big_num:
		second_big_num = num
print frist_big_num,second_big_num
