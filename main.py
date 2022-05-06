
## "https://sdsu.beta.instructure.com/"

import json
from datetime import date, datetime
from canvasapi import Canvas
import requests as req


currentYear = date.today().year
springStartDate = datetime.strptime(str(currentYear) + "-01-01", '%Y-%m-%d').date()
fallStartDate = datetime.strptime(str(currentYear) + "-08-01", '%Y-%m-%d').date()

apiURL = "<API URL>"

apiKey = "<API KEY>"
canvas = Canvas(apiURL, apiKey)

account = canvas.get_account(1)
courses = account.get_courses()

# Empty lists to store the course IDs and their SIS IDs for all courses
courseIDs = []
sisID = []

# Empty list to store only the course IDs of based on the input
searchedIDList = []

# List of course codes that the user likes to crosslist
courseIDsToCrossList = []

# Open the JSON file an d parse all the SIS IDs and the Course IDs into the designated empty list

with open('data.json', 'r') as f:
    courseDict = json.load(f)
    for i in courseDict:
        sis = i['SIS ID']
        courseID = i['ID']
        sisID.append(sis)
        courseIDs.append(courseID)

SISIDInput = input("Enter a SIS ID for your new shell: ").upper()


def stripSISID(s):
    s = s.split('-')
    return s[0]


crs = stripSISID(SISIDInput)

try:
    print("List of Sections: ")
    temp1 = []
    temp2 = []
    for c, i in zip(sisID, courseIDs):
        if c.startswith(crs):
            if c.endswith('Spring' + str(currentYear)):
                temp1.append(c)
                temp2.append(i)

    if len(temp1) == 0:
        print("No Sections Available.")
    else:
        for c, i in zip(temp1, temp2):
            print('SIS ID: ', c, '', 'Course ID: ', i)
            searchedIDList.append(i)

except:
    print("Error. Please try again later.")


def createShell(sis_id):
    # Function to create an empty shell
    shell = account.create_course()
    tempList = sis_id.split('-')
    course_code = tempList[0]
    section = str(tempList[1])
    name = course_code + '-' + section + '-' + 'Spring' + str(currentYear)
    shell.update(
        course={'course_code': course_code, 'name': name, 'sis_course_id': sis_id, 'term_id': 160,
                'id': shell.id})
    return shell


# Create a function for cross-listing.
def crossList(sectionID, newCourseID):
    ## data = {'id':sectionID,'new_course_id':newCourseID}
    header = {'Authorization': 'Bearer "<API KEY>"'}

    url = "https://sdsu.beta.instructure.com:443/api/v1/sections/{}/crosslist/{}".format(sectionID, newCourseID)
    resp = req.post(url, headers=header)
    return resp.status_code


# Create new Shell


try:
    print("Creating new shell.")
    newShell = createShell(SISIDInput)
    print("Shell Created:", newShell.name)
    print()
except:
    print("Error. Cannot create a shell.")
    print()

# Function to create a new section

def createSection(courseID):
    try:
        theCourse = canvas.get_course(courseID)
        sections = theCourse.create_course_section()
        print(sections)
        return None


    except:
        return "Error. Cannot create a new section for the shell."


# Extract section IDs from the courses. If section ID is not available, then ignore that course.

for x in searchedIDList:

    for y in canvas.get_course(x).get_sections():
        if y.id is not None:
            newCrossListedSection = crossList(y.id, newShell.id)
            print(newCrossListedSection)
            print("Course ID: ", canvas.get_course(x))
            print("Section ID: ", y.id)
        else:
            print("No section ID found for: ",x)

print(newShell.id)




