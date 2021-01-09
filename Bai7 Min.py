import random

n = int(input('Nhập n :'))
list = random.sample(range(0,100),n)
min = list[0]
for item in list:
    if item < min :
        min = item
print('List = ',list)
print('Min là :',min)