from Employees import Employee, NewEmployee

e1 = Employee()  # __init__ with default param
print(e1)
print(repr(e1))
""" str vs repr
__str__ gives informal representation of an object often used for printing
__repr__ gives formal representation of an object often used for reconstruction
"""
e2 = eval(repr(e1))
print(e2)
print(type(e2))

e3 = Employee(44545, 'bbb', 60000)  # __init__ with user-defined  param
print(e3)
print(e1.calculate_salary())
print(e3.calculate_salary())

#e3.name = 'abc' #read -only
print(e3.name)  # property name

# e3.basic = -1000 #-ve value not allowed
print(e3.calculate_salary())


n1 = NewEmployee('ppp', 45000)
n2 = NewEmployee('mmm', 90000)

NewEmployee.show_employee_count()
NewEmployee.set_count()
n3 = NewEmployee('kkk', 50000)
NewEmployee.show_employee_count()
