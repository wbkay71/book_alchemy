from app import app, db
from data_models import Author, Book
from datetime import datetime

# Sample data for authors
authors_data = [
    {
        "name": "Jane Austen",
        "birth_date": "1775-12-16",
        "date_of_death": "1817-07-18"
    },
    {
        "name": "Charles Dickens",
        "birth_date": "1812-02-07",
        "date_of_death": "1870-06-09"
    },
    {
        "name": "George Orwell",
        "birth_date": "1903-06-25",
        "date_of_death": "1950-01-21"
    },
    {
        "name": "J.K. Rowling",
        "birth_date": "1965-07-31",
        "date_of_death": None
    },
    {
        "name": "Stephen King",
        "birth_date": "1947-09-21",
        "date_of_death": None
    },
    {
        "name": "Haruki Murakami",
        "birth_date": "1949-01-12",
        "date_of_death": None
    },
    {
        "name": "Margaret Atwood",
        "birth_date": "1939-11-18",
        "date_of_death": None
    }
]

# Sample data for books
books_data = [
    {"title": "Pride and Prejudice", "isbn": "9780141439518", "publication_year": 1813, "author": "Jane Austen"},
    {"title": "Emma", "isbn": "9780141439587", "publication_year": 1815, "author": "Jane Austen"},
    {"title": "Oliver Twist", "isbn": "9780141439747", "publication_year": 1838, "author": "Charles Dickens"},
    {"title": "A Christmas Carol", "isbn": "9780141389479", "publication_year": 1843, "author": "Charles Dickens"},
    {"title": "1984", "isbn": "9780452284234", "publication_year": 1949, "author": "George Orwell"},
    {"title": "Animal Farm", "isbn": "9780452284241", "publication_year": 1945, "author": "George Orwell"},
    {"title": "Harry Potter and the Philosopher's Stone", "isbn": "9780747532699", "publication_year": 1997,
     "author": "J.K. Rowling"},
    {"title": "Harry Potter and the Chamber of Secrets", "isbn": "9780747538493", "publication_year": 1998,
     "author": "J.K. Rowling"},
    {"title": "The Shining", "isbn": "9780307743657", "publication_year": 1977, "author": "Stephen King"},
    {"title": "IT", "isbn": "9781501142970", "publication_year": 1986, "author": "Stephen King"},
    {"title": "Norwegian Wood", "isbn": "9780375704024", "publication_year": 1987, "author": "Haruki Murakami"},
    {"title": "The Handmaid's Tale", "isbn": "9780385490818", "publication_year": 1985, "author": "Margaret Atwood"}
]


def seed_database():
    with app.app_context():
        # Check if data already exists
        if Author.query.first() is not None:
            print("Database already contains data. Skipping seed.")
            return

        # Add authors
        print("Adding authors...")
        author_dict = {}  # Store author objects for book assignment

        for author_data in authors_data:
            # Convert string dates to date objects
            birth_date = datetime.strptime(author_data["birth_date"], "%Y-%m-%d").date() if author_data[
                "birth_date"] else None
            date_of_death = datetime.strptime(author_data["date_of_death"], "%Y-%m-%d").date() if author_data[
                "date_of_death"] else None

            author = Author(
                name=author_data["name"],
                birth_date=birth_date,
                date_of_death=date_of_death
            )
            db.session.add(author)
            author_dict[author_data["name"]] = author
            print(f"  Added: {author_data['name']}")

        # Commit authors first
        db.session.commit()
        print("Authors added successfully!")

        # Add books
        print("\nAdding books...")
        for book_data in books_data:
            # Find the author
            author = author_dict.get(book_data["author"])
            if author:
                book = Book(
                    isbn=book_data["isbn"],
                    title=book_data["title"],
                    publication_year=book_data["publication_year"],
                    author_id=author.id
                )
                db.session.add(book)
                print(f"  Added: {book_data['title']} by {book_data['author']}")

        # Commit books
        db.session.commit()
        print("Books added successfully!")
        print("\nDatabase seeded successfully! 🎉")


if __name__ == "__main__":
    seed_database()