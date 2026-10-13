# main.py
# Command-line menus. Run the project with:  python main.py

from datetime import datetime
from hospital import Hospital
from billing import Bill

EMPLOYEE_POSITIONS = ["Receptionist", "Nurse", "Pharmacist"]


# ====================== Input helper functions ======================
def read_text(prompt):
    """Ask until the user types something that is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")


def read_int(prompt, minimum, maximum):
    """Ask until the user types a whole number inside the allowed range."""
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Error: Please enter a whole number (digits only).")
            continue
        if number < minimum or number > maximum:
            print(f"Error: Please enter a number between {minimum} and {maximum}.")
        else:
            return number


def read_amount(prompt):
    """Ask until the user types a number that is not negative."""
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        if number < 0:
            print("Error: The amount cannot be negative.")
        else:
            return number


def read_phone(prompt):
    """Phone must contain digits only and be 7 to 15 digits long."""
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone
        print("Error: Phone must be 7 to 15 digits (numbers only).")


def read_gender():
    print("Gender: 1. Male  2. Female  3. Other")
    choice = read_int("Choose gender: ", 1, 3)
    return ["Male", "Female", "Other"][choice - 1]


def read_date(prompt):
    """Date must look like YYYY-MM-DD, for example 2026-12-25."""
    while True:
        text = input(prompt).strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Error: Use the format YYYY-MM-DD (example: 2026-12-25).")


def read_time(prompt):
    """Time must look like HH:MM in 24-hour format, for example 14:30."""
    while True:
        text = input(prompt).strip()
        try:
            datetime.strptime(text, "%H:%M")
            return text
        except ValueError:
            print("Error: Use the format HH:MM, 24-hour (example: 14:30).")


def show_list(items, empty_message):
    """Print any list of objects. Polymorphism: each object's own get_details() runs."""
    if len(items) == 0:
        print(empty_message)
        return
    for item in items:
        print("-" * 40)
        print(item.get_details())
    print("-" * 40)


