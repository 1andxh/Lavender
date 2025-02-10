books = []

print("Welcome to the Book Title Library!")


while True:
    print("Choose an option: \n1. Add a Book \n2. Remove a Book \n3. View All Books \n4. Exit \n")
    try:
        user_input = int(input("Enter your choice: "))

        if user_input == 1:
            add_book = input("Enter the book title: ")
            books.append(add_book)
            print(f'"{add_book}" has been added to the library\n')
        
        elif user_input == 2:
            remove_book = input("Enter book title to remove: ")
            if remove_book in books:
                books.remove(remove_book)
                print(f'"{remove_book}" has been removed from the library.\n')
            else:
                print(f"{remove_book} not found in library")

        elif user_input == 3:
            if books:
                print("Books in library: ")
                # for book in books:
                    # print(book)
                print(f"- {books[0]}\n")
            else:
                print("No books in Library\n")

        elif user_input == 4:
            print("Goodbye!")
            break
        else:
            print("Enter a valid option (1-4)")

    except ValueError:
        print("Invalid input! Enter a number!")
        continue
        



    

    

    