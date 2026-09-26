COURSES = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0),
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5),
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5),
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5),
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5),
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5),
    ],
    7: [
        ("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5),
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5),
    ],
}


def marks_to_grade_points(marks: int) -> float:
    """Convert a numeric mark out of 100 into its PUCIT grade point using the
    official grade band. Use this whenever a student gives you raw marks for
    a course and you need the grade point before calculating a GPA."""

    if marks > 100 or marks < 0:
        return "Error: Input marks should be between 0-100"
    elif marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0


def calculate_semester_gpa(
    grade_points: list[float], credit_hours: list[float]
) -> float:
    """Calculate one semester's GPA from a list of grade points and the matching
    list of credit hours. Use this once you have grade points and credit hours
    for every course in a semester and need the credit-weighted average."""

    if len(grade_points) != len(credit_hours):
        return "Error: The length of grade points should be equal to credit hours"
    if sum(credit_hours) <= 0:
        return "Error: Credit hours can not be 0 or negative"

    total_ch = sum(credit_hours)
    temp_gpa = sum(i * j for i, j in zip(grade_points, credit_hours))
    final_gpa = temp_gpa / total_ch
    return final_gpa


def calculate_new_cgpa(
    current_cgpa: float,
    completed_credit_hours: float,
    semester_gpa: float,
    semester_credit_hours: float,
) -> float:
    """Project a student's new CGPA after adding one semester's GPA to their
    existing record. Use this when the student already has a CGPA and completed
    credit hours, and wants to know where they will stand after an upcoming or
    just-finished semester."""

    if completed_credit_hours <= 0 or semester_credit_hours <= 0:
        return "Error: Credit hours can not be negative or 0"

    new_cgpa = (
        current_cgpa * completed_credit_hours + semester_gpa * semester_credit_hours
    ) / (completed_credit_hours + semester_credit_hours)

    return new_cgpa


def required_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float,
) -> float:
    """Calculate the GPA a student needs to earn over their remaining credit
    hours to reach a target CGPA by graduation. Use this when the student names
    a CGPA goal and you know their current CGPA, completed credit hours, and how
    many credit hours they have left. The result can be above 4.0, which means
    the target is not reachable in that many remaining hours."""

    if target_cgpa > 4.0:
        return "Error: Target CGPA can not be above 4.0"
    if completed_credit_hours <= 0 or remaining_credit_hours <= 0:
        return "Error: Credit hours can not be negative or 0"

    required_gpa = (
        target_cgpa * (completed_credit_hours + remaining_credit_hours)
        - current_cgpa * completed_credit_hours
    ) / remaining_credit_hours

    return required_gpa


def get_semester_courses(semester: int) -> str:
    """Return the string containing courses and their credit hours for a given PUCIT
    BS(CS) semester (1 through 8). Use this when you need to know which courses
    and how many credit hours belong to a specific semester."""

    if semester < 1 or semester > 8:
        return "Error: Semester number should be between 1-8"

    course_list = COURSES[semester]
    final_str = f"{semester} Semester courses: "

    for course in course_list:
        s = f"{course[0]} - {course[1]} ({course[2]} credit hours) , "
        final_str += s

    return final_str


def get_remaining_credit_hours(current_semester: int) -> float:
    """Calculate the total credit hours left from the given semester through
    semester 8. Use this when you need to know how many credit hours a student
    has remaining before graduation, for example to work out a required GPA."""

    if current_semester < 1 or current_semester > 8:
        return "Error: Semester number should be between 1-8"

    remaining_ch = 0.0
    for i in range(current_semester, 9):
        course_list = COURSES[i]
        for course in course_list:
            remaining_ch += course[2]

    return remaining_ch


def save_report(filename: str, content: str) -> str:
    """Save a text report to disk under the given filename and confirm it was
    saved. Use this only after producing something worth keeping, like a GPA
    result or a graduation plan, and only when the student has asked for it
    to be saved."""

    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        with open(filename, "w") as f:
            f.write(content)

        return f"Report saved successfully in {filename}"
    except Exception as e:  # noqa: BLE001
        return f"Error: could not save report - {e}"
