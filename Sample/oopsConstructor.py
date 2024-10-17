class calculator:
    num1 =100

    def __init__(self,a,b):
        self.firstNum = a
        self.secondNum = b

    def addition(self):
        print("Success")
        return self.firstNum + self.secondNum + calculator.num1


obj=calculator(3,5)
obj1=calculator(7,5)
obj2=calculator(3,1)
obj3=calculator(9,5)
obj4=calculator(3,5)
obj5=calculator(9,5)

print(obj.addition())
print(obj1.addition())
print(obj2.addition())
print(obj3.addition())
print(obj4.addition())
print(obj5.addition())
