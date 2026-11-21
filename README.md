
import streamlit as st
import json

st.title("Health Insurance Question & Answer Tool")
st.write("Ask questions about your UnitedHealthcare insurance plan.")

# Load the insurance information
with open("insurance_data.json", "r") as file:
    insurance_data = json.load(file)

text = insurance_data["pdf_text"]

# Ask the user a question
question = st.text_input("Ask a question about your insurance plan:")

if question:
    q = question.lower().strip()

    # Question 1: Deductible
    if "deductible" in q:
        answer = (
            "Your overall deductible is $500 for an individual "
            "and $1,000 for a family."
        )

    # Question 2: Out-of-pocket limit
    elif "out-of-pocket" in q or "out of pocket" in q:
        answer = (
            "Your out-of-pocket limit is $7,000 for an individual "
            "and $14,000 for a family."
        )

    # Questions 3 and 7: Emergency room
    elif "emergency" in q or "er visit" in q:
        answer = (
            "An emergency room visit has a $600 copay per visit."
        )

    # Questions 4 and 9: Specialist
    elif "specialist" in q:
        answer = (
            "An in-network specialist visit has a $75 copay per visit."
        )

    # Question 5: Urgent care
    elif "urgent" in q:
        answer = (
            "An in-network urgent care visit has a $50 copay per visit."
        )

    # Question 6: Primary care
    elif "primary care" in q:
        answer = (
            "An in-network primary care visit has a $15 copay per visit. "
            "Out-of-network visits are not covered."
        )

    # Question 8: Outpatient surgery
    elif "outpatient surgery" in q:
        answer = (
            "Outpatient surgery at an ambulatory surgery center has a "
            "$300 facility copay per service. Physician or surgeon fees "
            "are listed as no charge in that setting. Hospital outpatient "
            "surgery may cost $300 or $450 per date of service, depending "
            "on the setting. Preauthorization may be required."
        )

    # Question 10: Diagnostic tests
    elif "diagnostic test" in q:
        answer = (
            "Diagnostic test costs depend on the test and location. "
            "Blood work at a freestanding facility or office has a "
            "$10 copay per service. X-rays and other diagnostic testing "
            "at those locations have a $100 copay per service. "
            "Hospital-based testing may have different copays. "
            "Preauthorization may be required."
        )

    # Questions the program doesn't recognize
    else:
        answer = (
            "Sorry, I couldn't find an answer to that question "
            "in this insurance plan."
        )

    st.write("ANSWER:", answer)
