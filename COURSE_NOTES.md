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

### Fourth Session

#### Lambda Functions

Lambda functions are mostly handy when using _map_ and _filter_. They are defined in one and only one line.  
From a technical point of view, lambda functions are exactly same as functions. Both are recognized by type `<class function>`.

__Defining__:  

It is defined using `lambda` keyword following by the arguments and the operation.

```python
myFunction = lambda arg1, arg2 : ('Operation of the function')
```
##### 