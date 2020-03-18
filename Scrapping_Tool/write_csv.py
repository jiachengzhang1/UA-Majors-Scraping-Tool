from get_courses import get_courses


def write_csv(major, dtype, courses, path):

    headers = (
        "Curriculum,{},,,,,,,,,\n".format(major)
        + "Degree Plan,2019-20 Degree Plan,,,,,,,,,\n"
        + "Degree Type,{name},,,,,,,,,\n".format(name="BS" if dtype % 2 == 0 else "BA")
        + "System Type,semester,,,,,,,,,\n"
        + "CIP,14.2101,,,,,,,,,\n"
        + "Courses,,,,,,,,,,\n"
        + "Course ID,Course Name,Prefix,Number,Prerequisites,Corequisites,Strict-Corequisites,Credit Hours,Institution,Canonical Name,Term\n"
    )

    body = ""
    count = 0

    prereq = ""
    coreq = ""
    strict_coreq = ""

    for name, prefix, num, credit, term in courses:
        count += 1
        body += "{},{},{},{},{},{},{},{},,,{}\n".format(
            count, name, prefix, num, prereq, coreq, strict_coreq, credit, term
        )

    content = headers + body

    f = open(
        "{}/{}_{name}.csv".format(
            path, major.replace(" ", "_"), name="BS" if dtype % 2 == 0 else "BA"
        ),
        "w",
    )
    f.write(content)
    f.close()
