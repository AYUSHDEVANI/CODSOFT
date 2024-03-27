from termcolor import colored

class FormatInput:

    def __init__(self):
        self.expression = input(colored("Enter expression in pattern 'num_1 opertaor num_2': ","cyan"))

    def format_exp(self):
        exp = self.expression.split(" ")
        try:
            val1 = float(exp[0])
            val2 = float(exp[2])
            opr = exp[1]
            return val1, val2, opr
 
        except ValueError:
            print(colored("Got anything other than numbers!","red"))


class Calculator:

    def __init__(self,in_num1,in_num2,op_choice):
        self.num_1 = in_num1
        self.num_2 = in_num2
        self.choice = op_choice
        self.result = 0

    def add(self):
        return (self.num_1 + self.num_2)

    def subtract(self):
        return (self.num_1 - self.num_2)

    def multiplication(self):
        return (self.num_1 * self.num_2)

    def divide(self):
        try:

            return (self.num_1 / self.num_2)
        
        except ZeroDivisionError:
            return colored("Division by Zero not Possible!","yellow")

    
    def operation(self):
        
        if self.choice == '+':
            self.result = self.add()
        
        elif self.choice == '-':
            self.result = self.subtract()
        
        elif self.choice == "x" or self.choice == "*":
            self.result = self.multiplication()

        elif self.choice == "/":
            self.result = self.divide()

        else:
            self.result = colored("Invalid Operator choise!!!","red")
        
        return self.result


if __name__ == '__main__':
    while True:
        user_input = FormatInput()

        try:
            num_1, num_2, opr = user_input.format_exp()
            print(colored(f"First Number = {num_1} \nOperator = {opr} \nSecond Number = {num_2}","magenta"))
            calc = Calculator(num_1,num_2,opr)
            # print(result)
            result = calc.operation()

            print(colored(f"{num_1} {opr} {num_2} = {result}","blue"))

        except TypeError:
            print(colored("Please enter numbers and try again!!","light_yellow"))

        finally:
            in_end = input("Do you want to continue calculation(Y/y): ")
            
            if in_end.lower()  == 'y':
                continue
            else:
                break
