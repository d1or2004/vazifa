from classes import *


def servise_countri():
    services = input("""
        ------------------------------------------------
        👉 Country Table 
            1. Select
            2. Insert
            3. Delete
            4. Update
            5. Back
        ------------------------------------------------
        Enter : """)

    if services == "1":
        for i in Country.select("country"):
            print(i)
        return servise_countri()
    elif services == "2":
        name = input("Name : ")
        data = input("Data : ")
        country = Country(name, data)
        print(country.insert("country"))
        return servise_countri()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "country_id":
            print(Country.delete(column, data, "country"))
        else:
            print(Country.delete_id(column, data, "country"))
        return servise_countri()

    elif services == "4":
        column = input("Column : ")
        data = input("counter_id: ")
        query = f"""
                   UPDATE country SET name = '{column}' WHERE country_id = {data}
                                               """
        print(Country.update(query))
        return servise_countri()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_countri()


def servise_city():
    services = input("""
        ------------------------------------------------
        👉 City Table 
            1. Select
            2. Insert
            3. Delete
            4. Update
            5. Back
        ------------------------------------------------
        Enter : """)

    if services == "1":
        for i in City.select("city"):
            print(i)
        return servise_city()
    elif services == "2":
        name = input("Name : ")
        country = int(input("Country Id : "))
        data = input("Data : ")
        country = City(name, country, data)
        print(country.insert("city"))
        return servise_city()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "city_id":
            print(City.delete(column, data, "city"))
        else:
            print(City.delete_id(column, data, "city"))
        return servise_city()

    elif services == "4":
        column = input("New Name : ")
        data = input("city id: ")
        query = f"""
                   UPDATE city SET name = '{column}' WHERE city_id = {data}
                                               """
        print(City.update(query))
        return servise_city()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_city()


def servise_address():
    services = input("""
           ------------------------------------------------
           👉 Address Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)

    if services == "1":
        for i in Address.select("address"):
            print(i)
        return servise_address()
    elif services == "2":
        name = input("Name : ")
        country = int(input("City Id : "))
        country = Address(name, country)
        print(country.insert("address"))
        return servise_address()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "address_id":
            print(Address.delete(column, data, "address"))
        else:
            print(Address.delete_id(column, data, "address"))
        return servise_city()

    elif services == "4":
        column = input("New Name : ")
        data = input("address id: ")
        query = f"""
                      UPDATE address SET name = '{column}' WHERE address_id = {data}
                                                  """
        print(Address.update(query))
        return servise_address()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_address()


def servise_users():
    services = input("""
           ------------------------------------------------
           👉 Users Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)

    if services == "1":
        for i in Users.select("users"):
            print(i)
        return servise_users()
    elif services == "2":
        firs_name = input("First Name : ")
        last_name = input("Last Name")
        password = input("Password: ")
        gmail = input("Gmail : ")
        date = input("Date : ")
        country = Users(firs_name, last_name, password, gmail, date)
        print(country.insert("users"))
        return servise_users()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "users_id":
            print(Users.delete(column, data, "users"))
        else:
            print(Users.delete_id(column, data, "users"))
        return servise_users()

    elif services == "4":
        column = input("New Name : ")
        data = input("users id: ")
        query = f"""
                      UPDATE users SET first_name = '{column}' WHERE user_id = {data}
                                                  """
        print(Users.update(query))
        return servise_users()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_users()


