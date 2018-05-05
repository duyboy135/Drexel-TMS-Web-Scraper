#This script get all course in summer term
from get_info import getCourse

#Loop through all crn number
for crn in range(40000, 43000):
    course = getCourse('4', str(crn))
    if course != 'Invalid_Course':
        print(course)


