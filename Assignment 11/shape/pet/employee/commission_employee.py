from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, department, base_pay, sales, commission_rate):
        super().__init__(name, department)
        self.base_pay = base_pay
        self.sales = sales
        self.commission_rate = commission_rate

    def get_base_pay(self):
        return self.base_pay

    def get_commission(self):
        return self.sales * self.commission_rate

    def get_pay(self):
        return self.get_base_pay() + self.get_commission()
