books = []

def add_new_book():
    print("\nLet's add a new book!")
    book_name = input("Book title: ")
    author_name = input("Author: ")
    one_book = {
        "title": book_name,
        "author": author_name,
        "is_issued": False
    }
    books.append(one_book)
    print(f'"{book_name}" by {author_name} added to the library.')

def show_books():
    print("\nAll books in the library:")
    if books:
        for i, b in enumerate(books, 1):
            if b['is_issued']:
                status = 'Issued'
            else:
                status = 'Available'
            print(f"{i}. {b['title']} by {b['author']} [{status}]")
    else:
        print("No books right now!")

def lend_book():
    if not books:
        print("No books available to issue.")
        return
    show_books()
    try:
        n = int(input("Enter number of the book to issue: ")) - 1
        if 0 <= n < len(books):
            if books[n]['is_issued']:
                print("Sorry, already issued.")
            else:
                books[n]['is_issued'] = True
                print(f'You have borrowed "{books[n]["title"]}".')
        else:
            print("Book does not exist.")
    except:
        print("Invalid input.")

def give_back_book():
    if not books:
        print("No books available to return.")
        return
    show_books()
    try:
        n = int(input("Enter number of the book to return: ")) - 1
        if 0 <= n < len(books):
            if books[n]['is_issued']:
                books[n]['is_issued'] = False
                print(f'Thanks for returning "{books[n]["title"]}".')
            else:
                print("This book wasn't issued!")
        else:
            print("Book does not exist.")
    except:
        print("Invalid input.")

def remove_book():
    if not books:
        print("No books can be removed.")
        return
    show_books()
    try:
        n = int(input("Which book number to remove? ")) - 1
        if 0 <= n < len(books):
            removed_book = books.pop(n)
            print(f'Removed "{removed_book["title"]}" from the library.')
        else:
            print("No such book number.")
    except:
        print("Invalid input.")

def main_menu():
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Remove Book")
        print("6. Quit")
        choice = input("What do you want to do? ")
        if choice == "1":
            add_new_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            lend_book()
        elif choice == "4":
            give_back_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            print("Bye! Have a nice day.")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main_menu()
