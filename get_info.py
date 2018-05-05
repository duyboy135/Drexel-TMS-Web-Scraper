#Duy Nguyen (duyboy135)
#5/5/2018

import requests
from bs4 import BeautifulSoup
from course import Course


#This function returns a 'Course' with a specific term and crn
def getCourse(term = '4', crn = '11029'):
    url = 'https://termmasterschedule.drexel.edu/webtms_du/app'

    data = {
        'formids': 'term,courseName,crseNumb,crn',
        'component': 'searchForm',
        'page': 'Home',
        'service': 'direct',
        'term': term,
        'crn': crn
    }
    #Parse the html file, find the table containing all necessary information
    r = requests.post(url = url, data = data)
    soup = BeautifulSoup(r.text, 'html.parser')
    necessary_table = soup.find('table', bgcolor = "cccccc")
    necessary_table = BeautifulSoup(str(necessary_table), 'html.parser')
    info = necessary_table.tr.next_sibling.next_sibling.td

    #Travel through the table to get all necessary information
    cursor = info
    try:
        #Get the code of the course
        course_code = cursor.text
        cursor = cursor.next_sibling.next_sibling
        course_code += (' ' + cursor.text)

        #Get instr_type
        cursor = cursor.next_sibling.next_sibling
        instr_type = cursor.text

        #Get section
        cursor = cursor.next_sibling.next_sibling
        section = cursor.text

        #Get_crn
        cursor = cursor.next_sibling.next_sibling
        crn = cursor.text

        # Get_time/days
        cursor = cursor.next_sibling.next_sibling.next_sibling.next_sibling
        days = cursor.table.tr.td.text
        times = cursor.table.tr.td.next_sibling.next_sibling.text

        #Get Instructors
        cursor = cursor = cursor.next_sibling.next_sibling
        instructors = cursor.text
        instructors = instructors.split(', ')

        return Course(course_code, instr_type, section, crn, days, times, instructors)

    except:
        return "Invalid_Course"
    
if __name__ == '__main__':
    print(getCourse())