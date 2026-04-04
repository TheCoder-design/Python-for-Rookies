# Defining student grade
def get_grade(average):
    if average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


def main():
    # Collecting students grade
    students = []
    print("Welcome to the Student Grade System ")
    num_students = int(input("Enter the number of Students: "))
    for i in range(num_students):
        name = input(f"Enter name of Student{i + 1}: ").strip().title()
        marks1 = float(input("Enter marks for Physics: "))
        marks2 = float(input("Enter marks for Robotics: "))
        marks3 = float(input("Enter marks for Data Science: "))

        average = (marks1 + marks2 + marks3) / 3
        grade = get_grade(average)
        students.append({
            'name': name,
            'average': average,
            'grade': grade
        })

        print()

    # Display of the Students Grade
    print("--- Student Report ---")
    print("Name    Average     Grade ")
    total_average = 0
    for student in students:
        print(f"{student['name']}       {student['average']:.1f}           {student['grade']}")
        total_average += student['average']
    print("\n")

    # Display and Calculation of the Class average
    class_average = total_average / len(students)
    print(f"Class average: {class_average:.1f}")

    print("=" * 50)


main()
