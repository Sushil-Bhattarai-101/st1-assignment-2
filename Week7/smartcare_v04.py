class Patient:
    def __init__(self, name):
        self.name = name.strip().title()


class Practitioner:
    def __init__(self, name):
        self.name = name.strip().title()


class Appointment:
    def __init__(self, patient, practitioner, date, time):
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = "scheduled"

    def cancel(self):
        self.status = "cancelled"


class Clinic:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, patient_name, practitioner_name, date, time):
        patient = Patient(patient_name)
        practitioner = Practitioner(practitioner_name)

        # Check whether any values are empty.
        if not date or not time or not patient.name or not practitioner.name:
            print("Details cannot be empty.")
            return

        # Checking whether already booked appointment exists for the same practitioner at the same date and time.
        for appt in self.appointments:
            if (appt.practitioner.name == practitioner.name
                    and appt.date == date
                    and appt.time == time
                    and appt.status == "scheduled"):
                print("This appointment slot is already booked. Please choose a different time.")
                return

        new_appt = Appointment(patient, practitioner, date, time)
        self.appointments.append(new_appt)
        print("Appointment booked successfully.")

    def cancel_appointment(self, appointment):
        if appointment.status == "cancelled":
            print("Appointment is already cancelled.")
            return
        appointment.cancel()
        print("Appointment cancelled.")

    def count_appointments(self):
        return len(self.appointments)

    def display_appointments(self):
        if not self.appointments:
            print("No appointments recorded.")
            return
        print("Appointments:")
        for appt in self.appointments:
            print(f"Patient: {appt.patient.name}, Practitioner: {appt.practitioner.name}, "
                  f"Date: {appt.date}, Time: {appt.time}, Status: {appt.status}")



if __name__ == "__main__":
    clinic = Clinic()
    print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

    while True:
        patient_name = input("Enter your full name: ")
        practitioner_name = input("Enter your practitioner's name: ")
        date = input("Enter the date of the appointment (YYYY-MM-DD): ")
        time = input("Enter the time of the appointment (HH:MM): ")

        clinic.add_appointment(patient_name, practitioner_name, date, time)

        again = input("Add another appointment? (y/n): ")
        if again.lower() != 'y':
            break

    print("List of appointments:")
    clinic.display_appointments()
    print("Thank you for using SmartCare: Community Clinic Appointment Booking System!")