
class Book:
    def __init__(self, author="", title=""):
        """Initialize the Book object with an author and title."""
        self.author = author
        self.title = title
    
    def display(self):
        """Prints the book details in the required format."""
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    # Creating book objects
    book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")

    # Display book details
    book1.display()
    book2.display()

    print("This is assignment 1 part 2")
