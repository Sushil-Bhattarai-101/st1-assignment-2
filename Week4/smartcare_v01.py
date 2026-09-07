appointment = []

def add_appointment():
    print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
    patient_name = input("Enter your full name: ")
    practitioner_name = input("Enter your practitioner's name: ") .strip() .title()
    date = input("Enter the date of the appointment (YYYY-MM-DD): ")
    time = input("Enter the time of the appointment (HH:MM): ")

    # Check whether any values are empty.
    if not date or not time or not patient_name or not practitioner_name:
        print("Details cannot be empty.")
        return

    # Check whether the practitioner already has an appointment at this time.
    for appt in appointment:
        if (appt["practitioner"] == practitioner_name
                and appt["date"] == date
                and appt["time"] == time):
            print("This appointment slot is already booked. Please choose a different time.")
            return

    appointment_record = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "date": date,
        "time": time,
    }
    appointment.append(appointment_record)
    print("Appointment booked successfully.")

def display_appointments():
    if not appointment:
        print("No appointments recorded.")
        return
    print("Appointments:")
    for appt in appointment:
        print(f"Patient: {appt['patient']}, Practitioner: {appt['practitioner']}, Date: {appt['date']}, Time: {appt['time']}")


while True:
    add_appointment()
    again = input("Add another appointment? (y/n): ")
    if again.lower() != 'y':
        break

print("List of appointments:")
display_appointments()
print("Thank you for using SmartCare: Community Clinic Appointment Booking System!")
