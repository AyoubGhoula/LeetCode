from collections import Counter
nums=[0,0,1,1,1,1,2,3,3]
dic=Counter(nums)
print(dic)
list_val=list(dic.values())
pop_ele=list(dic.keys())[0]
print(pop_ele)
print(list_val)
while list_val[0]>list_val[1]:
    print(list_val[0])
    nums.pop(nums.index(pop_ele))
    list_val[0]-=1
print(nums)
max_c=0
ind=0
set_nums=set(nums)
for i in set_nums :
    if nums.count(i)>max_c:
        max_c=nums.count(i)
        ind=i
np_ele=0
for i in set_nums:
    if nums.count(i)>np_ele and i != ind:
       np_ele=nums.count(i)
for i in range(np_ele):
    nums.pop(nums.index(ind))
print(nums)
nums=[0,0,1,1,1,1,2,3,3,3]
for i in set(nums):
    while nums.count(i)>2:
        nums.pop(nums.index(i))
print(nums)
nums=[6,5,5]
dic=Counter(nums)
print(dic)
print(dic.most_common())
value, count = dic.most_common()[0]
print(value)
