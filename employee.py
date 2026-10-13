# employee.py
# Employee inherits from Person and shows ENCAPSULATION with a private salary.

from person import Person


class Employee(Person):
    def __init__(self, employee_id, name, age, phone, position, salary):
        super().__init__(name, age, phone)
        self.employee_id = employee_id
        self.position = position
        self.__salary = 0          # private: name-mangled, hidden from outside code
        self.set_salary(salary)    # use the setter so validation also runs here

    # Getter: the only way to READ the salary from outside
    def get_salary(self):
        return self.__salary

    # Setter: the only way to CHANGE the salary, with validation
    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = new_salary

    # Polymorphism: Employee's own version of get_details()
    def get_details(self):
        return (f"Employee ID : {self.employee_id}\n"
                f"Name        : {self.name}\n"
                f"Age         : {self.age}\n"
                f"Phone       : {self.phone}\n"
                f"Position    : {self.position}\n"
                f"Salary      : {self.get_salary():.2f}")
