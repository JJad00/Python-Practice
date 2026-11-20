from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, department)
        self.salary = salary

    def get_pay(self):
        return self.salary
