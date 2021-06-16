from modules import calculator
import random

def random_list():
    rand_list = []
    while len(rand_list) < 20:
        i = random.randint(1, 100)
        if i not in rand_list:
            rand_list.append(i)
    return rand_list


class main_calculator():
    def plus(a,b):
        print(calculator.plus.add.addition (a,b))

    def devis(a,b):
        print(calculator.div.Div.div(a, b))

    def multi(a,b):
        print(calculator.mul.mul.mul(a, b))

    def sub(a,b):
        print(calculator.substraction.substract.sub(a, b))

a = random.choice(random_list())
b = random.choice(random_list())

main_calculator.plus(a,b)
main_calculator.devis(a,b)
main_calculator.multi(a,b)
main_calculator.sub(a,b)
