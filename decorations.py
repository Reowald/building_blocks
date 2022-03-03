

def decorators_f(original_f):
    def wrapper_f(*args, **kwargs):
        print('wrapper executed before "{}"'.format(original_f.__name__))
        return original_f(*args, **kwargs)
    return wrapper_f


# class decorator_class(object):
#     def __init__(self, original_f):
#         self.original_f = original_f
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed before "{}"'.format(self.original_f.__name__))
#         return self.original_f(*args, **kwargs)

# @decorators_f
# @decorator_class
@decorators_f
def display():
    print('display function ran')

# @decorators_f adding this without args and kwargs produces an error
# @decorators_f
# @decorator_class
@decorators_f
def display_info(name, age):
    print('display info had arguments ({}, {})'.format(name, age))

#@ symbol is exactly the same as the below calling function within a function
# decorated_disp = decorators_f(display)
#
# p = decorated_disp
#
# decorated_disp()
#
# print(p)
#
# p()


# display()
# #OR
#
# p = display
# print(p)
#
# #closures
# p()

display_info('soms', 45)