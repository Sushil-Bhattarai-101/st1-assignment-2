Copilot Respose: 
# Part C - Use AI as Tutor

1)what the code does:
->The program is a simple clinic appointment booking system that collects appointment details, prevents scheduling conflicts for practitioners, stores appointments, and displays them at the end.

2) Three limitations:
i)Date and time are not validated
(The program accepts any text as a date or time.)
ii) Data is lost when the program closes
(Appointments are stored only in memory:)
iii) Name matching is case-sensitive
(this means: Dr Brown & dr brown are considered diffrent practitioners.)

3) Suggested improvements:
Improvement 1: Validate date and time format

Use Python's datetime module to ensure users enter dates and times correctly.

Benefit:
Prevents invalid entries.
Makes scheduling more reliable.

Improvement 2: Standardize names

Convert practitioner names to a consistent format before comparison.

Example:
practitioner_name = practitioner_name.strip().title()

Benefit:
Reduces duplicate entries caused by different capitalisation or extra spaces.

5) Ask me two questions to test my understanding.
Question 1
Suppose the appointment list already contains:
{
"patient": "John",
"practitioner": "Dr Brown",
"date": "2026-09-10",
"time": "10:00"
}

What will happen if another patient tries to book Dr Brown on 2026-09-10 at 10:00?
ans:-> The appointment will not be available because the program detects that Dr Brown already has an appointment on 2026-09-10 at 10:00

Question 2
Why does the function use:
return
"Details cannot be empty."

ans;-> The return statement is used to stop the function when required details are empty
------------------------------------------------------------
# Part D Generate an Alternative: AI ON

# List to store all appointments
appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    """
    Stores appointment details in the appointments list.
    """

    # Create a dictionary for one appointment
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Add the appointment to the list
    appointments.append(appointment)

    print("Appointment added successfully.")


# Example usage
add_appointment("John Smith", "Dr Brown", "10:00 AM")
add_appointment("Sarah Jones", "Dr Wilson", "2:30 PM")

# Display all appointments
print("\nAppointments:")
for appointment in appointments:
    print(appointment)
    --------------------------------------------

# Part F -Verify Behaviour
• Normal appointment
Appointment booked successfully.
• Blank patient name
Details cannot be empty.
• Two appointments for the same practitioner/time
This appointment slot is already booked. Please choose a diffent time
• Strange input such as patient_name=None or appointment_time=None
Details cannot be empty.

# Part G- Improved Thing!
Previous code:
practitioner_name = input("Enter your practitioner's name: ")

Improved code:
practitioner_name = input("Enter your practitioner's name: ").strip().title()

Result: 
.strip() removes extra spaces at the beginning and end.
.title() converts the name to title case.