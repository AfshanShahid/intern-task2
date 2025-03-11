# Task:2
# Part:1
# 1. Create an empty Dictionary
# 2. Each key should be a book's ISBN (a string).
# 3. Each value should be a tuple containing the following details in
# order:
# • Title (String)
# • Author (String)
# • Price (number)
# 4. Genres (a set of stings, e.g ({‘function’,’adventure’})

books = {}

books["125-4-65-35564-2"] = (
    "Comupter Science", 
    "Ali Ahmed", 
    150.00, 
    {"computer", "science"}
)

books["456-5-87-43256-9"] = (
    "Mathematics", 
    "Hassan Ali", 
    200.00, 
    {"mathematics", "science"}
)

print(books)


# Part:2
#1. Write function called search_by_author(author) that
# • Loops through the inventory dictionary
# • Find all book written by author name
# • Returns a list of pairs (or tuples) containing
# the ISBN and title of each matching book.

def search_by_author(author):
    result = []
    for isbn, details in books.items():
        if details[1] == author:
            result.append((isbn, details[0]))
    return result

print(search_by_author("Ali Ahmed"))


# Part:3
#1. Write a function name update_pric(isbn,new_price) that
# • Check If the isbn exist in the inventory
# • If Exist update the price book

def update_price(isbn, new_price):
    if isbn in books:
        title, author, _, tags = books[isbn]
        books[isbn] = (title, author, new_price, tags)
        return True
    return False

print(update_price("125-4-65-35564-2", 175.00))
print(books)


# Part:4
#Write a function called standardize_genres() that:
# • Iterates over every book in the inventory
# • For each book, converts all genre string to lowercase
# and trim any extra spaces
# • Update the genres set in the book’s tuple with the
# cleaned-up values

def standardize_genres():
    for isbn, details in books.items():
        title, author, price, genres = details
        cleaned_genres = {genre.strip().lower() for genre in genres}
        books[isbn] = (title, author, price, cleaned_genres)

standardize_genres()
print(books)


# Part:5
#Write function name display_inventory() that:
# • Loops through the inventory dictionary
# • Prints out the details of each book (ISBN, title, author,
# price, and genres) in a clean and readable format (such
# as a table).

def display_inventory():
    print(f"{'ISBN':<10} {'Title':<20} {'Author':<20} {'Price':<10} {'Genres'}")
    print("-" * 70)
    for isbn, details in books.items():
        title, author, price, genres = details
        genres_str = ", ".join(genres)
        print(f"{isbn:<10} {title:<20} {author:<20} {price:<10} {genres_str}")

display_inventory()


# Part:6
#Write a function called list_all_books() that:
# • Compiles a list of all book titles present in the
# inventory.
# • Sorts the list alphabetically.
# • Returns the sorted list.

def list_all_books():
    titles = [details[0] for details in books.values()]
    return sorted(titles)

print(list_all_books())