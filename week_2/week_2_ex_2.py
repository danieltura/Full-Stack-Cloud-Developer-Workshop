from os import supports_dir_fd
from turtle import st


COMMANDS = ["SEARCH", "ADD", "LIST", "DELETE", "UPDATE", "EXIT"]

STUDENT_RECORDS = []


def get_number_input(message, error_message):
    user_input = None
    is_input = False
    while is_input == False:
        try:
            user_input = float(input(message))
            is_input = True
        except Exception as e:
            print(error_message)
    return user_input


def get_command(commands):
    print("\nPlease Enter A Number For The Command You Wish To Excute:")
    for indx, command in enumerate(commands):
        print(command + ": " + str(indx + 1))

    error_message = (
        "Please enter numbers between 1 and " + str(len(commands)) + " inclusive.\n\n"
    )
    return int(get_number_input("\nYour Input: ", error_message))


def find(param, value):
    is_found = False

    for idx, student in enumerate(STUDENT_RECORDS):
        if student[param] == value:
            is_found = True
            grade, name = student.values()
            print(f"Student Found:\t Name: {name} \t Grade: {grade}")
            return (student, idx)

    if not is_found:
        print("No record found by the given input: " + str(value) + "\n")


def SEARCH():
    while True:
        print("Search By: \nName : 1 \nGrade: 2")
        search_option = int(
            get_number_input("Your Search Key: ", "Please Enter Number only:")
        )

        if search_option == 1:
            name = input("Name:")
            find("name", name)
            break

        if search_option == 2:
            grade = get_number_input("Grade: ", "Please Enter Number only:")
            find("grade", grade)
            break

        print("\nError, Only 1 or 2 Allowed")

    return True


def ADD():
    name, grade = None, None
    is_input = False

    while is_input == False:
        try:
            name = input("Please enter student name:  ")
            if name.strip() == "":
                continue

            # assuming the grade is 0 -100
            grade = get_number_input(
                "Please enter student's grade from 1 - 100:  ",
                "\nError, Please enter only number in grade input.\n\n",
            )

            if 1 <= grade <= 100:
                is_input = True
            else:
                print("\nError, Please Enter Grade B/N 1 and 100\n")

        except Exception as e:
            print("\nError, Please enter only number in grade input.\n\n")

    STUDENT_RECORDS.append({"grade": grade, "name": name})
    print("Student Added.\n")

    return True


def UPDATE():
    search_name = input("Please Enter Name Of The Student: ")
    student = find("name", search_name)

    new_grade = get_number_input(
        "\nPlease, Enter A New Grade: ", "Please Enter Number only:"
    )

    STUDENT_RECORDS[student[1]]["grade"] = new_grade
    print("Student Grade Updated.")
    return True


def DELETE():
    search_name = input("Please Enter Name Of The Student You Wish To Delete: ")
    student = find("name", search_name)

    while True:
        confirm = input("\nAre You Sure You Want To Delete This Student ^ (Y/N) : ")
        if confirm.upper() == "Y":
            print(f"{search_name} Deleted.")
            STUDENT_RECORDS.pop(student[1])
            break
        if confirm.upper() == "N":
            break
        print("Error, Please Enter Y or N Only.")

    return True


def LIST():
    print("\nStudent Records:")
    print(STUDENT_RECORDS)
    return True


def EXIT():
    print("DONE!!!\n")
    return False


def student_grade_system():
    is_done = True
    while is_done == True:
        choice = get_command(COMMANDS)
        indx = choice - 1

        is_done = eval(COMMANDS[indx] + "()")


if __name__ == "__main__":
    student_grade_system()
