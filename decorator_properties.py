

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    def fullanme(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('ian', 'john')


emp_1.first = 'jim'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullanme())
