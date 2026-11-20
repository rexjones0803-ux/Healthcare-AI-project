
import pdfplumber
from pathlib import Path

pdf_files = list(Path("pdfs").glob("*.pdf"))

keywords = [
    "overall deductible",
    "out-of-pocket limit",
    "emergency room care"
]

insurance_data = {"plan_name": "UnitedHealthcare", "pdf_text": ""}

if not pdf_files:
    print("ERROR: No PDF found.")
else:
    with pdfplumber.open(pdf_files[0]) as pdf:
#print("UnitedHealthcare Insurance Analysis")
        #print("Total pages:", len(pdf.pages))

        for keyword in keywords:
#print("\nSEARCHING FOR:", keyword.upper())

            for page_number, page in enumerate(pdf.pages, start=1):
                text = page.extract_text() or ""
                insurance_data["pdf_text"] += text + "\n"
#print("EXTRACTED TEXT:", text[:500])
                lines = text.splitlines()

                for index, line in enumerate(lines):
                    if keyword in line.lower():
                    #print("\nPDF Page:", page_number)
#print("MATCH:", line)

                        if index + 1 < len(lines):
                           pass

import json



with open("insurance_data.json", "w") as file:
    json.dump(insurance_data, file, indent=4)

    question = input("Ask a question about your insurance plan: ")
words = [word for word in question.lower().replace("?", "").split() if word not in ["what", "is", "my", "does", "insurance", "cover", "the", "a", "an", "how", "much"]]
text = insurance_data["pdf_text"]
#print("SEARCH WORDS:", words)
#print("SEARCH WORDS:", words)
if "emergency" in question.lower():
    words = ["emergency room"]
matches = [
    line for line in text.splitlines()
    if all(word in line.lower() for word in words if len(word) > 3)
]

if matches:
  print("ANSWER:", next((line for line in matches if "$" in line), matches[0]))
else:
    print("Sorry, I couldn't find an answer.")