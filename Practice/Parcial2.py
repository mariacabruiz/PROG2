class Publication:
    def __init__ (self, title:str, authors: list[str], year:int, status:str = "available"):
        self.title = title
        self.authors = authors
        self.year = year
        self.status = status
    def __str__(self):
        return f" {self.title} - {self.authors} - ({self.year})"
    
    
class Book(Publication):
    def __init__ (self, title: str, authors: list[str], year: int, isbn: str, num_pages: int ,status: str = "available"):
        super().__init__(title,authors,year,status)
        self.num_pages = num_pages
        if len(isbn) == 13 and isbn.isdigit:
            self.isbn = isbn
        else:
            print("ISBN must be a string of 13 length.")
    
    def __str__(self):
        return f" {self.title} - {self.authors} - ({self.year})"

    
    
class Journal(Publication):
    def __init__(self, title: str, authors: list[str], year: int, edition_num: int, periodicity: str):
        super().__init__(title, authors, year, "available")
        self.edition_num = edition_num
        self.periodicity = periodicity

class User:
    def __init__(self, name: str, user_id: str, max_pubs: int):
        self.name = name

        if len(user_id)==9 and user_id.isdigit():
            self.user_id = user_id
        else:
            print("User ID must be a string of length 9.")
        
        self.pubs = []
        self.max_pubs = max_pubs

    
   
    

    def lend_pub(self, publication):
        if len(self.pubs) < self.max_pubs and publication.status == "available":
            self.pubs.append(publication)
            publication.status = "borrowed"
            print(f"The Publication '{publication.title}' has been lent to {self.name}.")
        elif len(self.pubs) >= self.max_pubs:
            print(f"{self.name} has reached the maximum limit of borrowed items.")
        else:
            print(f"The Publication '{publication.title}' is already borrowed.")

    def return_pub(self, publication):
        if publication in self.pubs and publication.status == "borrowed":
            self.pubs.remove(publication)
            publication.status = "available"
            print(f"The Publication '{publication.title}' was returned by {self.name}.")
        else:
            print(f"{self.name} did not borrow '{publication.title}' from this library or it's not currently borrowed.")


class Professor(User):
    def __init__(self,name: str, user_id: str, department: str, employee_id: str, max_pubs:int = 2):
        super().__init__(name,user_id,max_pubs)
        self.department = department
        
        if len(employee_id) == 6:
            self.employee_id = employee_id
        else:
            print("Employee ID must be a string of length 6.")

class Student(User):
    def __init__(self, name:str, user_id:str, grade:str, student_id:str ,max_pubs:int = 1):
        super().__init__(name,user_id,max_pubs)
        self.grade = grade

        if len(student_id) == 6:
            self.student_id = student_id
        else:
            print("Employee ID must be a string of length 6.")


class Library:
    def __init__ (self, name: str):
        self.name = name
        self.catalogue = []
        self.users = []

    def show_catalogue(self):
        print(f"Catalogue of the library: {self.name}")
        print("--------------------------------------------------------------")
        for pub in self.catalogue:
            print(pub)
        print("--------------------------------------------------------------")

    def add_publication(self,publication):
        self.catalogue.append(publication)

    def register_user(self,user):
        self.users.append(user)
    
    def lend_pub(self,user,publication):
        if user in self.users and publication in self.catalogue:
            user.lend_pub(publication)
            publication.status = "borrowed"
        elif user not in self.users:
            print(f"The user {user.name} is not registered.")
        else:
            print(f"The book {publication.title} is not in the library catalogue.")

    def return_pub(self,user,publication):
        if user in self.users and publication in self.catalogue:
            user.return_pub(publication)
            publication.status="available"
        elif user not in self.users:
            print(f"The user {user.name} is not registered.")
        else:
            print(f"The book {publication.title} is not in the library catalogue.")



if __name__ == "__main__":
    library = Library("Loyola Andalucía Library")
    book1 = Book("Learning Python II",
                ["Javier Perez", "Daniel Muñoz"],
                2023, "1234567890123", 300)
    journal1 = Journal("Technology Journal",
                    ["Stephen Curry", "LeBron James"],
                    2022, 7, "Annual")
    journal2 = Journal("Medical Journal",
                    ["Michael Jordan", "Larry Bird"],
                    2023, 5, "Monthly")
    professor1 = Professor("Professor Tija", "123456789", "Philosophy", "123456")
    student1 = Student("Ashkabos Teberio", "987654321", "DAN", "654321")
    student2 = Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")

    library.add_publication(book1)
    library.add_publication(journal1)
    library.add_publication(journal2)
    library.register_user(professor1)
    library.register_user(student1)

    
    library.show_catalogue()
    library.lend_pub(professor1, book1)
    library.lend_pub(student1, book1) # the book should be borrowed
    print(student1.pubs) # empty list
    library.return_pub(professor1, book1)
    library.lend_pub(student1, book1)   # the book should be available now
    library.lend_pub(student1, journal2)
    print(student1.pubs)
    library.lend_pub(student2, journal1) # User not registred


    
    
    



    