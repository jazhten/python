def first_digit(list):
    return int(list[0])

def last_digit(list):
    length = len(list)-1
    return int(list[length])
list1 = [5,10,15,20,25]
list2 =[first_digit(list1),last_digit(list1)]
print(list2)
