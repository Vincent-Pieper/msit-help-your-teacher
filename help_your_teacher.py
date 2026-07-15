SUBJECTS = ["English", "Math"]  # can be expanded for more subjects


def print_failing_grades(failing_grades: dict, total_failing_grades: int):
    print("\nFailing grades per student:")
    for student in failing_grades:
        print(f"{student}: {failing_grades[student]} failing grade(s)")
    print(f"\nTotal number of failing grades across all students: {total_failing_grades}")


def calculate_failing_grades(student_data: list) -> tuple[dict, int]:
    failing_grades = {}
    total_failing_grades = 0

    for student in student_data:
        name = student["Name"]
        failing_grades[name] = 0

        for subject in SUBJECTS:
            if student[subject] <= 55:
                failing_grades[name] += 1
                total_failing_grades += 1

    return failing_grades, total_failing_grades


def print_averages(average: dict, overall: float):
    print("\nAverage grades per subject:")
    for subject, average_grade in average.items():
        print(f"{subject}: {average_grade:.2f}")
    print(f"\nOverall average grade across all subjects: {overall:.2f}")


def separate_subjects_from_overall(averages: dict) -> tuple[dict, float]:
    overall_average_grade = averages.pop("overall")  # original dict is changed!
    return averages, overall_average_grade


def get_average(grades: list) -> float:
    return round(sum(grades) / len(grades), 2)


def collect_averages(grades_per_subject: dict) -> dict:
    averages = {}
    for element in grades_per_subject:
        averages[element] = get_average(grades_per_subject[element])
    return averages


def collect_grades_by_subject(student_data: list) -> dict:
    data = {"overall": []}

    for subject in SUBJECTS:
        data[subject] = []

    for student in student_data:
        for subject in SUBJECTS:
            data[subject].append(student[subject])
            data["overall"].append(student[subject])

    return data


def calculate_average_grades(student_data: list) -> tuple[dict, float]:
    grades_per_subject = collect_grades_by_subject(student_data)
    averages = collect_averages(grades_per_subject)
    # "overall" is calculated together with the subjects first,
    # then separated because the output expects subject averages and overall average separately.
    return separate_subjects_from_overall(averages)


def get_list_of_grades(student: dict) -> list:
    grades_list = []
    for subject in SUBJECTS:
        grades_list.append(student[subject])
    return grades_list


def print_student_info(data: list):
    print()
    print("Student Information:")

    for student in data:
        name = student["Name"]
        grade_list = get_list_of_grades(student)
        best_grade = max(grade_list)
        average_grade = round(sum(grade_list) / len(grade_list), 2)

        print(f"Student: {name}, Best Grade: {best_grade}, Average Grade: {average_grade:.2f}")


def create_student_dictionary(name: str, grades: list) -> dict:
    student_dict = {"Name": name}
    for subject, grade in grades:
        student_dict[subject] = grade
    return student_dict


def check_user_input(grade: str) -> bool:
    if grade.isdigit():  # i dont allow decimal input.
        # This solution intentionally accepts only whole-number grades from 0 to 100.
        # This keeps the input within a realistic grading range.
        if 0 <= int(grade) <= 100:
            return True

    print("please type a number between 0 and 100")
    return False


def get_grades(subject: str) -> float:
    input_checked = False
    while not input_checked:
        grade = input(f"Enter {subject} grade: ")
        input_checked = check_user_input(grade)

    return float(grade)


def get_student_name(num: int) -> str:
    print(f"Enter details for student {num}")
    return input("Enter student name: ")


def get_student_info(num: int) -> dict:
    student_name = get_student_name(num)
    grades = []

    for subject in SUBJECTS:
        user_grade = get_grades(subject)
        grades.append((subject, user_grade))

    return create_student_dictionary(student_name, grades)


def get_amount_of_new_entries() -> int:
    input_check = False

    while not input_check:
        new_entries = input("Enter the number of students: ")
        if new_entries.isdigit() and int(new_entries) > 0:
            input_check = True

    return int(new_entries)


def main():
    new_entries = get_amount_of_new_entries()
    student_data = []

    for num in range(0, new_entries):
        print()
        student_dict = get_student_info(num + 1)
        student_data.append(student_dict)

    print_student_info(student_data)
    average_grades_per_subject, overall_average_grade = calculate_average_grades(student_data)
    print_averages(average_grades_per_subject, overall_average_grade)

    failing_grades, total_failing_grades = calculate_failing_grades(student_data)
    print_failing_grades(failing_grades, total_failing_grades)


if __name__ == "__main__":
    main()