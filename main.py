#                                                                                       Students and more...

Students = [""]

subjects = ["Development", "english", "spanish"]

while True:
        print("""
        1. Register student.
        2. View of students list.
        3. View
        4. Get out of here boi.
        """)

        Option = int(input("Enter a option: "))
        
        if Option == "1":
            print("-----------------------------------------")
            quantity = int(input("How many students do you want to register: "))

            for shi in range(quantity):
                subjects_and_grade = []
                Name = input(f"Enter the name of kid #{shi+1}: ")
                lastname = input(f"Enter the last name of the kid #{shi+1}: ")
                age = input(f"Enter the age of the kiddo #{shi+1}: ")
                full_name = Name + " " + lastname
                for idx, subjects in enumerate():
                    grade = float(input(f"Enter your grade {subjects}: "))
                    subjects_and_grade.append({subjects[idx]:grade})
            Students.append({"Full_name" : full_name,
                "age" : age,
                "subjects_and_grade" : subjects_and_grade})

            
            print(f"Successfully added {quantity} students")

        if Option == "2":
        
            print("-------------------------")
        
            for shi,idx in range(10):
                if Students[shi] == "":
                    print(f"The student in {shi+1} is: {Students[shi]}")
                else: 
                    print(f"Students #{shi+1}: ")
    
        if Option == "3":
            print
    
        else: 
            Option == "4"
            print("Ok ma boi")
            break