import json

SUBJECTS = ["English", "Math", "Sport", "Biology"]


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
    average_grade = round(sum(grade_list) / len(grade_list),2)
    print(f"Student: {name}, Best Grade: {best_grade}, Average Grade: {average_grade}")


def create_student_dictionary(name: str, grades: list ) -> dict:
  student_dict = {"Name": name}
  for subject, grade in grades:
    student_dict[subject] = grade
  return student_dict


def check_user_input(grade: str) -> bool:
  if grade.isdigit(): # i dont allow decimal input.
    if 0 <= int(grade) <= 100: # The demo allows negative input and input bigger than 100. In reality that doesn't make sense.
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


if __name__ == "__main__":
    main()