# hospital.py
# The Hospital class owns the four lists and the rules for changing them.
# Data lives only in memory, so it is lost when the program closes.

from patient import Patient
from doctor import Doctor
from employee import Employee
from appointment import Appointment


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.employees = []
        self.appointments = []
        # Counters give every new object a unique ID within its category
        self.next_patient_id = 1
        self.next_doctor_id = 1
        self.next_employee_id = 1
        self.next_appointment_id = 1

    # ---------------- Patients ----------------
    def add_patient(self, name, age, gender, phone, disease):
        patient = Patient(self.next_patient_id, name, age, gender, phone, disease)
        self.patients.append(patient)
        self.next_patient_id += 1
        return patient

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None   # not found

    def remove_patient(self, patient_id):
        patient = self.find_patient(patient_id)
        if patient is None:
            return False
        self.patients.remove(patient)
        # Cancel this patient's active appointments so none are left hanging
        for appointment in self.appointments:
            if appointment.patient_id == patient_id and appointment.status == "Booked":
                appointment.cancel()
        return True

    # ---------------- Doctors ----------------
    def add_doctor(self, name, age, specialization, phone, fee):
        doctor = Doctor(self.next_doctor_id, name, age, specialization, phone, fee)
        self.doctors.append(doctor)
        self.next_doctor_id += 1
        return doctor

    def find_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def remove_doctor(self, doctor_id):
        doctor = self.find_doctor(doctor_id)
        if doctor is None:
            return False
        self.doctors.remove(doctor)
        for appointment in self.appointments:
            if appointment.doctor_id == doctor_id and appointment.status == "Booked":
                appointment.cancel()
        return True

    # ---------------- Employees ----------------
    def add_employee(self, name, age, phone, position, salary):
        employee = Employee(self.next_employee_id, name, age, phone, position, salary)
        self.employees.append(employee)
        self.next_employee_id += 1
        return employee

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    # ---------------- Appointments ----------------
    def book_appointment(self, patient_id, doctor_id, date, time):
        # Validate that the patient and doctor really exist
        if self.find_patient(patient_id) is None:
            raise ValueError("Patient ID not found. Add the patient first.")
        if self.find_doctor(doctor_id) is None:
            raise ValueError("Doctor ID not found. Add the doctor first.")
        # A doctor cannot have two booked appointments at the same date and time
        for appointment in self.appointments:
            if (appointment.doctor_id == doctor_id and appointment.date == date
                    and appointment.time == time and appointment.status == "Booked"):
                raise ValueError("This doctor is already booked at that date and time.")
        appointment = Appointment(self.next_appointment_id, patient_id, doctor_id, date, time)
        self.appointments.append(appointment)
        self.next_appointment_id += 1
        return appointment

    def find_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None

    def search_appointments_by_patient(self, patient_id):
        results = []
        for appointment in self.appointments:
            if appointment.patient_id == patient_id:
                results.append(appointment)
        return results

    def cancel_appointment(self, appointment_id):
        appointment = self.find_appointment(appointment_id)
        if appointment is None:
            raise ValueError("Appointment ID not found.")
        if appointment.status == "Cancelled":
            raise ValueError("This appointment is already cancelled.")
        appointment.cancel()
