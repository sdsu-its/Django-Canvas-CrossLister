import json
from datetime import date

from canvasapi import Canvas

currentYear = date.today().year

apiURL = "https://sdsu.beta.instructure.com/"
apiKey = input("API KEY HERE: ")
canvas = Canvas(apiURL, apiKey)

account = canvas.get_account(1)
courses = account.get_courses()

data = []

for c in courses:
    if c.sis_course_id is not None:
        sis_idTerm = c.sis_course_id
        sis_idTerm = sis_idTerm.split("-")
        if len(sis_idTerm) == 3:
            if sis_idTerm[2].endswith(str(currentYear)):

                data.append({"SIS ID": c.sis_course_id, "Term": sis_idTerm[2], "ID": c.id})

                print("SIS ID:", c.sis_course_id)
                print("Term:", sis_idTerm[2])
                print("ID:", c.id)
                print()
            else:
                print("Skipping ", c.sis_course_id)
                print("")

toJSON = json.dumps(data, indent=2)
dataFile = open('data.json', 'w')
print(toJSON, file=dataFile)
dataFile.close()
