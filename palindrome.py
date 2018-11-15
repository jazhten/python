word = input("Enter string: ")

n_word = word.lower()

def reverse(s):
    return s[::-1]

if n_word == reverse(n_word):
    print(word + " is a palindrome")

else:
    print(word + " is not a palindrome")

