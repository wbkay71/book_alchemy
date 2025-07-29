from flask import Flask, render_template, request, redirect, url_for, flash
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

# Home route with sorting
@app.route('/')
def home():
    # Get sort parameter from URL
    sort_by = request.args.get('sort', 'title')  # Default sort by title

    # Query books with sorting
    if sort_by == 'author':
        # Sort by author name (join with Author table)
        books = Book.query.join(Author).order_by(Author.name).all()
    elif sort_by == 'year':
        # Sort by publication year
        books = Book.query.order_by(Book.publication_year).all()
    else:
        # Default: sort by title
        books = Book.query.order_by(Book.title).all()

    return render_template('home.html', books=books, current_sort=sort_by)

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

if __name__ == '__main__':
    app.run(debug=True, port=5002)