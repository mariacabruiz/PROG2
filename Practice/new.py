class Pubication: 
    def __init__(self, title, authors, year, status="available")
        self.title = title 
        self.authors = authors
        self.year = year
        self.status = status

class Book(Publication):
    def __init__(self, title, authors, year, ISBN, num_pages):
        super().__init__(title, authors, year)
        self.ISBN = ISBN
        self.num_pages = num_pages

class Journal(Publication):
    def __init__(self, title, authors, year, edition, periodicity):
        super().__init__(title, authors, year)
        self.edition = edition
        self.periodicity = periodicity

class User:
    def __init__(self, name, userID, max_pubs):
        self.name = name
        self.userID = userID
        self.pubs = []
        self.max_pubs = max_pubs
    
    def __str__(self):
        return f"{self.title} - {self.authors} ({self.year})" 

    def lend_pub(self, publication):
        if len(self.pubs) < self.max_pubs:
            self.pubs.append(publication)
            publication.status = "borrowed"
            print(f"The Book '{publication.title}' has been lent to {self.name}.")
        else:
            print(f"{self.name} has reached the maximum limit of borrowed items.")

    def return_pub(self, publication):
        if publication in self.pubs:
            self.pubs.remove(publication)
            publication.status = "available"
            print(f"The Book '{publication.title}' was returned by {self.name}.")
        else:
            print(f"{self.name} did not borrow this publication.")

class Professor(User):
    def __init__(self, name, userID, department, employeeID, max_pubs=2):
        super().__init__(name, userID, max_pubs)
        self.department = department
        self.employeeID = employeeID

class Student(User):
    def __init__(self, name, userID, grade, studentID, max_pubs=1):
        super().__init__(name, userID, max_pubs)
        self.grade = grade
        self.studentID = studentID

class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.catalog = []
    
    def show_catalog(self):
        print("Catalogue of the library: {self.name}")
        print("-" * 50)
        for pub in self.catalog:
            print(pub)
        print("-" * 50)
    
    def add_publication(self, publication):
        self.catalog.append(publication)
    
    def register_user(self, user):
        self.users.append(user)
    
    def lend_pub(self, user, publication):
        if user in self.users and publication in self.catalog and publication.status == "available":
            if user.lend_pub(publication):
                publication.status = "borrowed"
        elif publication.status == "borrowed":
            print(f"The publication '{publication.title}' is not available.")
        else:
            print("The user or publication is not registered.")

    def return_pub(self, user, publication):
        if user in self.users and publication in self.catalog and publication.status == "borrowed":
            if user.return_pub(publication):
                publication.status = "available"
                print(f"The publication '{publication.title}' was returned by {user.name}.")
        else:
            print("The user or publication is not registered.")

        
