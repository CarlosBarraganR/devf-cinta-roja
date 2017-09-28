##
###  PRINT DATA, FUNCTIONS AND FORMAT
####

say_hello = "Hello World"

print(say_hello)

print("\nHello Carlos B")

# ======== FUNCTIONS ============

"""
    my_function(line) -> none

    Print a string
"""
def my_function(line):
    print (line)
    function_inception()

"""
    function_inception() -> none

    Prints a second string
"""
def function_inception():
    print ('Esta string se encuentra dentro de otra funcion')

my_function(say_hello)

# ======== END FUNCTIONS =========

# ======== FORMAT  ============

"""
    get_result() -> none
    
    Shows the formatted result of get_suma(x,y)
"""
def get_result():
    return "El resultado de la suma de {} + {} es igual a {}"

"""
    get_suma(x,y) -> string
    
    Params: x (int), y (int)
    return: string
    
    Adds the integers retrieved in get_suma(x,y) to format
"""
def get_suma(x,y):
    suma = x + y
    return get_result().format(x, y, suma)

"""
    main_suma() -> none

    A basic function that adds two integers and prints the data 
"""
def main_suma():
    a = int(input("Enter a interger: "))
    b = int(input("Enter another interger: "))
    print(get_suma(a,b))

main_suma()

# ======== END FORMAT  ============

##
###  IF ELSE
####

# ======== IF ELSE  ============

"""
    if_else_function() -> none

    Basic if-elif-else example
"""
def if_else_function():

    numero1 = 4
    numero2 = 4

    if numero1 > numero2:
        print '{} es mayor que {}'.format(numero1, numero2)
    elif numero1 < numero2:
        print '{} es menor que {}'.format(numero1, numero2)
    elif numero1 == numero2:
        print 'son iguales'.format(numero1, numero2)
    else:
        print ('error')

if_else_function()

# ======== END IF ELSE  ============