def servise_student():
    services = input("""
           ------------------------------------------------
           👉 Student Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)

    if services == "1":
        for i in Student.select("student"):
            print(i)
        return servise_student()
    elif services == "2":
        first_name = input("First Name : ")
        last_name = input("Last Name")
        username = input("Username : ")
        password = input("Password: ")
        gmail = input("Gmail : ")
        date = input("Date : ")
        balance = input("Balance : ")
        active_courses = input("Active Courses : ")
        country = Student(first_name, last_name, username, password, gmail, date, balance, active_courses)
        print(country.insert("student"))
        return servise_student()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "student_id":
            print(Student.delete(column, data, "student"))
        else:
            print(Student.delete_id(column, data, "student"))
        return servise_student()

    elif services == "4":
        column = input("New Name : ")
        data = input("student id: ")
        query = f"""
                      UPDATE student SET first_name = '{column}' WHERE student_id = {data}
                                                  """
        print(Student.update(query))
        return servise_student()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_student()


def servise_mentor():
    services = input("""
           ------------------------------------------------
           👉 Mentor Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)

    if services == "1":
        for i in Mentor.select("mentor"):
            print(i)
        return servise_mentor()
    elif services == "2":
        first_name = input("First Name : ")
        last_name = input("Last Name")
        username = input("Username : ")
        password = input("Password: ")
        gmail = input("Gmail : ")
        status = input("Status : ")
        country = Mentor(first_name, last_name, username, password, gmail, status)
        print(country.insert("mentor"))
        return servise_mentor()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "mentor_id":
            print(Mentor.delete(column, data, "mentor"))
        else:
            print(Mentor.delete_id(column, data, "mentor"))
        return servise_mentor()

    elif services == "4":
        column = input("New Name : ")
        data = input("student id: ")
        query = f"""
                      UPDATE mentor SET first_name = '{column}' WHERE mentor_id = {data}
                                                  """
        print(Mentor.update(query))
        return servise_mentor()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_mentor()


