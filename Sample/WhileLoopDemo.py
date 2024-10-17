num=5
while num>1:
    print(num)
    num = num - 1

print("***** if Condition")
num1=5
while num1 >1:
    if num1!=3:
        print(num1)
    num1 = num1-1

print("****** Break")
num1=5
while num1 >1:
    if num1==3:
        break
    print(num1)
    num1 = num1-1

print("***** Continue statement")
num2 =10
while num2 > 1:
    if num2 == 5:
        num2 = num2 - 1
        continue
    print(num2)
    num2 = num2 -1
