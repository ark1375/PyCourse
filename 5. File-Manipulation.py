### Operating System -> Windows, Linux, Android, MacOS
#   File Access -> read, write
#   Open

# file = open('adress' , 'read mode')
# directory path -> adress
# reading file modes -> 'r' , 'w' , 'r+' , 'a'
# read mode 'r'

## Unix(MacOs) and Linux use '/' , Winows use '\'
# absoloute path    E:\Projects\Projects 2021\PyCourse\PyCourse\some_folder\test_file.txt
# relative path     some_folder\test_file.txt 
# . current folder, .. previous folder
# import timeit
# file = open('../' , 'r')
# # file.write('\nsome other Text')
# file_text = file.read()
# # file.close()
# print(ascii(file_text))




## Read - Write : Binary or ASCII read/write
## After manipulation, write or read -> close

# Using 'with' keyword
# with 'function' as 'variable name':

with open(r'some_folder\test_file.txt' , 'r') as file:
    print(
        file.read()
    )
    # file.write('\nA new Text')

## regex ---> r 





