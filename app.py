from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import or_ as db_or
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

# Create Flask application instance
app = Flask(__name__)

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the SQLite database with absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Import data models
from data_models import db, Author, Book

# Initialize the database with the Flask app
db.init_app(app)

# Create data directory if it doesn't exist
data_dir = os.path.join(basedir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Created data directory at: {data_dir}")

# Create all tables (run once, then comment out)
# with app.app_context():
#   db.create_all()
#   print("Database tables created successfully!")

# Home route with sorting and search
@app.route('/')
def home():
    # Get sort parameter from URL
    sort_by = request.args.get('sort', 'title')  # Default sort by title
    search_query = request.args.get('search', '')  # Get search query

    # Start with base query
    query = Book.query

    # Apply search filter if search query exists
    if search_query:
        # Search in book title OR author name
        query = query.join(Author).filter(
            db.or_(
                Book.title.like(f'%{search_query}%'),
                Author.name.like(f'%{search_query}%')
            )
        )

    # Apply sorting
    if sort_by == 'author':
        books = query.join(Author).order_by(Author.name).all()
    elif sort_by == 'year':
        books = query.order_by(Book.publication_year).all()
    else:
        books = query.order_by(Book.title).all()

    return render_template('home.html',
                           books=books,
                           current_sort=sort_by,
                           search_query=search_query)

# Route to add authors
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')

        # Check if author already exists
        existing_author = Author.query.filter_by(name=name).first()
        if existing_author:
            flash('This author already exists!', 'error')
            return redirect(url_for('add_author'))

        birthdate_str = request.form.get('birthdate')
        date_of_death_str = request.form.get('date_of_death')

        # Convert string dates to Python date objects
        birth_date = None
        if birthdate_str:
            try:
                birth_date = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid birth date format', 'error')
                return redirect(url_for('add_author'))

        date_of_death = None
        if date_of_death_str:
            try:
                date_of_death = datetime.strptime(date_of_death_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid death date format', 'error')
                return redirect(url_for('add_author'))

        # Create new author
        new_author = Author(
            name=name,
            birth_date=birth_date,
            date_of_death=date_of_death
        )

        # Add to database
        db.session.add(new_author)
        db.session.commit()

        flash('Author added successfully!', 'success')
        return redirect(url_for('add_author'))

    return render_template('add_author.html')


# Route to add books
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get form data
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')

        # Create new book
        new_book = Book(
            isbn=isbn if isbn else None,  # ISBN is optional
            title=title,
            publication_year=int(publication_year) if publication_year else None,
            author_id=int(author_id)
        )

        # Add to database
        db.session.add(new_book)
        db.session.commit()

        flash('Book added successfully!', 'success')
        return redirect(url_for('add_book'))

    # GET request - show form with authors
    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)

# Route to delete a book
@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    # Find the book
    book = Book.query.get_or_404(book_id)
    book_title = book.title
    author_id = book.author_id

    # Delete the book
    db.session.delete(book)
    db.session.commit()

    # Check if author has other books
    other_books = Book.query.filter_by(author_id=author_id).count()
    if other_books == 0:
        # Delete author if no other books exist
        author = Author.query.get(author_id)
        if author:
            author_name = author.name
            db.session.delete(author)
            db.session.commit()
            flash(f'Book "{book_title}" and author "{author_name}" deleted successfully!', 'success')
        else:
            flash(f'Book "{book_title}" deleted successfully!', 'success')
    else:
        flash(f'Book "{book_title}" deleted successfully!', 'success')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)