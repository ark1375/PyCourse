import math

## Lambda Functions
### map, filter, advanced for loops --
## Normal functions:

def name_of_function(inp_1 , inp_2):
    return inp_1 + inp_2

print(
    name_of_function(12,21)
)

## Lambda Functions:

name_of_lambda_function = lambda x,y : x + y

print(
    name_of_lambda_function(12,21)
)

## Eculidian Distance   Sqrt((x1 - x0)^2 + (y1 - y0)^2)
## Norm2 -- The size of a vector --> Sqrt(x^2 + y^2)

euc_distance = lambda x_1 , x_2 , y_1 , y_2 : math.sqrt( 
        math.pow( (x_1 - x_2) , 2) + math.pow( (y_1 - y_2) , 2) 
    )

print(
    euc_distance( 0 , 1 , 0 , 1)
)


## Defining Norm_2 as lambda functions

norm_2 = lambda x , y : math.sqrt( (x**2) + (y**2) )

# a , b = int(input("X:")) , int(input('Y:'))

print(
    norm_2(x = 2 , y = 2)
)

## Behavour of functions as variables

nomr_2_copy = norm_2

print(
    nomr_2_copy(x = 1, y = 1)
)

## Lambda functions are as type class=function

print(type(nomr_2_copy))


def some_function():
    print("Python Advanced Class")

some_function_copy = some_function

some_function_copy()


##################################################
############## Function Generators ###############
##################################################


def p_norm(p , x1 , x2):
    sum_elements = (x1 ** p) + (x2 ** p)
    return math.pow( sum_elements , (1/p) )

print(
    p_norm(1 , 1 ,1)
)

## Function Generators: A Function that resturns a utilized function

def p_norm_generator(p):

    p_norm = lambda x1 , x2 : math.pow( (x1 ** p) + (x2 ** p) , (1/p) )
    
    return p_norm

norm_1 = p_norm_generator(1)
norm_2 = p_norm_generator(2)
norm_3 = p_norm_generator(3)

## norm_1 = lambda x1 , x2 : math.pow( (x1 ** 1) + (x2 ** 1) , (1/1) )
## norm_2 = lambda x1 , x2 : math.pow( (x1 ** 2) + (x2 ** 2) , (1/2) )
## norm_3 = lambda x1 , x2 : math.pow( (x1 ** 3) + (x2 ** 3) , (1/3) )

print(
    norm_1(1,1),
    norm_2(1,1),
    norm_3(1,1)
)

print(
    p_norm_generator(1)(1,2),
    p_norm_generator(2)(1,2),
    p_norm_generator(3)(1,2)
)

## adress = "http://www.google.com"

## internet.get_html(adress)
## internet.seratch_html(adress , 'python')
## ...

## internet_lib = internet(adress)

## internet_lib.get_html()
## internet_lib.search_html('python')


## Using def keyword for function generator:

def p_norm_generator(p):

    def norm(x1 , x2):
        return math.pow( (x1 ** p) + (x2 ** p) , (1/p) )
    
    return norm

norm_1 = p_norm_generator(1)
norm_2 = p_norm_generator(2)
norm_3 = p_norm_generator(3)

print(
    norm_1(1,1),
    norm_2(1,1),
    norm_3(1,1)
)

print(
    p_norm_generator(1)(1,2),
    p_norm_generator(2)(1,2),
    p_norm_generator(3)(1,2)
)