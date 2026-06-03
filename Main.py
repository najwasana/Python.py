import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LAB 1: Student Registration
# -------------------------------
def student_registration():

    name = input("Enter Student Name: ")
    score = float(input("Enter Exam Score: "))

    if 90 <= score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("Remark:", remark)


# -------------------------------
# LAB 2: Course Enrollment
# -------------------------------
def course_enrollment():

    courses = []
    max_courses = 5

    print("\n=== Course Enrollment ===")

    while True:

        if len(courses) >= max_courses:
            print("Maximum Course Limit Reached")
            break

        course = input("Enter Course Name (or done): ")

        if course.lower() == "done":
            break

        credits = input("Enter Credits: ")

        if not credits.isdigit():
            print("Invalid Credit Value")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credits must be positive")
            continue

        courses.append((course, credits))

    print("\nEnrolled Courses")
    for c, cr in courses:
        print(c, "-", cr, "Credits")


# -------------------------------
# LAB 3: Student Records
# -------------------------------
def student_records():

    students = [
        {"name": "Priya", "age": 20, "grades": [85, 90, 78]},
        {"name": "Rahul", "age": 21, "grades": [72, 88, 91]},
        {"name": "Anita", "age": 19, "grades": [95, 89, 92]}
    ]

    print("\n=== Student Records ===")

    for s in students:
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Grades:", s["grades"])
        print()

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    print("\nEvent Analysis")
    print("Common Participants:", event_A & event_B)
    print("All Participants:", event_A | event_B)
    print("Only Event A:", event_A - event_B)


# -------------------------------
# LAB 4: Search and Sort
# -------------------------------
def search_sort_students():

    ids = [105, 102, 110, 108, 101, 115]

    print("\nOriginal IDs:", ids)

    n = len(ids)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ids[j] > ids[j + 1]:
                ids[j], ids[j + 1] = ids[j + 1], ids[j]

    print("Sorted IDs:", ids)

    target = int(input("Enter Student ID to Search: "))

    # Linear Search
    found = -1

    for i in range(len(ids)):
        if ids[i] == target:
            found = i
            break

    if found != -1:
        print("Linear Search: Found at index", found)
    else:
        print("Linear Search: Not Found")

    # Binary Search
    low = 0
    high = len(ids) - 1
    found = -1

    while low <= high:

        mid = (low + high) // 2

        if ids[mid] == target:
            found = mid
            break

        elif ids[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    if found != -1:
        print("Binary Search: Found at index", found)
    else:
        print("Binary Search: Not Found")


# -------------------------------
# LAB 5: Fee Calculation
# -------------------------------
def calculate_fee(tuition, hostel=0, transport=0):
    return tuition + hostel + transport


def fee_calculation():

    tuition = float(input("Enter Tuition Fee: "))
    hostel = float(input("Enter Hostel Fee: "))
    transport = float(input("Enter Transport Fee: "))

    total = calculate_fee(tuition, hostel, transport)

    print("Total Fee =", total)


# -------------------------------
# LAB 6: File Handling
# -------------------------------
def file_management():

    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")

    print("Records Written Successfully")

    with open("student_records.txt", "r") as file:
        records = file.readlines()

    print("\nStored Records")

    for r in records:
        print(r.strip())

    total = 0
    highest = -1
    topper = ""
    count = 0

    for r in records[1:]:

        data = r.strip().split(",")

        marks = int(data[2])

        total += marks
        count += 1

        if marks > highest:
            highest = marks
            topper = data[1]

    print("\nReport")
    print("Average Marks:", total / count)
    print("Topper:", topper)


# -------------------------------
# LAB 7: Directory Scanner
# -------------------------------
class MissingFileOrFolderError(Exception):
    pass


def scan_directory(path):

    try:

        if not os.path.exists(path):
            raise FileNotFoundError("Directory Not Found")

        print("\nDirectory Structure")

        for root, dirs, files in os.walk(path):

            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level

            print(indent + os.path.basename(root))

            for f in files:
                print(" " * 4 * (level + 1) + f)

            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty Folder Detected: {root}"
                )

    except FileNotFoundError as e:
        print(e)

    except MissingFileOrFolderError as e:
        print(e)

    except Exception as e:
        print("Unexpected Error:", e)


def directory_scanner():

    path = input("Enter Directory Path: ")
    scan_directory(path)


# -------------------------------
# LAB 8: Performance Analytics
# -------------------------------
def performance_analytics():

    data = {
        "Name": ["Arjun", "Meera", "Ravi", "Anita"],
        "Math": [85, 92, 76, 89],
        "Science": [80, 95, 72, 90],
        "English": [88, 91, 75, 85]
    }

    df = pd.DataFrame(data)

    print("\nRaw Data")
    print(df)

    print("\nStatistical Summary")
    print(df.describe())

    scores = df[["Math", "Science", "English"]].to_numpy()

    print("\nMean:", np.mean(scores, axis=0))
    print("Median:", np.median(scores, axis=0))
    print("Standard Deviation:", np.std(scores, axis=0))

    subjects = ["Math", "Science", "English"]
    means = np.mean(scores, axis=0)

    plt.figure()
    plt.bar(subjects, means)
    plt.title("Average Scores")
    plt.show()

    df.plot(x="Name",
            y=["Math", "Science", "English"],
            kind="bar")
    plt.title("Student Performance")
    plt.show()


# -------------------------------
# MAIN APPLICATION (LAB 9)
# -------------------------------
while True:

    print("\n")
    print("=" * 50)
    print(" SMART CAMPUS INFORMATION SYSTEM ")
    print("=" * 50)

    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Student Records")
    print("4. Search and Sort Student IDs")
    print("5. Fee Calculation")
    print("6. File Management")
    print("7. Directory Scanner")
    print("8. Performance Analytics")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        student_registration()

    elif choice == "2":
        course_enrollment()

    elif choice == "3":
        student_records()

    elif choice == "4":
        search_sort_students()

    elif choice == "5":
        fee_calculation()

    elif choice == "6":
        file_management()

    elif choice == "7":
        directory_scanner()

    elif choice == "8":
        performance_analytics()

    elif choice == "9":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
