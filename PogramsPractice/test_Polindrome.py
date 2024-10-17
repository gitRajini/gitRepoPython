# num = int(input("Enter a number: "))
# # Input: 12321
# temp = num
# reverse = 0
# while temp > 0:
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10
# if num == reverse:
#   print('Palindrome')
# else:
#   print("Not Palindrome")
# # Output: Palindrome




















num = int(input("Enter the number"))
temp = num
reverse = 0

while num > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp//10

if num == reverse:
    print("Is polindrome")
else:
    print("Not polindrome")
print("Execution Done")