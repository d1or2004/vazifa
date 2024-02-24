from data import Database


def create_tables():
    country = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now(),
            date DATE);"""

    city = f"""
            CREATE TABLE city(
                city_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                country_id INT REFERENCES country(country_id),
                last_update TIMESTAMP DEFAULT now(),
                date DATE);"""

    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            city_id INT REFERENCES city(city_id));
    """
    users = f"""
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            password VARCHAR(20),
            gmail VARCHAR(20),
            last_update TIMESTAMP DEFAULT now(),
            date DATE);"""

    student = f"""
    CREATE TABLE student(
        student_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        username VARCHAR(20),
        password VARCHAR(20),
        gmail VARCHAR(20),
        last_update TIMESTAMP DEFAULT now(),
        date DATE,
        balance VARCHAR(30),
        active_courses VARCHAR(20));
    """

    mentor = f"""
        CREATE TABLE mentor(
        mentor_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        username VARCHAR(20),
        password VARCHAR(20),
        gmail VARCHAR(20),
        status VARCHAR(20),
        last_update TIMESTAMP DEFAULT now(),
        address_id INT REFERENCES address(address_id));"""

    course = f"""
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            title VARCHAR(20),
            description VARCHAR(20),
            reyting FLOAT,
            price SMALLINT,
            price_status VARCHAR(20),
            language VARCHAR(20));
    """

    course_coments = f"""
        CREATE TABLE course_comments(
        course_comments_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES student(student_id),
        course_id INT REFERENCES course(course_id),
        text VARCHAR(200),
        create_time TIMESTAMP DEFAULT now()
        );
    """

    modul = f"""
    CREATE TABLE modul(
        modul_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        lesson_count SMALLINT,
        last_update TIMESTAMP DEFAULT now(),
        create_date DATE,
        course_id INT REFERENCES course(course_id));
    """

    lesson = f"""
    CREATE TABLE lesson(
        lesson_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        modul_id INT REFERENCES modul(modul_id),
        last_update TIMESTAMP DEFAULT now());
    """

    payment_status = f"""
        CREATE TABLE payment_status(
            payment_status_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now());
    """

    payment_type = f"""
        CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now());
    """
    payment = f"""
    CREATE TABLE payment(
    payment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id),
    course_id INT REFERENCES course(course_id),
    amount SMALLINT,
    payment_status_id INT REFERENCES payment_status(payment_status_id),
    payment_type_id INT REFERENCES payment_type(payment_type_id),
    last_update TIMESTAMP DEFAULT now(),
    create_date DATE);
    """

    data_table = {
        "country": country,
        "city": city,
        "address": address,
        "users": users,
        "student": student,
        "mentor": mentor,
        "course": course,
        "course_coments": course_coments,
        "modul": modul,
        "lesson": lesson,
        "payment_status": payment_status,
        "payment_type": payment_type,
        "payment": payment
    }

    for i in data_table:
        print(f"{i} {Database.connect(data_table[i], "create")}")


# if __name__ == "__main__":
#     create_tables()
