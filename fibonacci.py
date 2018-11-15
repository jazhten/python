def nth_fib(num):
    if num ==1 or num ==2 :
        return 1
    first =1
    second =1
    third =1
    for i in range(2,num):
        first = second
        second = third
        third = second + first
    return third


nth = int(input("How many fibonacci numbers to generate:"))

list = [nth_fib(i) for i in range(1,nth)]

print(list)

