from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, department, hours, rate):
        super().__init__(name, department)
        self.hours = hours
        self.rate = rate

    def get_pay(self):
        return self.hours * self.rate
