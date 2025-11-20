class Employee:
    def __init__(self, empid=100, name='aaa', basic=10000):
        self._empid = empid
        self._name = name
        self._basic = basic

    # property name : read-only
    @property
    def name(self):
        return self._name

    # property basic : read/write
    @property
    def basic(self):
        return self._basic

    @basic.setter
    def basic(self, value):
        if value <= 0:
            raise ValueError('Salary cannot be zero or negative')
        else:
            self._basic = value

    def calculate_salary(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da

    def calculate_premium(self):
        return self._basic * 0.01

    def __str__(self):
        return f'Employee details Id: {self._empid} ,' \
               f' Name: {self._name} , Salary: {self._basic}'

    def __repr__(self):
        return f'Employee ({self._empid} , {repr(self._name)}, {self._basic})'


class NewEmployee:
    count = 0  # class attribute

    def __init__(self, name='aaa', basic=10000):
        NewEmployee.count += 1
        self._empid = NewEmployee.count
        self._name = name
        self._basic = basic

    def calculate_salary(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da



    def __str__(self):
        return f'Employee details Id: {self._empid} ,' \
               f' Name: {self._name} , Salary: {self._basic}'

    @staticmethod
    def show_employee_count():
        print('Employee count', NewEmployee.count)

    @classmethod
    def set_count(cls):
        cls.count = 100
