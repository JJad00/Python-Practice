from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee


def load_employees():
    # Create a list of employees with different pay types
    employees = [
        HourlyEmployee("Nick DeFalco", "Sales", 2000, 26),
        SalaryEmployee("Applejack Johnson", "Sales", 44000),
        SalaryEmployee("Mario Dubois", "Sales", 77200),

        SalaryEmployee("Anthony Jo", "Engineering", 98000),
        Employee("Stephanie Johnson", "Engineering"),

        CommissionEmployee("Dominic Togo", "Maintenance",
                           20000, 90000, 0.50),
        HourlyEmployee("Christina Gonzalez", "Maintenance",
                       2000, 20.592),

        HourlyEmployee("Geoffrey Dav", "HR", 2000, 67.60)
    ]

    return employees


def main():
    employees = load_employees()

    # Dictionary grouped by department
    employee_dict = {}

    for emp in employees:
        if emp.department not in employee_dict:
            employee_dict[emp.department] = []

        employee_dict[emp.department].append(emp)

    # Process each department
    for department, emp_list in employee_dict.items():
        print(f"Department: {department}")

        total_payroll = 0

        for emp in emp_list:
            pay = emp.get_pay()

            print(f"    {emp.name} ({emp.__class__.__name__}): ${pay:.2f}")

            # Show commission breakdown only for commission employees
            if isinstance(emp, CommissionEmployee):
                base = emp.get_base_pay()
                commission = emp.get_commission()

                percentage = (commission / pay) * 100 if pay != 0 else 0

                print(
                    f"        Base ${base:.2f} + "
                    f"Commission ${commission:.2f} "
                    f"({percentage:.1f}% of earnings)"
                )

            total_payroll += pay

        print(f"Total Payroll: ${total_payroll:.2f}")
        print()


if __name__ == "__main__":
    main()
