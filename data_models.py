from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()


# Define Author model
class Author(db.Model):
    __tablename__ = 'authors'

    # Primary key - auto-incrementing integer
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Author attributes
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    # Relationship to books (one author can have many books)
    books = db.relationship('Book', backref='author', lazy=True)

    # String representation methods
    def __repr__(self):
        return f'<Author {self.name}>'

    def __str__(self):
        return f'{self.name} ({self.birth_date} - {self.date_of_death or "present"})'


# Define Book model
class Book(db.Model):
    __tablename__ = 'books'

    # Primary key - auto-incrementing integer
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Book attributes
    isbn = db.Column(db.String(13), unique=True)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer)

    # Foreign key to Author table
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    # String representation methods
    def __repr__(self):
        return f'<Book {self.title}>'

    def __str__(self):
        return f'{self.title} by {self.author.name} ({self.publication_year})'