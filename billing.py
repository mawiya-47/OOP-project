# billing.py
# A simple bill: consultation charges + additional hospital charges.


class Bill:
    def __init__(self, patient_id, patient_name, consultation_charges, additional_charges):
        # Validate: charges must not be negative
        if consultation_charges < 0 or additional_charges < 0:
            raise ValueError("Charges cannot be negative.")
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.consultation_charges = consultation_charges
        self.additional_charges = additional_charges

    def calculate_total(self):
        return self.consultation_charges + self.additional_charges

    def get_details(self):
        return (f"Patient ID           : {self.patient_id}\n"
                f"Patient Name         : {self.patient_name}\n"
                f"Consultation charges : {self.consultation_charges:.2f}\n"
                f"Additional charges   : {self.additional_charges:.2f}\n"
                f"TOTAL BILL           : {self.calculate_total():.2f}")
