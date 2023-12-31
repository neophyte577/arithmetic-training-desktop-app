from random import randint, choice
from time import time

level_bounds = [ {'+':(1,25,1,25), '-':(1,25,1,24), '*':(2,5,1,5), '/':(1,10,5)},
              {'+':(5,50,5,50), '-':(5,50,4,49), '*':(5,10,2,5), '/':(2,20,2,6)},
              {'+':(5,100,5,100), '-':(5,100,4,99), '*':(10,20,2,10), '/':(2,40,3,10)} ]


def isprime(n):

    prime = True

    for k in range(2,n):
        if n % k == 0:
            return False
        else:
            pass
            
    return prime


def int_selector(operation, current_level):

    bounds = level_bounds[current_level][operation]
    
    if operation in ['+', '-', '*']:
 
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

        for k in range(bounds[2],bounds[3]):

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

                print('Correcto')
                print()
                
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

    op_list = ['+', '-', '*', '/']

    last_level = 2

    current_level = 0

    while current_level <= last_level:

        print('---------------')
        print('LEVEL', current_level+1)
        print('---------------')
        print()


        time_total = 0

        counter = 0

        while counter < 3:

            operation = choice(op_list)

            x, y = int_selector(operation, current_level)

            print('Que es', x, operation, y, '?')
            print()

            counter, round_time = round(operation, x, y, counter)
        
            time_total += round_time

        print('Level', current_level+1, 'complete.')
        print()

        current_level += 1

main()