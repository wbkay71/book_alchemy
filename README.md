# 📚 Book Alchemy - Digital Library

A modern, dark-themed digital library application built with Flask and SQLAlchemy. Manage your personal book collection with style!

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### Core Functionality
- **Author Management**: Add, view, and manage authors with biographical information
- **Book Collection**: Track your books with title, ISBN, publication year, and cover images
- **Smart Deletion**: Automatic cleanup of authors when their last book is removed
- **Search & Filter**: Find books by title or author name
- **Sorting Options**: Sort your library by title, author, or publication year

### Advanced Features
- **ISBN Lookup**: Automatically fetch book details from Google Books API
- **Auto-Create Authors**: Create authors on-the-fly during ISBN lookup
- **Book Covers**: Display book covers using Google Books API
- **Detail Pages**: Dedicated pages for books and authors with rich information
- **Age Calculations**: See author's age at publication and at death

### Modern UI
- 🌙 Dark mode design with glassmorphism effects
- 🎨 3D hover animations on book covers
- 📱 Fully responsive design
- ⚡ Smooth transitions and animations
- 🎯 Intuitive user experience

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/book_alchemy.git
cd book_alchemy
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5002
```

## 📁 Project Structure

```
book_alchemy/
├── app.py                 # Main Flask application
├── data_models.py         # SQLAlchemy models
├── seed_data.py          # Sample data generator
├── requirements.txt       # Python dependencies
├── static/
│   ├── style.css         # Modern dark theme styles
│   └── no-cover.svg      # Placeholder for missing covers
├── templates/
│   ├── home.html         # Main library view
│   ├── add_author.html   # Author creation form
│   ├── add_book.html     # Book creation with ISBN lookup
│   ├── book_detail.html  # Individual book page
│   └── author_detail.html # Author biography page
└── data/
    └── library.sqlite    # SQLite database (auto-created)
```

## 💻 Usage

### Adding an Author
1. Click "Add Author" on the home page
2. Fill in the author's name and optional dates
3. Submit to add to your library

### Adding a Book
1. Click "Add Book" on the home page
2. Either:
   - Enter ISBN and click "Lookup" for automatic details
   - Manually enter book information
3. Select the author from the dropdown
4. Submit to add to your collection

### ISBN Lookup Feature
- Enter any valid ISBN-13 or ISBN-10
- Click "Lookup ISBN" to fetch book details
- If the author doesn't exist, you'll be prompted to create them automatically

### Searching and Sorting
- Use the search bar to find books by title or author
- Click the sort links to organize by title, author, or year

## 🛠️ Technologies Used

- **Backend**: Flask 3.0.0
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML5, CSS3 with custom animations
- **APIs**: Google Books API for covers and book data
- **Fonts**: Inter from Google Fonts
- **Design**: Modern dark theme with glassmorphism

## 📊 Database Schema

### Authors Table
- `id`: Primary key
- `name`: Author's full name
- `birth_date`: Date of birth (optional)
- `date_of_death`: Date of death (optional)

### Books Table
- `id`: Primary key
- `isbn`: ISBN number (optional)
- `title`: Book title
- `publication_year`: Year published (optional)
- `author_id`: Foreign key to Authors table

## 🎨 UI Features

- **Dark Mode**: Easy on the eyes with muted green accents
- **Glassmorphism**: Semi-transparent cards with backdrop blur
- **3D Effects**: Books transform on hover with depth
- **Responsive**: Works on desktop, tablet, and mobile
- **Animations**: Smooth transitions and loading effects

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Books API for book covers and metadata
- Flask and SQLAlchemy communities
- Inter font by Rasmus Andersson
- Inspiration from modern UI/UX design trends

## 📧 Contact

Your Name - [[@wbkay71]](https://www.linkedin.com/in/wanja-benjamin-kneib-a6345851/)

Project Link: [https://github.com/wbkay71/book_alchemy](https://github.com/yourusername/book_alchemy)

---

Made with ❤️ and ☕ for book lovers everywhere
