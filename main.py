from modules import calculator
import random

#def rand_list():
rand_list = []
while len(rand_list) < 20:
    i = random.randint(1, 100)
    if i not in rand_list:
        rand_list.append(i)
print(rand_list)


class main_calculator():
    def plus(*val1,**val2):
        print(calculator.plus.add.addition (*val1,**val2))

    def devis(val1,val2):
        print(calculator.div.Div.div(val1, val2))

    def multi(val1,val2):
        print(calculator.mul.mul.mul(val1, val2))

    def sub(val1,val2):
        print(calculator.substraction.substract.sub(val1,val2))

a = random.choice(rand_list)
b = random.choice(rand_list)
print(int(a))
print(int(b))

main_calculator.plus(a,b,3,3,3)
main_calculator.devis(a,b)
main_calculator.multi(a,b)
main_calculator.sub(a,b)