# ====================== Patient submenu ======================
def patient_menu(hospital):
    while True:
        print("\n--- Patient Management ---")
        print("1. Add new patient")
        print("2. View all patients")
        print("3. Search patient by ID")
        print("4. Update patient information")
        print("5. Remove patient")
        print("6. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = read_text("Name: ")
            age = read_int("Age (0-120): ", 0, 120)
            gender = read_gender()
            phone = read_phone("Phone number: ")
            disease = read_text("Disease / reason for visit: ")
            patient = hospital.add_patient(name, age, gender, phone, disease)
            print(f"Patient added successfully. Patient ID = {patient.patient_id}")

        elif choice == "2":
            show_list(hospital.patients, "No patients found.")

        elif choice == "3":
            patient_id = read_int("Enter patient ID: ", 1, 999999)
            patient = hospital.find_patient(patient_id)
            if patient is None:
                print("Error: No patient found with that ID.")
            else:
                print(patient.get_details())

        elif choice == "4":
            patient_id = read_int("Enter patient ID to update: ", 1, 999999)
            patient = hospital.find_patient(patient_id)
            if patient is None:
                print("Error: No patient found with that ID.")
            else:
                print(patient.get_details())
                print("What do you want to update?")
                print("1. Name  2. Age  3. Gender  4. Phone  5. Disease")
                field = read_int("Choose field: ", 1, 5)
                if field == 1:
                    patient.name = read_text("New name: ")
                elif field == 2:
                    patient.age = read_int("New age (0-120): ", 0, 120)
                elif field == 3:
                    patient.gender = read_gender()
                elif field == 4:
                    patient.phone = read_phone("New phone number: ")
                else:
                    patient.disease = read_text("New disease / reason: ")
                print("Patient updated successfully.")

        elif choice == "5":
            patient_id = read_int("Enter patient ID to remove: ", 1, 999999)
            if hospital.remove_patient(patient_id):
                print("Patient removed. Their booked appointments were cancelled.")
            else:
                print("Error: No patient found with that ID.")

        elif choice == "6":
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 6.")


# ====================== Doctor submenu ======================
def doctor_menu(hospital):
    while True:
        print("\n--- Doctor Management ---")
        print("1. Add doctor")
        print("2. View all doctors")
        print("3. Search doctor by ID")
        print("4. Remove doctor")
        print("5. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = read_text("Name: ")
            age = read_int("Age (18-100): ", 18, 100)
            specialization = read_text("Specialization: ")
            phone = read_phone("Phone number: ")
            fee = read_amount("Consultation fee: ")
            doctor = hospital.add_doctor(name, age, specialization, phone, fee)
            print(f"Doctor added successfully. Doctor ID = {doctor.doctor_id}")

        elif choice == "2":
            show_list(hospital.doctors, "No doctors found.")

        elif choice == "3":
            doctor_id = read_int("Enter doctor ID: ", 1, 999999)
            doctor = hospital.find_doctor(doctor_id)
            if doctor is None:
                print("Error: No doctor found with that ID.")
            else:
                print(doctor.get_details())

        elif choice == "4":
            doctor_id = read_int("Enter doctor ID to remove: ", 1, 999999)
            if hospital.remove_doctor(doctor_id):
                print("Doctor removed. Their booked appointments were cancelled.")
            else:
                print("Error: No doctor found with that ID.")

        elif choice == "5":
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 5.")


# ====================== Appointment submenu ======================
def appointment_menu(hospital):
    while True:
        print("\n--- Appointment Management ---")
        print("1. Book appointment")
        print("2. View all appointments")
        print("3. Search appointments by patient ID")
        print("4. Cancel appointment")
        print("5. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            patient_id = read_int("Patient ID: ", 1, 999999)
            doctor_id = read_int("Doctor ID: ", 1, 999999)
            date = read_date("Date (YYYY-MM-DD): ")
            time = read_time("Time (HH:MM): ")
            try:
                appointment = hospital.book_appointment(patient_id, doctor_id, date, time)
                print(f"Appointment booked. Appointment ID = {appointment.appointment_id}")
            except ValueError as error:   # raised by Hospital if validation fails
                print("Error:", error)

        elif choice == "2":
            show_list(hospital.appointments, "No appointments found.")

        elif choice == "3":
            patient_id = read_int("Enter patient ID: ", 1, 999999)
            results = hospital.search_appointments_by_patient(patient_id)
            show_list(results, "No appointments found for this patient.")

        elif choice == "4":
            appointment_id = read_int("Enter appointment ID to cancel: ", 1, 999999)
            try:
                hospital.cancel_appointment(appointment_id)
                print("Appointment cancelled successfully.")
            except ValueError as error:
                print("Error:", error)

        elif choice == "5":
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 5.")


# ====================== Employee submenu ======================
def employee_menu(hospital):
    while True:
        print("\n--- Employee Management ---")
        print("1. Add employee")
        print("2. View all employees")
        print("3. Search employee by ID")
        print("4. Change employee salary")
        print("5. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = read_text("Name: ")
            age = read_int("Age (18-70): ", 18, 70)
            phone = read_phone("Phone number: ")
            print("Position: 1. Receptionist  2. Nurse  3. Pharmacist")
            position = EMPLOYEE_POSITIONS[read_int("Choose position: ", 1, 3) - 1]
            salary = read_amount("Salary: ")
            employee = hospital.add_employee(name, age, phone, position, salary)
            print(f"Employee added successfully. Employee ID = {employee.employee_id}")

        elif choice == "2":
            show_list(hospital.employees, "No employees found.")

        elif choice == "3":
            employee_id = read_int("Enter employee ID: ", 1, 999999)
            employee = hospital.find_employee(employee_id)
            if employee is None:
                print("Error: No employee found with that ID.")
            else:
                print(employee.get_details())

        elif choice == "4":
            employee_id = read_int("Enter employee ID: ", 1, 999999)
            employee = hospital.find_employee(employee_id)
            if employee is None:
                print("Error: No employee found with that ID.")
            else:
                new_salary = read_amount("New salary: ")
                try:
                    employee.set_salary(new_salary)   # uses the setter (encapsulation)
                    print("Salary updated. New salary =", employee.get_salary())
                except ValueError as error:
                    print("Error:", error)

        elif choice == "5":
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 5.")


# ====================== Billing submenu ======================
def billing_menu(hospital):
    while True:
        print("\n--- Billing System ---")
        print("1. Create bill for a patient")
        print("2. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            patient_id = read_int("Enter patient ID: ", 1, 999999)
            patient = hospital.find_patient(patient_id)
            if patient is None:
                print("Error: No patient found with that ID.")
                continue
            consultation = read_amount("Consultation charges: ")
            additional = read_amount("Additional hospital charges: ")
            try:
                bill = Bill(patient.patient_id, patient.name, consultation, additional)
                print("\n========== BILL ==========")
                print(bill.get_details())
                print("==========================")
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            break
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")


# ====================== Main program ======================
def main():
    hospital = Hospital("MediCare Hospital")

    while True:   # keeps running until the user chooses Exit
        print("\n========== MEDICARE HOSPITAL MANAGEMENT ==========\n")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Employee Management")
        print("5. Billing System")
        print("6. Exit")
        print("\n==================================================")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            patient_menu(hospital)
        elif choice == "2":
            doctor_menu(hospital)
        elif choice == "3":
            appointment_menu(hospital)
        elif choice == "4":
            employee_menu(hospital)
        elif choice == "5":
            billing_menu(hospital)
        elif choice == "6":
            print("Thank you for using MediCare. All data in memory is now cleared. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or closed input: leave politely instead of showing an error
        print("\nProgram closed. Goodbye!")
