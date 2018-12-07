str_input = input("Enter string: ")

result = str_input.split()
result = result[::-1]
result = " ".join(result)

print(result)
