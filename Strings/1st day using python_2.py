Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("%(lang)s is fun!" % {"lang": "Python"})
Python is fun!
>>> "Python is as simple as {0}, {1}, {2}".format ("a", "b", "c")
'Python is as simple as a, b, c'
>>> print ("%(value)s %(value)s %(value)s!" % {"value": "JAZ"})
JAZ JAZ JAZ!
>>> "Python is as simple as {1}, {0}, {2}".format ("a", "b", "c")
'Python is as simple as b, a, c'
>>> 
