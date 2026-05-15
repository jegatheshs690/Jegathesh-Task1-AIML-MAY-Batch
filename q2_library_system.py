# Function to add a book
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book '{title}' added successfully.")


# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book ID {book_id} borrowed successfully.")
        else:
            print(f"Book ID {book_id} is already borrowed.")
    else:
        print(f"Book ID {book_id} does not exist.")


# Function to return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


# Function to register a member
def register_member(members, member_id):
    members.add(member_id)
    print(f"Member {member_id} registered.")


# Function to show available books
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


# Main function
def main():
    # Data structures
    catalog = {}
    borrowed_books = []
    members = set()

    # Adding books
    add_book(catalog, 1, "Python Basics", "John Smith", 2020)
    add_book(catalog, 2, "Data Structures", "Alice Brown", 2019)
    add_book(catalog, 3, "Machine Learning", "David Lee", 2022)
    add_book(catalog, 4, "AI Fundamentals", "Emma Wilson", 2021)

    print()

    # Registering members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)  # Duplicate member

    print()

    # Borrowing books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    print()

    # Returning one book
    return_book(borrowed_books, 1)

    # Display available books
    show_available(catalog, borrowed_books)


# Calling main function
main()
