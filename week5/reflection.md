# Reflection

The AI review helped identify several issues that I had not fully
considered in my initial requirements. One important point was that some
requirements were ambiguous or difficult to test. For example, NFR-03
stated that the system should be usable after a "brief walkthrough," but
this phrase is not clearly measurable and would require clarification
from the client. The AI also highlighted edge cases, such as what should
happen when a receptionist attempts to cancel a non-existent or already
cancelled appointment. These questions improved the quality of the
requirements because they exposed situations that were not explicitly
covered.

However, the AI also made suggestions that went beyond the evidence
provided in the client brief. For example, it suggested that cancelled
appointments should always be retained with a "cancelled" status rather
than being deleted. While this is a reasonable idea, it was not directly
stated by the client and therefore remains an assumption requiring
validation.

One requirement that changed after review was the handling of cancelled
appointments. Instead of accepting the AI suggestion as a confirmed
requirement, I documented it as an assumption and identified it as
something that should be clarified with the client.

Requirements must have evidence because AI can generate suggestions
based on common industry practices rather than actual client needs.
Evidence ensures that requirements are traceable, justified, testable,
and aligned with the client's stated problems and goals.

## AI Tool Use

Only GitHub Copilot was used for AI assistance where applicable. The
conditions and instructions provided for the task were followed when
using the AI tool. AI suggestions were reviewed by me rather than being
accepted automatically, and decisions were made based on the available
client evidence and the assessment requirements.