def servise_course():
    services = input("""
           ------------------------------------------------
           👉 Course Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)

    if services == "1":
        for i in Course.select("course"):
            print(i)
        return servise_course()
    elif services == "2":
        title = input("Title : ")
        description = input("Description : ")
        reyting = int(input("Reyting : "))
        price = int(input("Price : "))
        price_status = input("Price Status : ")
        language = input("Language : ")
        country = Course(title, description, reyting, price, price_status, language)
        print(country.insert("course"))
        return servise_course()
    elif services == "3":
        column = input("Column : ")
        data = input("Row : ")
        if column != "course_id":
            print(Course.delete(column, data, "course"))
        else:
            print(Course.delete_id(column, data, "course"))
        return servise_course()

    elif services == "4":
        column = input("New Name : ")
        data = input("Course Id id: ")
        query = f"""
                      UPDATE course SET title = '{column}' WHERE course_id = {data}
                                                  """
        print(Course.update(query))
        return servise_course()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday servise mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_course()


def servise_course_coments():
    services = input("""
    ------------------------------------------------
    👉 Course Coments Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in CoursesComents.select("course_comments"):
            print(i)
        return servise_course_coments()
    elif services == '2':
        student_id = int(input("Enter student id "))
        course_id = int(input("Enter course id "))
        text = input("Enter text ")
        country = CoursesComents(student_id, course_id, text)
        print(country.insert("course_comments"))
        return servise_course_coments()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "course_coments_id":
            print(CoursesComents.delete(column, date, "course_comments"))

        else:
            print(CoursesComents.delete_id(column, date, "course_comments"))
        return servise_course_coments()
    elif services == "4":
        country = input("New Text : ")
        id = int(input("Course coments ID : "))
        query = f"""
            UPDATE course_comments SET text = '{country}' WHERE course_comments_id = {id}
                                        """
        print(CoursesComents.update(query))
        return servise_course_coments()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_course_coments()


def servise_modul():
    services = input("""
    ------------------------------------------------
    👉 Modul  Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Modul.select("modul"):
            print(i)
        return servise_modul()
    elif services == '2':
        name = input("Name : ")
        lesson = int(input("Lesson Count : "))
        create_date = input("Create date : ")
        course = int(input("Course id"))
        country = Modul(name, lesson, create_date, course)
        print(country.insert("modul"))
        return servise_modul()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "modul_id":
            print(Modul.delete(column, date, "modul"))

        else:
            print(Modul.delete_id(column, date, "modul"))
        return servise_modul()
    elif services == "4":
        country = input("New Name : ")
        id = int(input("Modul ID : "))
        query = f"""
            UPDATE modul SET name = '{country}' WHERE modul_id = {id}
                                        """
        print(Modul.update(query))
        return servise_modul()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_modul()


def servise_lesson():
    services = input("""
           ------------------------------------------------
           👉 Lesson Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------
           Enter : """)
    if services == '1':
        for i in Lesson.select("lesson"):
            print(i)
        return servise_lesson()
    elif services == '2':
        name = input("Name : ")
        modul_id = int(input("Modul Id "))
        country = Lesson(name, modul_id)
        print(country.insert("lesson"))
        return servise_lesson()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "lesson_id":
            print(Lesson.delete(column, date, "lesson"))

        else:
            print(Lesson.delete_id(column, date, "lesson"))
        return servise_lesson()
    elif services == "4":
        country = input("New Name : ")
        id = int(input("Lesson ID : "))
        query = f"""
                   UPDATE lesson SET name = '{country}' WHERE lesson_id = {id}
                                               """
        print(Lesson.update(query))
        return servise_lesson()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_lesson()


def servise_payment_status():
    services = input("""
               ------------------------------------------------
               👉 Payment Status Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------
               Enter : """)
    if services == '1':
        for i in PaymentStatus.select("payment_status"):
            print(i)
        return servise_payment_status()
    elif services == '2':
        name = input("Name : ")
        country = PaymentStatus(name)
        print(country.insert("payment_status"))
        return servise_payment_status()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "payment_status_id":
            print(PaymentStatus.delete(column, date, "payment_status"))

        else:
            print(PaymentStatus.delete_id(column, date, "payment_status"))
        return servise_payment_status()
    elif services == "4":
        country = input("Name : ")
        id = int(input("Payment Status ID : "))
        query = f"""
                       UPDATE payment_status SET name = '{country}' WHERE payment_status_id= {id}
                                                   """
        print(PaymentStatus.update(query))
        return servise_payment_status()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_payment_status()


def servise_payment_type():
    services = input("""
               ------------------------------------------------
               👉 Payment Type Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------
               Enter : """)
    if services == '1':
        for i in PaymentTYpe.select("payment_type"):
            print(i)
        return servise_payment_type()
    elif services == '2':
        name = input("Name : ")
        country = PaymentTYpe(name)
        print(country.insert("payment_type"))
        return servise_payment_type()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "payment_status_id":
            print(PaymentTYpe.delete(column, date, "payment_type"))

        else:
            print(PaymentTYpe.delete_id(column, date, "payment_type"))
        return servise_payment_type()
    elif services == "4":
        country = input("Name : ")
        id = int(input("Payment Status ID : "))
        query = f"""
                       UPDATE payment_type SET name = '{country}' WHERE payment_type_id= {id}
                                                   """
        print(PaymentTYpe.update(query))
        return servise_payment_type()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_payment_type()


def servise_payment():
    services = input("""
               ------------------------------------------------
               👉 Payment  Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------
               Enter : """)
    if services == '1':
        for i in Payment.select("payment"):
            print(i)
        return servise_payment()
    elif services == '2':
        student_id = int(input("Student ID : "))
        course_id = int(input("Course ID : "))
        amount = int(input("Amount : "))
        payment_status_id = int(input("Payment Status ID : "))
        payment_type_id = int(input("Payment Type ID : "))
        create_date = input("Create date ")
        country = Payment(student_id, course_id, amount, payment_status_id, payment_type_id, create_date)
        print(country.insert("payment"))
        return servise_payment()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "payment_id":
            print(Payment.delete(column, date, "payment"))

        else:
            print(Payment.delete_id(column, date, "payment"))
        return servise_payment()
    elif services == "4":
        country = int(input("Amount  : "))
        id = int(input("Payment ID : "))
        query = f"""
                       UPDATE payment SET amount = '{country}' WHERE payment_id= {id}
                                                   """
        print(Payment.update(query))
        return servise_payment()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_payment()


def main():
    tabl = input("""
    1. Country
    2. City
    3. Address
    4. User
    5. Student
    6. Mentor
    7. Course
    8. Course Coments
    9. Modul 
    10. Lesson
    11. Payment Status
    12. Payment Type
    13. Payment
  >>>>  """)

    if tabl == "1":
        return servise_countri()
    elif tabl == "2":
        return servise_city()
    elif tabl == "3":
        return servise_address()
    elif tabl == "4":
        return servise_users()
    elif tabl == "5":
        return servise_student()
    elif tabl == "6":
        return servise_mentor()
    elif tabl == "7":
        return servise_course()
    elif tabl == "8":
        return servise_course_coments()
    elif tabl == "9":
        return servise_modul()
    elif tabl == "10":
        return servise_lesson()
    elif tabl == "11":
        servise_payment_status()
    elif tabl == "12":
        return servise_payment_type()
    elif tabl == "13":
        return servise_payment()


    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday Table mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return main()


if __name__ == '__main__':
    main()
