from random import randint, choice
from time import time
from math import sqrt, ceil


level_bounds = [ {'+':(1,25,1,25), '-':(1,25,1,24), '*':(2,5,2,5), '/':(2,16)},
                 {'+':(20,50,5,50), '-':(5,50,4,49), '*':(5,10,5,10), '/':(6,30)},
                 {'+':(30,100,5,100), '-':(5,100,4,99), '*':(11,30,6,10), '/':(20,150)} ]


def isprime(n):

    prime = True

    for k in range(2,ceil(sqrt(n))+1):
        if n % k == 0:
            return False
        else:
            pass
            
    return prime


def int_selector(operation, current_level):

    bounds = level_bounds[current_level][operation]
    
    if operation in {'+', '-', '*'}:
        x, y = randint(bounds[0], bounds[1]), randint(bounds[2], bounds[3])
        if operation == '-':
            if x < y:
                x, y = y, x

    elif operation == '/':
        prime = True

        while prime == True:
            x = randint(bounds[0], bounds[1])
            prime = isprime(x)

        div_list = []

        print(x, 'in div')

        for k in range(2, ceil(sqrt(x))+1):
            if x % k == 0:
                div_list.append(k)

        y = choice(div_list)

    return x, y

     
def round(operation, x, y, counter):
        
    round_time = 0

    correct = False

    start = time()

    while correct == False:
        try:
            n = int(input('Respuesta: '))
            print()

            if n == int(eval(str(x) + operation + str(y))):
                print('Correcto\n')                
                correct = True
                stop = time()
                latency = stop - start
                round_time += latency
                counter += 1

            else:
                print('WRONG')
                print()
                continue

        except Exception as error:
            print('Necesito int, por dios')
            print()
            continue
            
        return counter, round_time 


def main():

    operations = ('+', '-', '*', '/')

    last_level = 2

    current_level = 0

    time_data = []

    while current_level <= last_level:
        print('---------------')
        print('LEVEL', current_level+1)
        print('---------------')
        print()

        time_total = 0
        counter = 0
        level_times = []

        while counter < 3:
            operation = choice(operations)

            x, y = int_selector(operation, current_level)

            print('Que es', x, operation, y, '?')
            print()

            counter, round_time = round(operation, x, y, counter)
        
            level_times.append(round_time)

        time_data.append(level_times)

        print('Level', current_level+1, 'complete.')
        print()

        current_level += 1

    print(time_data)

if __name__ == '__main__':
    main()