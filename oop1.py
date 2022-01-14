#method function associated with class

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee('Brian', 'Messiah', 5000)
emp_2 = Employee('User', 'Test', 100)
#
# print(emp_1)
# print(emp_2)
#
# emp_1.first = 'Bob'
# emp_1.last = 'Lob'
# emp_1.email = 'Bob.Lob@gmail.com'
# emp_1.pay = 2
#
# emp_2.first = 'Test'
# emp_2.last = 'Tester'
# emp_2.email = 'Test.Tester@gmail.com'
# emp_2.pay = 8
#
print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)


