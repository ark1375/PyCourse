## Primitive data Types
## int, bool, float, str, complex, list, tuple, dic, set, object
## type(varName)
## [Link](https://docs.python.org/3/library/stdtypes.html) 

## Non-Primitive Data types
## Defined by the User ----> Class

# var_1 = 12
# print(type(var_1))

# var_1 = 1.2
# print(type(var_1))

# var_1 = "1.2"
# print(type(var_1))

# var_complex = 12 + 2j
# print(type(var_complex))



## Flow_Control
## 
## GoTo:
##
## 10 Hello
## 20 World
## 30 Hello Again
## 40 World Again
## 50 GOTO 10
##
##

## IF (if), Else If (elif) , ELSE (else)   ----> Flow Control 1
## For (for) , While(while)                ----> Flow Control 2 (loop)
## Min-Max ----> Program with else - if - elif

### Root Fininding Algorithm For Cubic Polynomial 
### y = ax3 + bx2 + cx + d
### Gettig a,b,c,d from the user

## Default Arguments -> def name_of_the_function(arg = "Default Value"):

a = float( input("a:") )
b = float( input("b:") )
c = float( input("c:") )
d = float( input("d:") )

def cubic(x = 1):
    sent_1 = a * (x ** 3 )
    sent_2 = b * (x ** 2 )
    sent_3 = c * x
    sent_4 = d
    
    return sent_1 + sent_2 + sent_3 + sent_4

def cubic_deriv(x = 1) -> float:
    sent_1 = 3 * a * (x ** 2)
    sent_2 = 2 * b * x
    sent_3 = c

    return sent_1 + sent_2 + sent_3

guess_x = 0.5

itter = 10

for i in range(itter):
    
    cub = cubic(x = guess_x)
    cub_der = cubic_deriv(x = guess_x)
    
    guess_x -= (cub/cub_der)

print(guess_x)

