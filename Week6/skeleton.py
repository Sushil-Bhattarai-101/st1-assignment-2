# SmartCare Domain class skeletons (Week 6)

class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def get_name(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name

    def get_name(self):
        pass

    def has_conflict(self, date, time):
        pass


class Appointment:
    def __init__(self, patient, practitioner, date, time):
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = "scheduled"

    def cancel(self):
        pass

    def conflicts_with(self, other):
        pass


if __name__ == "__main__":
    patient = Patient("P001", "John Smith")
    practitioner = Practitioner("D001", "Dr Brown")
    appointment = Appointment(patient, practitioner, "2026-10-01", "10:00")

    print("Patient:", patient.name)
    print("Practitioner:", practitioner.name)
    print("Appointment:", appointment.date, appointment.time, appointment.status)