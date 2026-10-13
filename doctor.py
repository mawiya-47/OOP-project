# doctor.py
# Doctor inherits name, age and phone from Person.

from person import Person


class Doctor(Person):
    def __init__(self, doctor_id, name, age, specialization, phone, consultation_fee):
        super().__init__(name, age, phone)
        if consultation_fee < 0:
            raise ValueError("Consultation fee cannot be negative.")
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    # Polymorphism: Doctor's own version of get_details()
    def get_details(self):
        return (f"Doctor ID      : {self.doctor_id}\n"
                f"Name           : {self.name}\n"
                f"Age            : {self.age}\n"
                f"Specialization : {self.specialization}\n"
                f"Phone          : {self.phone}\n"
                f"Consultation   : {self.consultation_fee:.2f}")
