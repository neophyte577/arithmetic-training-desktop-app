from random import randint, choice
from time import time

level_list = []

def isprime(n):

    prime = True

    for k in range(2,n):
        if n % k == 0:
            return False
        else:
            pass
            
    return prime


def int_selector(operation):
     
    if operation == '+':

        x, y = randint(1,10), randint(1,10) 

    elif operation == '*':

        x, y = randint(1,10), randint(1,10) 

    elif operation == '-':

        x = randint(2,10)

        y = randint(1,x-1)

    elif operation == '/':

        prime = True

        while prime == True:

            x = randint(1,10)

            prime = isprime(x)

        div_list = []

        for k in range(1,x):

            if x % k == 0:

                div_list.append(k)

        y = choice(div_list)

    return x, y

     
def round(operation, x, y, counter):
        
    round_time = 0

    correct = False

    start = time()

    while correct == False:

        is_integer = False

        while is_integer == False:

            try:

                n = int(input('Respuesta: '))
                print()

                is_integer = True

                if n == int(eval(str(x) + operation + str(y))):

                    print('Correcto')
                    print()
                    
                    correct = True

                    stop = time()

                    latency = stop - start

                    round_time += latency

                    counter += 1

            except Exception as error:
                print('Necesito int, por dios')
                print()

        return counter, round_time 


def main():

    op_list = ['+', '-', '*', '/']

    last_level = 3

    current_level = 3

    while current_level <= last_level:

        time_total = 0

        counter = 0

        while counter < 3:

            operation = choice(op_list)

            x, y = int_selector(operation)

            print('Que es', x, operation, y, '?')
            print()

            counter, round_time = round(operation, x, y, counter)
        
            time_total += round_time

        current_level += 1

main()