#                                                                  Students and more...

students = [] 
subjects_list = ["Development", "English", "Spanish"]

while True:
    print("""
    1. Register student.
    2. View students list.
    3. View grades
    4. Get out of here boi.
    """)

    option = input("Enter an option: ") 
    
    if option == "1":
        print("-----------------------------------------")
        quantity = int(input("How many students do you want to register: "))

        for i in range(quantity):
            subjects_and_grades = []
            name = input(f"Enter the name of kid #{i+1}: ")
            lastname = input(f"Enter the last name of the kid #{i+1}: ")
            age = input(f"Enter the age of the kiddo #{i+1}: ")
            full_name = f"{name} {lastname}"

            for sub in subjects_list:
                grade = float(input(f"Enter grade for {sub}: "))
                subjects_and_grades.append({sub: grade})

            students.append({
                "Full_name": full_name,
                "age": age,
                "grades": subjects_and_grades
            })
        
        print(f"Successfully added {quantity} students")

    elif option == "2":
        print("--- Student List ---")
        if not students:
            print("The list is empty.")
        for idx, student in enumerate(students):
            print(f"{idx + 1}. {student['Full_name']} (Age: {student['age']})")

    elif option == "3":
        print("--- Detailed Grades ---")
        for student in students:
            print(f"Student: {student['Full_name']}")
            for item in student['grades']:
                for sub, grade in item.items():
                    print(f"  - {sub}: {grade}")
    
    elif option == "4":
        print("Ok ma boi, cya!")
        break
    
    else:
        print("Invalid option, try again.")