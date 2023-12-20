class Publication:
    def __init__(self, title, authors, year, status="available"):
        self.title = title
        self.authors = authors
        self.year = year
        self.status = status
  

class Book(Publication):
    def __init__(self, title, authors, year, ISBN, num_pages):
        super().__init__(title, authors, year)
        self.ISBN = ISBN
        self.num_pages = num_pages
        if len(ISBN) != 13:
            raise ValueError("ISBN must have 13 digits.")
    

class Journal(Publication):
    def __init__(self, title, authors, year, edition, periodicity):
        super().__init__(title, authors, year)
        self.edition = edition
        self.periodicity = periodicity

class User:
    def __init__(self, name, userID, max_pubs):
        self.name = name
        self.userID = userID
        self.max_pubs = max_pubs
        self.pubs = []
    
    #def __str__(self):
        #for pub in self.pubs:
            #return f"{self.title} - {self.authors} ({self.year})"
    
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
        self.catalogue = []
        self.users = []

    def show_catalog(self):
        print(f"Catalogue of the library: {self.name}")
        print("-" * 50)
        for pub in self.catalogue:
            print(f"{pub.title} - {pub.authors} ({pub.year})")
        print("-" * 50)

    def add_publication(self, publication):
        self.catalogue.append(publication)

    def register_user(self, user):
        self.users.append(user)

    def lend_pub(self, user, publication):
        if user in self.users and publication in self.catalogue and publication.status == "available":
            user.lend_pub(publication)
            publication.status = "borrowed"
        elif publication.status == "borrowed":
            print(f"The Book '{publication.title}' is not available.")
        else:
            print("The user or publication is not registered.")
    
    def return_pub(self, user, publication):
        if user in self.users and publication in self.catalogue and publication.status == "borrowed":
            user.return_pub(publication)
            publication.status = "available"
        else:
            print("The user or publication is not registered or not borrowed.")
            

# Test code
if __name__ == "__main__":
    library = Library("Loyola Andalucía Library")
    book1 = Book("Learning Python II", ["Javier Perez", "Daniel Muñoz"], 2023, "1234567890123", 300)
    journal1 = Journal("Technology Journal", ["Stephen Curry", "LeBron James"], 2022, 7, "Annual")
    journal2 = Journal("Medical Journal", ["Michael Jordan", "Larry Bird"], 2023, 5, "Monthly")
    professor1 = Professor("Professor Tija", "123456789", "Philosophy", "123456")
    student1 = Student("Ashkabos Teberio", "987654321", "DAN", "654321")
    student2 = Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")

    library.add_publication(book1)
    library.add_publication(journal1)
    library.add_publication(journal2)
    library.register_user(professor1)
    library.register_user(student1)

    

library.show_catalog()
library.lend_pub(professor1, book1)
library.lend_pub(student1, book1) # the book should be borrowed
print(student1.pubs) # empty list
library.return_pub(professor1, book1)
library.lend_pub(student1, book1)   # the book should be available now
library.lend_pub(student1, journal2)
print(student1.pubs)
#print([f"{pub.title} - {pub.authors} ({pub.year})" for pub in student1.pubs])
library.lend_pub(student2, journal1) # User not registred
