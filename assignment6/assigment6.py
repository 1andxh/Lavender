students_record = []


print("Welcome to the Student Management System!\n")
while True:
    print("Choose an option: \n1. Add a student\n2. Remove a Student\n3. View all Students\n4. View one student\n5. exit\n")
    user_input = input("Enter your choice: ")

    if user_input == "1":      
        name = input("Enter student name: ").title()
        age = int(input("Enter age: "))
        grade = input("Enter grade: ").upper()
        course = input("Enter course: ").title()

        print(f"{name.capitalize()} has been added to the System: \n")

        student = {'name': name , 'age': age, 'grade' : grade, 'course' : course}
        students_record.append(student)

    elif user_input == '2':
        
        remove_student = input("Enter name of student: ").title()

        for i, student in enumerate(students_record):
            if student['name'] == remove_student:
                # students_record.remove(student[name])
                students_record.pop(i)
                # del students_record[remove_student]
                print(f"{remove_student} has been removed from the system\n")
                break
                
        else:  
            print("No records found\n")


    elif user_input == '3':
        print("Students in the System\n")
        for student in students_record:
            print(f"- {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Course: {student['course']}")

    elif user_input == '4':
        view_one_student = input("Enter name of student: ")
        for student in students_record:
            if student['name'] == view_one_student:
                print(student)
                break
        else:
            print(f"Name '{view_one_student}' not found!\n")

    elif user_input == '5':
        print("Goodbye!")
        break
    else:
        print("Enter a valid option(1-5)!")
