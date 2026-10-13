# patient.py
# Patient inherits name, age and phone from Person.

from person import Person


class Patient(Person):
    def __init__(self, patient_id, name, age, gender, phone, disease):
        super().__init__(name, age, phone)  # parent constructor sets name, age, phone
        self.patient_id = patient_id
        self.gender = gender
        self.disease = disease

    # Polymorphism: same method name as Doctor/Employee, different output
    def get_details(self):
        return (f"Patient ID : {self.patient_id}\n"
                f"Name       : {self.name}\n"
                f"Age        : {self.age}\n"
                f"Gender     : {self.gender}\n"
                f"Phone      : {self.phone}\n"
                f"Disease    : {self.disease}")
