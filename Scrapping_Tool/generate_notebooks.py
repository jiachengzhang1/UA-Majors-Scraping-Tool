import nbformat as nbf


def generate_notebook(institution, college, majors, path):

    nb = nbf.v4.new_notebook()

    text = (
        "# <center>{} Curricula - {}</center>\n\n".format(college, institution)
        + "This notebook contains a prelmininary analyses of the curricula and degree plans associated"
        + "with the undergradatue programs in the {} at the {}. ".format(
            college, institution
        )
        + "In order to execute the analyses provided in this notebook, "
        + "you need to load the following Julia packages:"
    )

    nb["cells"].append(nbf.v4.new_markdown_cell(text))

    code = (
        "using CurricularAnalytics"
        + "using Glob\n"
        + "using CSV\n"
        + "using DataFrames\n"
        + "using Statistics"
    )

    nb["cells"].append(nbf.v4.new_code_cell(code))

    text = (
        "## Curricular Analytics Toolbox\n\n"
        + "The analyses in this notebook makes use of the Curricular Analytics toolbox built "
        + "using the Julia programming language and available as open source software [1]. "
        + "As a starting point, you may find it useful to read the toolbox documenation, "
        + "as well as the curricular analytics paper listed in the References section below [2].\n\n"
        + "### Create the Data Structures\n"
        + "Degree plans associated with four different disciplines (animal science, mechanical engineering, "
        + "music education, and psychology) were collected from each of the eleven schools in the cluster. "
        + "The degree plans were stored as CSV files using the format for degree plans specified in the Curricular Analytics toolbox.  "
        + "The files are organized in a directory structure that is assumed to be in the same directory as this notebook as follows:  `"
        + "./programs/<college-name>/`\n\n"
        + "Asuuming the aforementioned directory structure, we first create an dictionay called `plans` "
        + "containing the degree plans for each of the programs in a given college, in this case the {}.".format(
            college
        )
    )

    nb["cells"].append(nbf.v4.new_markdown_cell(text))

    code = (
        'college = "{}"\n'.format(college.lower().replace(" ", "_"))
        + "plans = Dict{String, DegreePlan}()\n"
        + 'program_files = glob("*", "./programs/$college")\n'
        + "for program in program_files\n"
        + "    dp = read_csv(program)\n"
        + "    complexity(dp.curriculum)  # compute the curricular complexity of the degree plan\n"
        + "    plans[dp.curriculum.name] = dp    # store the degree plan the dictionary\n"
        + "end\n"
    )

    nb["cells"].append(nbf.v4.new_code_cell(code))

    for major in majors:
        code = '{}_plan = plans["{}"]\nvisualize({}_plan, notebook=true)'.format(
            major.replace(" ", "_"), major, major.replace(" ", "_")
        )

        nb["cells"].append(nbf.v4.new_code_cell(code))

    text = (
        "## References\n"
        + "<a id='References'></a>\n\n"
        + "[1] Heileman, G. L., Abdallah, C.T., Slim, A., and Hickman, M. (2018). "
        + "Curricular analytics: A framework for quantifying the impact of curricular "
        + "reforms and pedagogical innovations. www.arXiv.org, arXiv:1811.09676 [cs.CY].\n\n"
        + "[2] Heileman, G. L., Free, H. W., Abar, O. and Thompson-Arjona, W. G, (2019). "
        + "CurricularAnalytics.jl Toolbox. https://github.com/heileman/CurricularAnalytics.jl."
    )
    nb["cells"].append(nbf.v4.new_markdown_cell(text))

    nbf.write(nb, "{}/{}-curricula.ipynb".format(path + "/../", "Arizona"))

