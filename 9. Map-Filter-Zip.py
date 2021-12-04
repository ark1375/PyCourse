
import math


############## Map ##############

# map(
#    function , itterator 1 , itterator 2 , ... 
# )

my_list_1 = [12,23,54,67,1,34,9]
my_list_2 = (2,3,1,6,2,3,1)

# def my_func(inp1, inp2 ):
#     return inp1 ** inp2

# my_new_list = map(my_func , my_list)

# print(
#     tuple(my_new_list)
#     )


## Itterator

# my_new_list = map(my_func , my_list_1 , my_list_2)

# print(
#     list(my_new_list)
# )

# my_new_list = map(lambda x: x+2 , my_list_1)

# math.pow(2 ,(1/3))

# my_new_list = map( lambda x: math.pow(x , 1/3) , my_list_1)

# print(
#     list(my_new_list)
# )



############## Filter ##############
# where --> numpy

# filter(function, itterator)

# my_number_list = [1,2,3,4,10,20,33,45,67,94]
# for elm in my_number_list:
#     if elm % 2 == 0:
#         do someting

# my_even_numlist = filter( lambda x: x % 2 == 0 , my_number_list)
## Filter ---> list cast to true and false, true passes filter and false doesn't pass filter

# print(
#     my_number_list , 
#     list(my_even_numlist)
# )


############## Zip ##############

# my_student_list = ['Ahmadreza' , 'Hossein' , 'Mahsa' , 'Maryam']
# my_student_score = [12,18,14,19]

# my_zipped_list = zip( my_student_list , my_student_score)
# print(
#     list(my_zipped_list)
# )


#### ZIP + FILTER

ls1 = [1,2,3,4,5,6,7,8]
ls2 = [1,3,3,2,1,4,6,1]

new_ls = list(zip(ls1, ls2))

filtered = filter( lambda x : x[0]%x[1] == 0 , new_ls )

print(
    list(filtered)
)