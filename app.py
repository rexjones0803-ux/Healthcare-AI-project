
import streamlit as st
import json
import re

st.title("Health Insurance Question & Answer Tool")
st.write("Ask questions about your UnitedHealthcare insurance plan.")

# Load insurance information
with open("insurance_data.json", "r") as file:
    insurance_data = json.load(file)

text = insurance_data["pdf_text"]

# Find and format insurance costs
def find_cost(keyword, service):
    for line in text.splitlines():
        if keyword in line.lower():

            copay = re.search(
                r"(\$[\d,]+)\s*copay\s*/\s*(visit|service|day)",
                line,
                re.IGNORECASE
            )

            if copay:
                amount = copay.group(1)
                unit = copay.group(2)

                return (
                    f"The listed copay for {service} "
                    f"is {amount} per {unit}. "
                    "Other coverage conditions may apply."
                )

            coinsurance = re.search(
                r"(\d+%)\s*coinsurance",
                line,
                re.IGNORECASE
            )

            if coinsurance:
                amount = coinsurance.group(1)

                return (
                    f"The listed coinsurance for {service} "
                    f"is {amount} of the covered cost."
                )

    return None


# Question input
question = st.text_input(
    "Ask a question about your insurance plan:"
)

if question:
    q = question.lower().strip()

    # Out-of-pocket limit
    if "out-of-pocket" in q or "out of pocket" in q:
        answer = (
            "Your out-of-pocket limit is $7,000 for an "
            "individual and $14,000 for a family."
        )

    # Deductible
    elif "deductible" in q:
        answer = (
            "Your overall deductible is $500 for an "
            "individual and $1,000 for a family."
        )

    # Emergency room
    elif "emergency room" in q or "er visit" in q:
        answer = (
            "An emergency room visit has a "
            "$600 copay per visit."
        )

    # Urgent care
    elif "urgent care" in q:
        answer = (
            "An in-network urgent care visit has "
            "a $50 copay per visit."
        )

    # Specialist visit
    elif "specialist" in q:
        answer = (
            "An in-network specialist visit has "
            "a $75 copay per visit."
        )

    # Primary care
    elif "primary care" in q:
        answer = find_cost(
            "primary care visit",
            "a primary care visit"
        )

        if not answer:
            answer = (
                "The primary care visit cost could not "
                "be verified from the extracted information."
            )

    # Outpatient surgery
    elif "outpatient surgery" in q:
        answer = (
            "In-network outpatient surgery has a $300 "
            "facility copay. Surgeon fees are $300 at "
            "an independent facility or $450 at a hospital. "
            "Applicable deductible requirements may apply."
        )

    # Diagnostic tests
    elif "diagnostic test" in q or "blood work" in q or "x-ray" in q:
        answer = (
            "In-network lab testing costs $10 at an office "
            "or independent lab and $65 at a hospital. "
            "X-rays cost $100 at an office or independent "
            "facility and $200 at a hospital. "
            "The deductible applies to X-rays but not "
            "lab testing. Out-of-network diagnostic tests "
            "are not covered. Prior authorization may "
            "be required."
        )

    # Unrecognized questions
    else:
        answer = (
            "Sorry, I could not find a reliable answer "
            "to that question in this insurance plan."
        )

    # Display the answer
    st.subheader("Answer")
    st.write(answer)

    st.caption(
        "Plan reference: UnitedHealthcare 2025 "
        "Summary of Benefits and Coverage."
    )
