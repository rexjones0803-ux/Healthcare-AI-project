import streamlit as st
import json

st.title("Health Insurance Question & Answer Tool")
st.write("Ask basic questions about your UnitedHealthcare insurance plan.")

with open("insurance_data.json", "r") as file:
    insurance_data = json.load(file)

text = insurance_data["pdf_text"]

question = st.text_input("Ask a question about your insurance plan:")

if question:
    q = question.lower()

    if "dental implant" in q:
        st.write("Sorry, I couldn't find information about dental implants.")
    else:
        if "emergency" in q:
            search = "emergency room care"
        elif "urgent" in q:
            search = "urgent care"
        elif "specialist" in q:
            search = "specialist visit"
        elif "deductible" in q:
            search = "overall deductible"
        elif "out-of-pocket" in q:
            search = "out-of-pocket limit"
        else:
            search = q.replace("?", "").strip()

        matches = [
            line for line in text.splitlines()
            if search in line.lower()
        ]

        if matches:
            if "urgent" in q:
                answer = next(
                    (line for line in matches
                     if "urgent care" in line.lower()
                     and "copay" in line.lower()
                     and "plan type" not in line.lower()),
                    "Sorry, I couldn't find the urgent care visit cost."
                )
            else:
                answer = next(
                    (line for line in matches if "$" in line),
                    matches[0]
                )
            st.write("ANSWER:", answer)
        else:
            st.write("Sorry, I couldn't find an answer.")
