## List Comprehensions
##
import math

my_list = [12,23,54,67,1,34,9]

my_new_list = []

# for elm in my_list:
#     my_new_list.append(elm * 2)

# print(my_new_list)

# for i in range( len(my_list) ):
#     my_list[i] *= 2

# print(my_list)


## enumerate() ----> for a list, return index with value

# print(
#     list(enumerate(my_list))
# )

# for idx , elm in enumerate(my_list):
#     my_list[idx] = elm * 2

# print(my_list)

# my_new_list = [ (elm - 2) for elm in my_list ]
# print(my_new_list)

# list_coordinates = [(0,1) , (1,2) , (1,3) , (3,2)]

# def vec_norm(inp):
#     return math.sqrt(
#         (inp[0] ** 2) + (inp[1] ** 2)  
#     )

# list_norms = [ vec_norm(elm) for elm in list_coordinates ]

# print(list_norms)

# matrix = [
#     [12,2.34,33],
#     [4.2,15,6.1],
#     [7.3,5.8,29]
# ]

# my_new_list = [ elm for i in matrix for elm in i ]
# print(my_new_list)

matrix = [
    [12,2.34,33],
    [4.2,15,6.1],
    [7.3,5.8,29]
]

my_new_list = [ elm for i in matrix for elm in i if elm > 20 ]
print(my_new_list)

# frst_list = [1,2,3]
# sec_list = [4,5,6]

# print(
#     [(elm , elm2) for elm in frst_list for elm2 in sec_list]
# )

## Uses in Functional Programming