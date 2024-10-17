from oopsConstructor import calculator


class child(calculator):
    num = 100

    def __init__(self):
        calculator.__init__(self,5,5)

    def getdata(self):
        return self.firstNum + self.secondNum + self.num + self.num1

obj = child()
print(obj.getdata())

obj1=child()
obj1.addition()
