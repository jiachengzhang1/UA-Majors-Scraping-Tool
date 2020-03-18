from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


def get_courses(major):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    br = webdriver.Chrome(chrome_options=options)

    br.get("https://www.arizona.edu/degree-search/majors/major/{}".format(major))

    all_courses = []

    content = br.page_source
    soup = BeautifulSoup(content, "html.parser")

    # extract major curriculum from the website
    for semester in soup.findAll("div", {"class": "semester"}):
        # extract term information
        term = semester.find("div", {"class": "semester-course-heading"}).text
        term_num = term[0:1]

        course = semester.findAll("div", {"class": "semester-course"})
        credit = semester.findAll("div", {"class": "semester-credit"})
        courses = [
            (course.text.replace("\xa0", " "), credit.text)
            for course, credit in zip(course, credit)
        ]

        for course, credit in courses:

            # extract course information
            name = course

            if name == "Calculus I":
                name = "MATH 122A/B " + name
                credit = 4

            info = name.split(" ")
            info = [s for s in info if s != "" and s != "-"]

            prefix = ""
            num = ""

            # The courses with details
            if len(info) > 2:
                sec_indx = info[1]
                if sec_indx[0:1].isnumeric():
                    prefix = info[0]
                    num = info[1]
                    name = " ".join(info[2:])

            # name, prefix, number, credit, term
            course_tuple = (name, prefix, num, credit, term_num)
            # print(course_tuple)

            all_courses.append(course_tuple)

    # print(all_courses)
    return all_courses
