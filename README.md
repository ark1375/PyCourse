# :snake: Python: One Step Further 
One step further in python.  
Instructed by Alireza Khalilian.
## Overview
:snake: __Welcome to PyCourse, One Step Further__  

This course is prepared for those who want to learn more about python and its capabilities. It is also for those who started python, forgot about it and left it unfinished. 
The main intention of this course is to give you a better intuition about python, how to better use it, write it, and apply it.
> ⚠️ __Having prior basic knowledge about python is _mandetory___.  
> However, at the beginning of the course, we review the basics of python to refresh your memory on the subject.  

### Course Road Map
> :black_nib: Full details of the contents are available [here](#contents).  

At the beginning of the course, we review the ___basic topics of python___ such as variables, operations, primitive data types, etc.  
The second section is a dive into ___Python's data structure___.  
Then we will take a look at ___how to write python codes correctly___.  
After that, we will start ___Programming paradigms___, First, _functional programming_, and later _object-oriented programming_ in python. We'll also spend some time exploring other ways to write python code.  
Later, we learn ___how packages and modules are handled in python___.  
And in the end, we learn some of the most important ___built-in modules of python___.  

> We intended to cover the python's built-in GUI (using Tkinter and Turtle) as well. However, because of the time limitations at hand, it is removed from the contents for now. 
&nbsp;  

### Discussions and Issues  
Students are free to use the __Issues and Discussion__ section of the repository to ask questions and start discussions. Students can participate in discussions or issues freely.

### Exercises
Exercises are one of the key aspects of this course. After the end of each topic, an __exercise__ will be given to students. The details of these exercises are uploaded to this Github repository. Studentes are expected to read the details of the exercise and write a solve for the problem acording to what theyre learned in previous weeks. 
> :zap: ___It is important to get your hands dirty if you want to learn to program thoroughly.___ Studying syntax and understanding them is roughly 20% of the work. It is when you write the actual code that the rest 80% of the learning happens.  

The exercises should be delivered via github and each student will have a branch to work on. You should clone the repository (instructions available bellow) and work on your branch directly.  

> :speech_balloon: If you had any problem related to programming syntax, runtime or semantic errors, you should start an __Issue__ [here][1].  
> On the other hand if you had any question about the lesson itself, for example something that you didn't quite understand, you should start a discussion [here][2].

Each exercise has a deadline based on its difficulty. It is expected that the solutions will be uploaded before meeting this deadline.
It is worth noting that any commit to your branch after the specified deadline is not acceptable.

#### How To Deliver Exercises
##### Clone the Repository
>⚠️You need to do this only once  
1. Create a folder in an arbitary path.
2. Navigate inside the folder, right-click and press `GitBash Here`.
3. Enter the following command `git clone https://github.com/ark1375/PyCourse.git`.

##### Write your Exercise and Upload
1. Navigate inside the repository and open GitBash.
2. If you have your personal branch activated you are good to go. If not, switch to your branch using `git checkout -your branch name-`.
3. Now create a folder inside `Student_Resources` according to the exercise. For example `Exer_1` or `Exer_2`.
4. Write your code and save.
5. In git bash, add the files to git using `git add -file name` or `git add -A ` to add all files.
6. Commit your changes with an apropriate commit message using `git commit -m "Your Commit Message".
7. Push your local repository to github using `git push origin -Your branch name`.


### Notes
At the end of each week, the respective notes will be uploaded to this document. You can use these notes to review the lessons and solve the exercises. Feel free to explore them, review and update them.  
&nbsp;  

If you have any further question, feel free to contact me via telegram or email.
## Contents
The contents of this course are based on the books __Fluent Python - Luciano Ramalho__ and __Automate the Boring Stuff with Python - Al Sweigart__.  
It is estimated that these contents take 16 to 20 hours to complete. 
### Table of Content
1. Basics
    - Introduction
      - Python Versions
      - Python Installation
      - Coding Environments
      - Git and Exercises
      - Print Estatment and "Hello World"
    - Variables, Operations, Input, Primitive Data Types and Flow Controls
    - Functions, Lambda functions
    - Files
    - String Formating
    - Exercises

2. Pythonic Code
    - Naming Conventions
    - Pythonic Style
    - Better Comments, Lesser Comments

3. Data Structure
    - Lists and Tuples
    - Sets and Dictionaries
    - Conversions
    - Exercises

4. Functional Programming
    - Functional Programming Paradigim
    - Zip, Map and Filter
    - Exercises

5. Object Oriented Programming
    - Classes and Objects
    - Properties and Access Levels
    - Methods
    - Static Methods
    - Predefined Properties and Overwriting
    - Operator Overloading
    - Inheritance
    - Exercises

6. Other Programming Paradigims in Python 

7. Modules and Packages
    - Modules
    - Packages
    - Using Pip Effectively
    - Packaging your own Code
    - Python Docs
    - Exercises

8. Tools and Libraries
    - RegEX
    - Math
    - Random
    - HTTP
    - OS
    - JSON
    - Time
    - Exercises

9. ~~GUI and Graphics~~

## Notes

### Second Session

#### Git Hints

- You can use `git clone 'repository link'` to clone a repository in your computer.
- You can use `git pull origin master` to update your repository from github.

#### XOR Cipher

XOR Cipher is one of the most famous cipher algorithm to encrypt your data. It is simple, fast and easy.  
The algorithm is simple:  

1. Having a key __KEY__ and a string __STRING__:
2. For every character,  __CHAR__ in __STRING__:  
Perform the XOR operation on __KEY__ and __CHAR__ and save the result into another string __NEW_STRING__.
3. End the Algorithm.

Interesting thing about the XOR Cipher is that if you pereform the cipher using the same key on the _Encrypted_ string, you get the starting string __STRING__.  
  
Two main functions we used in the `2. xor-cipher.py` are `ord()` for converting a single string to ascii and `chr()` for converting an ascii code to string.  
For more information see the [Wikipedia Page](https://en.wikipedia.org/wiki/XOR_cipher) on XOR Cipher. Aslo for more on ASCII table, refer [here](https://en.wikipedia.org/wiki/ASCII).


### Third Session

#### Primitive Data Types

There are four primitive datatypes in python. However it can be extended to more than ten types.

- __Integer__: Integer numbers in python. Recognized by `class int`. You can convert other _permiited_ data types to integer using `int()` function.
- __Float__: Numbers with decimal points in python. Recognized by `class float`. You can convert other _permiited_ data types to float using `float()` function.
- __String__: Character String in python. One of the mose used data types. Recognized by `class str`. You can convert other _permiited_ data types to string using `str()` function.  
Remember that `ord()` was for converting a single length string to ascii code and `chr()` for converting ascii code back to string.
- __Boolean__: Boolean data type is used in python for determining binary situations. It's either `True` or `False`. You can convert other _permiited_ data types to string using `bool()` function.  
Remember that `ord()` was for converting a single length string to ascii code and `chr()` for converting ascii code back to string.  

    > :hotsprings: Any positive or negative number converted to boolean using `bool()` will yield `True` with exception of __0__ which results in `False`.

__Other default types in python:__

- __Object__: Backbone of every object in python.
- __Function__: Type of every function in python.
- __Complex__: Default type of Complex Numbers.
- __List__: Manifastation of Arrays.
- __Set__: Another array like type which simulates Sets in math.
- __Dictionary__: Equivalent of Map in Java, C and C++. This datatypes is roughly speaking related to JSONS in JavaScript.
- __Tuple__: An unextandable datatype like list.

### Flow Controls

There are thre type of flow control in python.

1. __if, elif and else__
2. __for, while__
3. __match__: Roughly speaking, it is equivalent to `switch` statement in C and Java.

### Functions and Default Arguments

Functions can be defined in python using the `def` keyword. Every function has it's own scope though they can access variables and functions in the upper scopes.  
#### Default Parameters Value

When defining a function, you can use the assign operator `=` to set a default value for an argument: `def someFunction(arg = default)`. When calling the function, if this arguments is not passed to the function, the code will use the arguments default value.  

```python
def someFunction(arg = default):
    pass

someFunction(arg) # --> Valid <--
someFunction() # --> Also Valid <--
```

#### Function Arguments

In total there are two types of Arguments:
-__Positional Arguments__: The triditional method of passing the arguments to a function. Positioning each variable at the right spot.
```python

def myFunction(arg1 , arg2):
    pass

var1 = 'some values'
var2 = 'some values 2'

myFunction(var1 , var2)
```

-__Keyword Arguments__: The new way of passing arguments to the functions, using the arguments by their names.
```python

def myFunction(arg1 , arg2):
    pass

var1 = 'some values'
var2 = 'some values 2'

myFunction(arg1 = var1 , arg2 = var2)
```



[1]: https://github.com/ark1375/PyCourse/issues
[2]: https://github.com/ark1375/PyCourse/discussions
