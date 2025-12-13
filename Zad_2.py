from ssl import HAS_NEVER_CHECK_COMMON_NAME


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library address: {self.city}, {self.street}, {self.zip_code}, Phone: {self.phone}, Hours: {self.open_hours}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Hired: {self.hire_date}, Birth: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, Phone_number: {self.phone}"

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f"Boook from {self.library}, Published {self.publication_date} by: {self.author_name}, {self.author_surname}, Number of Pages: {self.number_of_pages} "

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f"Employee: {self.employee}, Student: {self.student}, Books: {self.books}, Order Date: {self.order_date}"

Library1 = Library("Kraków", "Starowiślna", "32-612", "8:00-16:00", "600-500-800")
Library2 = Library("Kraków", "Wincentego Witosa", "32-612", "8:00-14:00", "600-300-811")

Employee1 = Employee("Jan", "Kowalski","10-03-2025","16-02-1992", "Kraków", "Zakopiańska", "33-990", "600-300-999")
Employee2 = Employee("Jolanta", "Kropka","10-01-2023","16-02-1988", "Kraków", "Wielicka", "22-990", "600-375-999")
Employee3 = Employee("Janina", "Szczotka","10-01-2018","16-02-1865", "Warszawa", "Długa", "22-888", "600-378-999")

Student1 = Student("Jan", "Brzechwa")
Student2 = Student("Teofil", "Jamróz")
Student3 = Student("Zbigniew", "Nowak")

Book1 = Book(Library1, "10-04-2023", "Wisława", "Szymborska", 250)
Book2 = Book(Library2, "10-12-1999", "Remigiusz", "Mróz", 233)
Book3 = Book(Library2, "08-11-1976", "Remigiusz", "Mróz", 157)
Book4 = Book(Library2, "24-11-1898", "Jan", "Kochanowski", 116)
Book5 = Book(Library1, "02-07-1999", "Wisława", "Szymborska", 199)

Order1 = Order(Employee1,Student1, [Book2,Book3, Book5], "14-02-1195")
Order2 = Order(Employee2,Student3, [Book2, Book4, Book5], "10-03-2001")

print(Order1)
print(Order2)

