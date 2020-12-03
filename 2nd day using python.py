Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_list = [1,2,3]
>>> my_list2 = ["a", "b", "c"]
>>> my_nested_list = [my_list, my_list2]
>>> my_nested_list
[[1, 2, 3], ['a', 'b', 'c']]
>>> my_list = [4,5,6]
>>> my_list2 = ["d", "e", "f"]
>>> combo_list = my_list + my_list2
>>> combo_list
[4, 5, 6, 'd', 'e', 'f']
>>> alpha_list = [45, 1, 5, 56, 78, 25, 66, 4]
>>> alpha_list.sort()
>>> alpha_list
[1, 4, 5, 25, 45, 56, 66, 78]
>>> alpha_list[0:4]
[1, 4, 5, 25]
>>> my_dict = {}
>>> another_dict = ()
>>> my_other_dict = {"four":4, "five":5, "six":6}
>>> my_other_dict
{'four': 4, 'five': 5, 'six': 6}
>>> my_other_dict[four]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    my_other_dict[four]
NameError: name 'four' is not defined
>>> my_other_dict["four"]
4
>>> my_dict = {"name":"Al", "address": "420 somewhere I belong"}
>>> my_dict
{'name': 'Al', 'address': '420 somewhere I belong'}
>>> my_dict[""name]
SyntaxError: invalid syntax
>>> my_dict["name"]
'Al'
>>> my_dict["name"],["address"]
('Al', ['address'])
>>> my_dict["name","address"]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    my_dict["name","address"]
KeyError: ('name', 'address')
>>> "name" in my_dict
True
>>> "age" in my_dict
False
>>> "address" in my_dict
True
>>> my_dict["name, address"]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    my_dict["name, address"]
KeyError: 'name, address'
>>> my_dict.keys()
dict_keys(['name', 'address'])
>>> "name" in my_dict.keys()
True
>>> 
