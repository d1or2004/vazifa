from data import Database


class Base:

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}' """
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {data} """
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Country(Base):
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,date) VALUES ('{self.name}','{self.date}')"""
        return Database.connect(query, "insert")


class City(Base):
    def __init__(self, name: str, country_id: int, date: str):
        self.name = name
        self.country_id = country_id
        self.date = date

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,country_id,date) VALUES ('{self.name}',{self.country_id},'{self.date}')"""
        return Database.connect(query, "insert")


class Address(Base):
    def __init__(self, name: str, city_id: int):
        self.name = name
        self.city_id = city_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,city_id) VALUES ('{self.name}',{self.city_id})"""
        return Database.connect(query, "insert")


class Users(Base):
    def __init__(self, first_name: str, last_name: str, password: str, gmail: str, date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.gmail = gmail
        self.date = date

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,password,gmail,date) VALUES 
        ('{self.first_name}','{self.last_name}','{self.password}','{self.gmail}','{self.date}')
        """
        return Database.connect(query, "insert")


class Student(Base):
    def __init__(self, first_name: str, last_name: str, username: str, password, gmail, date, balance, active_courses):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gmail = gmail
        self.date = date
        self.balance = balance
        self.active_courses = active_courses

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,username,password,gmail,date,balance,active_courses) VALUES
        ('{self.first_name}','{self.last_name}','{self.username}',
        '{self.password}','{self.gmail}','{self.date}','{self.balance}','{self.active_courses}')
        """
        return Database.connect(query, "insert")


class Mentor(Base):
    def __init__(self, first_name, last_name, username, password, gmail, status):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gmail = gmail
        self.status = status


    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,username,password,gmail,status) VALUES
        ('{self.first_name}','{self.last_name}','{self.username}','{self.password}','{self.gmail}','{self.status}'
        )
        """
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, title, description, reyting, price, price_status, language):
        self.title = title
        self.description = description
        self.reyting = reyting
        self.price = price
        self.price_status = price_status
        self.language = language

    def insert(self, table):
        query = f"""INSERT INTO {table}(title,description,reyting,price,price_status,language) VALUES 
        ('{self.title}','{self.description}',{self.reyting},{self.price},'{self.price_status}','{self.language}')
        """
        return Database.connect(query, "insert")


class CoursesComents(Base):
    def __init__(self, student_id, course_id, text):
        self.student_id = student_id
        self.course_id = course_id
        self.text = text

    def insert(self, table):
        query = f"""INSERT INTO {table}(student_id,course_id,text) VALUES
        ({self.student_id},{self.course_id},'{self.text}')
        """
        return Database.connect(query, "insert")


class Modul(Base):
    def __init__(self, name, lesson_count, create_date, course_id):
        self.name = name
        self.lesson_count = lesson_count
        self.create_date = create_date
        self.course_id = course_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,lesson_count,create_date,course_id) VALUES
        ('{self.name}',{self.lesson_count},'{self.create_date}',{self.course_id})
        """
        return Database.connect(query, "insert")


class Lesson(Base):
    def __init__(self, name, modul_id):
        self.name = name
        self.modul_id = modul_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,modul_id) VALUES
        ('{self.name}',{self.modul_id})
        """
        return Database.connect(query, "insert")


class PaymentStatus(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES 
        ('{self.name}')
        """
        return Database.connect(query, "insert")


class PaymentTYpe(PaymentStatus):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES 
        ('{self.name}')
        """
        return Database.connect(query, "insert")


class Payment(Base):
    def __init__(self, student_id, course_id, amount, payment_status_id, payment_type_id, create_date):
        self.student_id = student_id
        self.course_id = course_id
        self.amount = amount
        self.payment_status_id = payment_status_id
        self.payment_type_id = payment_type_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(student_id,course_id,amount,payment_status_id,payment_type_id,create_date) VALUES 
        ({self.student_id},{self.course_id},{self.amount},{self.payment_status_id},{self.payment_type_id},'{self.create_date}')
        
        """
        return Database.connect(query, "insert")
