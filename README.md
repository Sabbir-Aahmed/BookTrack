# BookTrack API

BookTrack is a RESTful API for managing a library system built with Django REST Framework. It supports book, author, category, and borrow record management with role-based access control for librarians and members.

---

## Features

- **User roles**: Librarians and members with different permissions.
- **Books**: CRUD operations with detailed metadata.
- **Authors**: CRUD operations for library authors.
- **Categories**: Manage book categories.
- **Borrow Records**: Track borrowing and returning of books.
- **Permissions**: Librarians have full access; members have read-only or limited access.
- **API documentation**: Swagger/OpenAPI integrated with `drf-yasg`.
- **Authentication**: Token or session-based (customize as needed).

---

## Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- drf-yasg (Swagger/OpenAPI documentation)
- SQLite (default DB, replaceable)

---

## Installation


Follow these steps to set up and run the BookTrack API locally.

### 1. Prerequisites

- Python 3.8 or higher installed ([Download Python](https://www.python.org/downloads/))
- Git installed ([Download Git](https://git-scm.com/downloads))
- (Optional) Virtual environment tool (comes with Python `venv` module)

---

### 2. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/Sabbir-Aahmed/BookTrack
cd BookTrack
```
---
### 3. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to isolate project dependencies.

```
python -m venv .env
# Windows
.env\Scripts\activate
# Unix/macOS
source .env/bin/activate
```
---
### 4. Install dependencies
Make sure you have pip updated, then install all dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```
---

### 5. Configure Environment Variables
Create a .env file to store environment variables like SECRET_KEY, database settings, etc.
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```
---

### 6. Apply Database Migrations
Prepare the database schema by running:

```
python manage.py migrate
```
---

### 7. Create a Superuser
Create an admin user to access the Django admin and librarian features:

```
python manage.py createsuperuser
```
---

### 8. Run the development server
Start the server locally:

```
python manage.py runserver
```
---

## API Endpoints Overview

| Endpoint                          | HTTP Methods             | Description                                     | Permissions                                  |
|----------------------------------|-------------------------|------------------------------------------------|----------------------------------------------|
| `/api/books/`                    | GET, POST               | List all books or add a new book                | Authenticated; POST requires librarian role |
| `/api/books/{id}/`               | GET, PUT, PATCH, DELETE | Retrieve, update, partially update, or delete a book | Authenticated; unsafe methods require librarian |
| `/api/authors/`                  | GET, POST               | List all authors or add a new author            | Authenticated; POST requires librarian role |
| `/api/authors/{id}/`             | GET, PUT, PATCH, DELETE | Retrieve, update, or delete an author           | Authenticated; unsafe methods require librarian |
| `/api/categories/`               | GET, POST               | List all categories or add a new category       | Authenticated; POST requires librarian role |
| `/api/categories/{id}/`          | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a category          | Authenticated; unsafe methods require librarian |
| `/api/borrowrecords/`            | GET, POST, DELETE       | List borrow records, create new, or delete (librarians only) | Authenticated; DELETE requires librarian role |
| `/api/borrowrecords/{id}/`       | GET, DELETE             | Retrieve or delete a specific borrow record     | Authenticated; DELETE requires librarian role |
| `/api/borrowrecords/{id}/return/`| GET                     | Mark a borrowed book as returned                 | Only borrowing member                         |

---

### Notes:

- **Authenticated** means the user must be logged in.
- **Librarian role** is checked via `user.is_librarian` or staff status.
- Members can only see their own active borrow records.
- Only the borrowing member can mark a book as returned.
- Deletion of borrow records is restricted to librarians only.

---

### Example Request

```http
GET /api//v1/books/
Host: localhost:8000
Authorization: Bearer <your_access_token>
Accept: application/json
```
---

## API Documentation
The interactive Swagger UI is available at:
```
http://localhost:8000/swagger/
```

---

## License
This project is licensed under the MIT License.

## Contact

Created by **Md Sabbir Ahmed**

- Email: [mdsabbir5820@gmail.com](mailto:mdsabbir5820@gmail.com)   
- LinkedIn: [https://www.linkedin.com/in/md-sabbir-ahmed/](https://www.linkedin.com/in/md-sabbir-ahmed/)  

Feel free to reach out for questions, suggestions, or collaboration!
