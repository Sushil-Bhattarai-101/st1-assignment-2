## Design Decisions

The hardest decision was whether to include a separate **Clinic** class. Although it was not explicitly listed in the requirements like **Patient**, **Practitioner**, and **Appointment**, I decided to keep it because functions such as viewing appointments, searching, and counting require one class to manage the collections.

The AI initially suggested additional classes such as **PatientManager**, **PractitionerManager**, **ClinicController**, and **NotificationManager**. However, these either duplicated responsibilities already handled by the existing classes or introduced features, such as notifications, that were not required. Including them would have added unnecessary complexity.

My final design decisions were based on the requirements. Each class and relationship was checked against a specific requirement. If a class or feature could not be justified by a requirement, I rejected or modified it. This helped keep the model simple, focused, and aligned with the clinic's actual needs.