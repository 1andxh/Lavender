class BookLibrary:
    
    
    def __init__(self):
        
        self.books = []
    
    def display_menu(self):
        print("Welcome to the Book Title Library!")
        print("Choose an option: ")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. View All Books")
        print("4. Exit")
    
    def add_book(self):
        add_book = input("Enter the book title: ")
        self.books.append(add_book)
        print(f'"{add_book}" has been added to the library\n')
    
    def remove_book(self):
        remove_book = input("Enter book title to remove: ")
        if remove_book in self.books:
            self.books.remove(remove_book)
            print(f'"{remove_book}" has been removed from the library.\n')
        else:
            print(f"{remove_book} not found in library")
    
    def view_books(self):
        if self.books:
            print("Books in library: ")
            for book in self.books:
                print(f"- {book}")
            print()  # Extra newline for formatting
        else:
            print("No books in Library\n")
    
    def run(self):
        while True:
            self.display_menu()
            
            try:
                user_input = int(input("Enter your choice: "))
                
                if user_input == 1:
                    self.add_book()
                elif user_input == 2:
                    self.remove_book()
                elif user_input == 3:
                    self.view_books()
                elif user_input == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Enter a valid option (1-4)")
            
            except ValueError:
                print("Invalid input! Enter a number!")
                continue

def main():
    library = BookLibrary()
    library.run()

# Run the program
if __name__ == "__main__":
    main()