# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())



# KeyError
def produce_key_error():
    dictionary = {'pea': 5, 'pod': 7, 'china': 10}
    print(dictionary['doll'])



# IndexError
def produce_index_error():
    list = ['these', 'are', 'things', 'in', 'a', 'list']
    print(list[9])


# NameError
def produce_name_error():
    print(fakenews)


# UnboundLocalError
name = 'alice'
def produce_unbound_local_error():
    print(name)

    name = 'bob'


# TypeError
def produce_type_error():
    print('string'/ 9)


# ValueError
def produce_value_error():
    import math
    print(math.sqrt(-1))


# ZeroDivisionError
def produce_zero_division_error():
    print(9 / 0)



# OverflowError
def produce_overflow_error():
    import math
    print(math.exp(1000))


# FileNotFoundError
def produce_file_not_found_error():
    open('narnia', 'r')


# UnicodeEncodeError
def produce_unicode_encode_error():
    a = u'café'
    b = a.encode('utf8')
    r = str(b)
    print("The unicode string after fixing the UnicodeEncodeError is as follows:")
    print(r)


# ModuleNotFoundError
def produce_module_not_found_error():
    import pndas


# ImportError
def produce_import_error():
    import rndom
