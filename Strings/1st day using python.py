Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # This is a comment before some code
print("Hello from Python!")
print("Winter is coming") # this is an in-line comment
SyntaxError: multiple statements found while compiling a single statement
>>> print ("I'm a string") #I'm a comment
I'm a string
>>> my_string ("I'm a Python Programmer!")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    my_string ("I'm a Python Programmer!")
NameError: name 'my_string' is not defined
>>> my_string "I'm a Python Programmer!"
SyntaxError: invalid syntax
>>> my_string = "I'm a Python programmer!"
>>> my_string = "I'm a Python programmer!
SyntaxError: EOL while scanning string literal
>>> my_string = "I'm a Python programmer!"
>>> my_string = "I'm a Python programmer!"
>>> a_long_string = '''This is a
multi-line string. It covers more than
one line'''
>>> my_string = "HEllo "quote" world"
SyntaxError: invalid syntax
>>> tripleString = """hello world "quote" in a string"""
>>> my_number = 123
>>> my_string = str(my_number)
>>> my_string = abc
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    my_string = abc
NameError: name 'abc' is not defined
>>> my_string = "abc"
>>> my_number = str(my_string)
>>> asd
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    asd
NameError: name 'asd' is not defined
>>> my_number = "123"
>>> my_string = "abc"
>>> id(my_string)
5271072
>>> my_string = "abc"
>>> id(my_string)
5271072
>>> my_unicode_string = u"This is unicode!"
>>> 123
123
>>> 123
123
>>> string_one = "My dog ate "
>>> string_two = "my homework!"
>>> string_three = string_one + string_two
>>> dir(my_string)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> my_string = "I like Python!"
>>> my_string[0:1]
'I'
>>> my_string = "I like Python!"
>>> my_string[0:6]
'I like'
>>> my_string = "I like Python!"
>>> my_string[0:10]
'I like Pyt'
>>> my_string = "IlikePythion!"
>>> my_string[0:6]
'IlikeP'
>>> my_string = "I hate you"
>>> my_string[0] = "I love myself"
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    my_string[0] = "I love myself"
TypeError: 'str' object does not support item assignment
>>> my_string = "I hate you"
>>> my_string = "I love myself"
>>> my_string = "fuck you"
>>> my_string[0:1]
'f'
>>> my_string = "I hate you", my_string = "I love myself", my_string = "fuck you"
SyntaxError: can't assign to literal
>>> my_string = "I love you!"
>>> my_string[7:]
'you!'
>>> my_string = "I love you!"
>>> my_string[2:-5]
'love'
>>> my_string = "I like %s" % "Python"
>>> my_string
'I like Python'
>>> var = "cookies"
>>> another_string = "I like %s" % var
>>> another_string
'I like cookies'
>>> another_string = "I like %s and %s % ("Python", var)
SyntaxError: invalid syntax
>>> my_string = "I like %s" % "Python"
>>> my_string
'I like Python'
>>> var = "cookies"
>>> newString = "I like %s" % var
>>> newString
'I like cookies'
>>> another_string = "I like $s and %s" % ("Python", var)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    another_string = "I like $s and %s" % ("Python", var)
TypeError: not all arguments converted during string formatting
>>> another_string = "I like %s and %s" % ("Python", var)
>>> another_string
'I like Python and cookies'
>>> my_string = "I love %s" % "Skateboarding"
>>> my_string
'I love Skateboarding'
>>> var = "Programming"
>>> newString = "I love %s" % var
>>> newString
'I love Programming'
>>> another_string = "I love %s and %s" % ("Skateboarding", var)
>>> another_string
'I love Skateboarding and Programming'
>>> my_string = "%i" + "%i" = "%i" (4,3,7)
SyntaxError: can't assign to operator
>>> my_string = "%i + %i = %i" (4,3,7)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    my_string = "%i + %i = %i" (4,3,7)
TypeError: 'str' object is not callable
>>> my_string = "%i + %i = %i" % (4,3,7)
>>> my_string
'4 + 3 = 7'
>>> float_string = "%f" % (1.23)
>>> float_string
'1.230000'
>>> floar_string = "%ff" % (1.23)
>>> floar_string
'1.230000f'
>>> float_string = "%f00000" % (1.23)
>>> float_string
'1.23000000000'
>>> float_string2 = "%.2f" % (1.25)
>>> floar_string2
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    floar_string2
NameError: name 'floar_string2' is not defined
>>> float_string2
'1.25'
>>> float_string3 = "%.2f" % (1.2589)
>>> float_string3
'1.26'
>>> float_string3 = "%.4" % (1.2345)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    float_string3 = "%.4" % (1.2345)
ValueError: incomplete format
>>> float_string3 = "%.4f" % (1.2345)
>>> float_string3
'1.2345'
>>> float_string3 = "%.2f" % (1.3785)
>>> float_string3
'1.38'
>>> float_string3 = "%.2f" % (1.3185)
>>> float_string
'1.23000000000'
>>> float_string3
'1.32'
>>> float_string3 = "%.2f" % (1.3185)
>>> float_string3
'1.32'
>>> float_string3 = "%.2f" % (1.3115)
>>> float_string3
'1.31'
>>> print ("%(lang)s is fun!" % {"lang": "Skateboarding"})
Skateboarding is fun!
>>> 
