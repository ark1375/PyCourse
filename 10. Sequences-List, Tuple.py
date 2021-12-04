## List Comperhensions ----> Talked Before

## Array , collection.deque, memoryview , bytearray, array.array
## List - Tuple - Dictionary


## Container Sequence ---> list, tuple,  coollection.deque , dictionary , set , ...
#####   ----> Hold Refrences
my_list = [12 , 14 , 19 , 0]

## Flat Sequence      ---> str , bytes , bytearray, memoryview, array.array , ...
#####   ----> Hold Value
my_string = 'hello'
my_list.append(my_string)

## [[x][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]]
## [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13]
## [ [H] , [E] , [L] , [L] , [O] ]
##    |-> 12654
##    |-> [12000 , 14000]  ---> [ [H] , [E] , [L] , [L] , [O] , ............... ]

## Mutable and Immutable Sequences   ----->   Mutable -> Can be changed , Immutable -> Cannot be changed
## Mutable Sequence
####  ----> list , bytearray, array.array, collection.deque

## Immutable Sequences
####  ----> tuple, str, bytes

#### List -> Generator Expression #=> Later

## Tuple --> Unpacking

isf_cord = (32.6539, 51.6660)
lat , long = isf_cord

## Swaping Elements
frst_var = 12
sec_var = 16
frst_var , sec_var = sec_var , frst_var ## Swaping Assignments

def some_function():
    return (12,13)

var_1 , var_2 = some_function()
# print(var_1 , var_2)

def formater(fname , lname , studentno):
    return f'Name: {fname}    FamilyName: {lname}     #{studentno}'

my_tp_ls = [
    ('Alireza' , 'Khalilian' , '1234') ,
    ('Mohamadreza' , 'Golzar' , '4567') ,
    ('Mohsen' , 'Tanabande' , '9870')
]

# for fname , lname , no in my_tp_ls:
#     print(
#         formater(fname , lname , no)
#     )
ls = [1,2,3]
print(
    formater(*ls)
)
for my_tpl in my_tp_ls:
    print(
        formater(*my_tpl)
    )

# my_tpl = ('ImpVar1' , 'ImpVar2' , 'ImpVar3' , 12,13,14,15,16)
my_tpl = ('ImpVar1' , 'ImpVar2' , 'ImpVar3' , 12,13,14,15,16 , 'ImpVar4')
var1 , var2, var3 , *rest , var4 = my_tpl
print(var1 , var2 , var3 , var4)
print(rest)



#### Named Tuples
from collections import namedtuple
City = namedtuple('City' , 'name country population')
isf = City('isfahan' , 'iran' , 2000000)
print(isf)
print(isf.country)
print(
    tuple(isf)
)