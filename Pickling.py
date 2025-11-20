import pickle
from Employees import Employee
import logging

# An example Python object
e1 = Employee()
e2 = Employee(99, 'xyz', 30000)
e3 = Employee(44545, 'bbb', 60000)

employees = [e1, e2, e3]

# logging.basicConfig(filename='my_app.log', filemode='a', level=logging.INFO)
logging.basicConfig(level=logging.INFO, format='%(levelname)s, %(asctime)s, %(message)s')

# Pickling the object to a file
with open('employee_data.pkl', 'wb') as fw:
    try:
        for employee in employees:
            pickle.dump(employee, fw)
            logging.info('Writing data')
    except IOError as er:
        print(er)

employee_data =[]
with open('employee_data.pkl', 'rb') as fr:
    while True:
        try:
            employees = pickle.load(fr)
            employee_data.append(employees)
        except EOFError:
            logging.info('Reached end of the file')
            break

print(employee_data)