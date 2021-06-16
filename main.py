from modules import calculator
import random

def random_numbers():
    rand_list = []
    for i in range(20) :
        r = random.randint(1,101)
        if r not in lis :
            rand_list.append(r)
        i+=1


class main_calculator():
    def plus(a,b):
        print(calculator.plus.add.addition (a,b))

    def devis(a,b):
        print(calculator.div.Div.div(a, b))

    def multi(a,b):
        print(calculator.mul.mul.mul(a, b))

    def sub(a,b):
        print(calculator.substraction.substract.sub(a, b))

a = random.choice(random_numbers())
b = random.choice(random_numbers())

main_calculator.plus(a,b)
main_calculator.devis(a,b)
main_calculator.multi(a,b)
main_calculator.sub(a,b)