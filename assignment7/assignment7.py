students = []

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = int(input("Enter student's grade: "))
    students.append({'name': name, 'age': age, 'grade': grade})
    print(f"{name} added successfully!")

def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student['name'] == name:
            print(f"===Current Records===\n- {student['name']} - Age: {student['age']}, Grade: {student['grade']}")
            age = input("Enter new age (or press Enter to keep current): ")
            grade = input("Enter new grade (or press Enter to keep current): ")
            if age:
                student['age'] = int(age)
            if grade:
                student['grade'] = int(grade)
            print(f"{name}'s record updated!")
            return
    print(f"Student {name} not found.")

def average_grade():
    if students:
        avg = sum(s['grade'] for s in students) / len(students)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No students in the record.")

def display_students():
    if students:
        print("\nStudent Records:")
        for s in students:
            print(f"Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
    else:
        print("No students in the record.")

def main():
    print("=== Student Records System ===")
    while True:
        print("\n1. Add Student\n2. Update Student\n3. Average Grade\n4. Display Students\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            average_grade()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
