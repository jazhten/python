import random

#this could also be used to show/test Pigeon hole principle

len1 = int(input('Enter length of the first list: '))
len2 = int(input('Enter length of the second list: '))

list1 = random.sample(range(100),len1)
list2 = random.sample(range(100),len2)

print('list one :' + str(list1))
print('list two :' + str(list2))

listcommon = [i for i in list1 if i in list2]

listcommon.sort()

print('Common numbers are : ' + str(listcommon))
