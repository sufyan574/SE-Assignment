import PyPDF2

pdf_path = "fw7.pdf"

field_map = {
    "f1_07": "First Name",
    "f1_08": "Middle Name",
    "f1_09": "Last Name",
    "f1_13": "Street Address",
    "f1_14": "City",
    "f1_16": "State",
    "f1_17": "Date of Birth",
    "f1_18": "Country of Birth",
    "f1_19": "City of Birth",
    "f1_25": "Passport Number",
    "f1_26": "Passport Expiry",
}

with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)

    print("\n========= PDF NORMAL TEXT =========\n")
    for page in reader.pages:
        text = page.extract_text()
        if text:
            print(text)

    fields = reader.get_fields()

    print("\n========= FILLED FORM DATA (Readable) =========\n")
    if fields:
        for key, field in fields.items():
            value = field.get("/V")

            clean_key = key.split("[")[0]

            readable = field_map.get(clean_key, clean_key)

            if value not in [None, ""]:
                print(f"{readable}: {value}")
    else:
        print("No form fields found.")
