class Expression:
    def __init__(self, num1, num2, num3):
        self.number1 = num1
        self.number2 = num2
        self.number3 = num3
    
    def addition(num1, num2, num3):
        sum = num1 + num2 + num3
        print(f"{num1} + {num2} + {num3} = {sum}")

Expression.addition(3, 19, 12)