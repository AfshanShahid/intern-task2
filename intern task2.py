# Task:2
# Part:1
books = {}

books["1234"] = (
    "Comupter Science", 
    "Ali Ahmed", 
    150.00, 
    {"computer", "science"}
)

books["12345"] = (
    "Mathematics", 
    "Hassan Ali", 
    200.00, 
    {"mathematics", "science"}
)

print(books)


# Part:2
def search_by_author(author):
    result = []
    for isbn, details in books.items():
        if details[1] == author:
            result.append((isbn, details[0]))
    return result

print(search_by_author("Ali Ahmed"))


# Part:3
def update_price(isbn, new_price):
    if isbn in books:
        title, author, _, tags = books[isbn]
        books[isbn] = (title, author, new_price, tags)
        return True
    return False

print(update_price("1234", 175.00))
print(books)


# Part:4
def standardize_genres():
    for isbn, details in books.items():
        title, author, price, genres = details
        cleaned_genres = {genre.strip().lower() for genre in genres}
        books[isbn] = (title, author, price, cleaned_genres)

standardize_genres()
print(books)


# Part:5
def display_inventory():
    print(f"{'ISBN':<10} {'Title':<20} {'Author':<20} {'Price':<10} {'Genres'}")
    print("-" * 70)
    for isbn, details in books.items():
        title, author, price, genres = details
        genres_str = ", ".join(genres)
        print(f"{isbn:<10} {title:<20} {author:<20} {price:<10} {genres_str}")

display_inventory()


# Part:6
def list_all_books():
    titles = [details[0] for details in books.values()]
    return sorted(titles)

print(list_all_books())