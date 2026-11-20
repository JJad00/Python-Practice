class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def get_pay(self):
        return 0

    def __str__(self):
        return self.name
