#This is the class course
class Course:

    def __init__(self, course_code, instr_type, section, crn, days, time, instructor):
        self.__course_code = course_code
        self.__instr_type = instr_type
        self.__section = section
        self.__crn = crn
        self.__days = days
        self.__time = time
        self.__instructor = instructor

    def __str__(self):
        return ('%s %s %s %s %s %s %s') % (self.__course_code, self.__instr_type, self.__section, self.__crn, self.__days,self.__time, self.__instructor)


