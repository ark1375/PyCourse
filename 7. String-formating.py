## C
## String Formating
## 'Hello' -> ['H','e','l','l','o']
## int , double , float ---> How to display it : String Formating
## java -> system.out.print('Hello' + 12 + 'World!') ---> Hello12World!
## python -> first, cast the variable to string, then add them them together
## C / C++ -> printf("Hello %d World" , 12) ---> Hello 12 World
##
## List of students = ['ahamad','ali','sara','mariam']
## List of scores = [12, 20 , 16 , 14]
##
## printf("Student: %s With Score %d" , name_student , score_student) -> Student: Ahmad With Score 12

## Old Style Formating
## New Style Formating
## String Interpolation or f-string :::: python_version > 3.6
students_fname = ['Ahamad','Ali','Sara','Mariam']
students_lname = ['Kazemi','Jabari','Mardiha','Hoseini']
student_score = [12.5, 20 , 16.25 , 14.75]

# % operator string formating
# for i in range(4):
#     # print('Student Name: ' + students_fname[i] +" " + students_lname[i] + "  With Score: " + str(student_score[i])  )
#     # %s , %d , %f , %x and etc
#     print('Student Name: %s %s With Score %0.2f'%(students_fname[i] ,students_lname[i], student_score[i] ))

    # 32.1264 - 07.3f --> 032.126

## New Style Formating
## .format
# "Hello {} World {}".format('12' , 'To Classroom') --> 'Hello 12 World To Classroom'
# "Hello {my_number} World {my_str}".format( my_number = '12' , my_str = 'To Classroom') --> 'Hello 12 World To Classroom'

# for i in range(4):
#     print(
#         'Student Name: {} {} With Score {:0.2f}'.format(students_fname[i] ,students_lname[i], student_score[i])
#         )

## String Interpolarion
## f'Hello {12} World {'My Class'}'

for i in range(4):
    print(
        f'Student Name: {students_fname[i]} {students_lname[i]} With Score {student_score[i]:0.2f}'
        )

## :04.0'a letter'
## f -> float
## d -> int or decimal
## b -> binary (base 2)
## o -> octal (base 8)
## x or X -> hex
## s -> string
## e or E -> scientific notation 145.12 -> 1.4512 * 10^2
## % -> mult by 100
## 12.345 -> 03.2f --/-->  012.34