import os, sys
import shutil

from write_csv import write_csv
from get_courses import get_courses
from generate_notebooks import generate_notebook
from college_of_science import get_majors

institution = "University of Arizona"
college = "College of Science"

majors = get_majors()
major_names = []

# majors = []
path = "../{}/".format(college.lower().replace(" ", "_"))

if os.path.exists(path):
    print("Removing old directory...")
    shutil.rmtree(path)

os.mkdir(path)

num_majors = 1
for major_name, dtype in majors:
    count = 0
    courses = []
    print(
        "Major: {} -- {}/{}\nScraping courses information...".format(
            major_name, num_majors, len(majors)
        )
    )
    while len(courses) == 0:
        if count == 10:
            print("Major name wrong, skip major:{} {}".format(major_name, dtype))
            major_name += "__ISSUE_FILE"
            break

        count = count + 1

        major_url = "{}{flag}".format(
            major_name.lower().replace(" ", "-").replace(":", "").replace(",", ""),
            flag="" if dtype == 0 or dtype == 3 else "-{}".format(dtype),
        )
        courses = get_courses(major_url)

    print("Generating CSV file...")

    major_name = major_name.replace(":", "").replace(",", "")
    write_csv(major_name, dtype, courses, path)

    num_majors = num_majors + 1
    major_names.append(major_name)

print("Generating Jupyter notebook for {}...".format(college))

generate_notebook(institution, college, major_names, path)

print("Done.")

