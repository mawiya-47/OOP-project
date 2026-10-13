# appointment.py
# An appointment links one patient and one doctor using their IDs.


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = "Booked"     # becomes "Cancelled" when cancelled

    def cancel(self):
        self.status = "Cancelled"

    # Same method name as the other classes (polymorphism)
    def get_details(self):
        return (f"Appointment ID : {self.appointment_id}\n"
                f"Patient ID     : {self.patient_id}\n"
                f"Doctor ID      : {self.doctor_id}\n"
                f"Date           : {self.date}\n"
                f"Time           : {self.time}\n"
                f"Status         : {self.status}")
