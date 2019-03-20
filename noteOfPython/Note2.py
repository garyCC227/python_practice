"""
Good Naming

#####################and also make sure you have a good comment by # !
#####################or description of the class or method or function by """ """
"""
#clearing descrip the variable
'''
Rule for nameing:
    -  constant
        1.how to name:Upercase and Underscrore:
            THIS_IS_GLOBAL_CONSTANT
        2.good to make all constant in one file
    - variable, funtion name, arguments, property
        1. lower case and Underscrore
            i_am_a_variable_or_a_function
    - class name
        1. always write in CamelCase
            ClassName
    -modules, package
        1.short, and lowercase
            os
            sys
            flask
    -for boolean elements
        1. use "is" or "has":
            is_existed
            has_cached
            is_connected
    -dictionary variable
        1. make it explicit
    - avoid existed name and dont make variblae name too generic!!!!
'''

'''
How to build good arguments

    -iterative design
        1. argument name 在一个class里面， build by 可以重复利用多次
        2. for some agurment 是附加的， 应该设置default value
            def my_function(some_arg_is_not_use_often = None):
    - *args and **kw. use carefully
        1. *arg ->把没有keyword的varible pack as a list
        2. **kw ->把有keyword的varible pack as a dictionary
'''
# first with *args
>>> args = ("two", 3,5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two","arg1":5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3

# use *arg and **kw as function argument  to manager input arguments
some_func(fargs,*args,**kwargs)
##########-------------------------------------------------------------------------------------
''''
limitation of class and modules
    for a class
        -   around 10 methods is best
        -   more than 10, create another sub-class
    for a module
        -   around 500 lines is good
'''
