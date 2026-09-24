# Reflection

**Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?**

I rejected the SQL inside `cancel()` and the `NotificationManager` dependency, because neither was in the approved UML or supported by a requirement -- they would have added scope the client never asked for. I modified the inheritance from `PatientRecord` into a normal reference, since `Appointment` is not a kind of Patient. AI's version also exposed status as something any code could set directly with no check at all; I kept status as a plain attribute for simplicity, but every place that changes it (`cancel_appointment()`, the conflict check in `add_appointment()`) still runs through a method that checks it first, rather than being set from outside with no logic at all.

The approved design constrained the AI by giving it a fixed shape to fill in: exact class names, attributes, and method behaviour from the UML, plus explicit rules ("no database, UI, notification or service classes"). This meant any extra class the AI added stood out immediately as something to reject, instead of me having to judge the whole design from scratch.
