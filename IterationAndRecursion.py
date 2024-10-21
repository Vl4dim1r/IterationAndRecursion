
#Brad Boal
#CIS261
#Iterative and  recursive functionality

def iterative_factorial(n):
    result = 1
    if n >= 0:
        for i in range(1, n+1):
            result = result * i
        return result
    else:
        return 'number must be positive'

def recursive_factorial(n):
    result  = 1
    while n  > 1:
        result =  result * n
        n -= 1 
    return result

def main_loop():
    print('Factorial results using an iterative function')
    print('0!' + str(iterative_factorial(0)))
    print('5!' + str(iterative_factorial(5)))
    print('10!' + str(iterative_factorial(10)))
    print('25!' + str(iterative_factorial(25)))
    print('50!' + str(iterative_factorial(50)))
    print('100!' + str(iterative_factorial(100)))
       
    print('Factorial results using an recursive function')
    print('0!' + str(recursive_factorial(0)))
    print('5!' + str(recursive_factorial(5)))
    print('10!' + str(recursive_factorial(10)))
    print('25!' + str(recursive_factorial(25)))
    print('50!' + str(recursive_factorial(50)))
    print('100!' + str(recursive_factorial(100)))
    
main_loop()