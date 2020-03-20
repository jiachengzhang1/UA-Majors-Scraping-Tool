

user_quit = False

courses = []

while not user_quit:
    course_name = input("Course Name:\n")
    course_prefix = input("Course Prefix:\n")
    course_number = input("Course Number:\n")

    done = False
    prerequisites = []
    while not done:
        course_pre = input(
            "Course Prerequisites (In format of <Prefix>-<Number>):\n")
        course = course_pre.split("-")
        prerequisites.append((course[0], course[1]))

    corequisites = []
    while not done:
        course_co = input(
            "Course Corequisites (In format of <Prefix> <Number>):\n")
        course = course_co.split(" ")
        corequisites.append((course[0], course[1]))

    strict_corequisites = []
    while not done:
        course_strict = input(
            "Course Strict-Corequisites (In format of <Prefix> <Number>):\n")
        course = course_strict.split(" ")
        strict_corequisites.append((course[0], course[1]))

    course_credit = input("Course Credit Hours:\n")

    courses.append('{"name": {}, "prefix": {}, "number": {}, "pre": {}, "co": {}, "strict":{}, "credit": {}}'.format(
        course_name, course_prefix, course_number, course_pre, course_co, course_strict, course_credit))
