mylist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
time=1
for i in mylist:
    if time == 1:
        max = i
        time+=1
        continue
    if i >= max:
        max = i
#print max

time=1
for i in mylist:
    if time == 1:
        second_max = i
        time+=1
        continue
    if i == max:
        continue
    if  second_max  <= i  <= max:
        second_max = i
#print second_max   
print  max + second_max       
