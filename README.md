# Cafe Finder - Django Web Application

A comprehensive web application for discovering and reviewing cafes in Jaipur, Delhi, and Gurgaon. Browse cafes by city, read and submit reviews, and manage your cafe database with an easy-to-use admin panel.

![Homepage Screenshot]()
*Screenshot: Homepage - Add image here*

---

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Admin Panel](#admin-panel)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)

---

## 🎯 About

Cafe Finder helps you discover the best cafes across Jaipur, Delhi, and Gurgaon. View detailed ratings for coffee quality, WiFi strength, and ambiance. Check if a cafe has power sockets, read reviews from other visitors, and share your own experience. The application includes a secret-key protected admin panel for managing the cafe database without needing Django's default admin interface.

---

## ✨ Features

### 🌐 Public Features
- **Browse by City**: Select from Jaipur, Delhi, or Gurgaon to view cafes
- **Search & Sort**: Search cafes by name and sort by rating or alphabetically
- **Detailed Ratings**:
  - ☕ Coffee Quality (1-5 stars)
  - 📶 WiFi Strength (1-5 stars)
  - 🎨 Ambiance (1-5 stars)
  - 🔌 Power Socket Availability (Yes/No)
- **Location Links**: Direct Google Maps integration for each cafe
- **Review System**: 
  - Submit reviews (anonymous or with email)
  - Read reviews from other visitors
  - Vote on reviews with 👍 Agree / 👎 Disagree buttons
  - See vote counts for each review

### 🔐 Admin Features (Secret Key Protected)
- **Add New Cafes**: Complete form with all cafe details
- **Edit Cafes**: Update any cafe information inline
- **Delete Cafes**: Remove cafes from the database
- **Custom Interface**: No Django admin panel needed

---

## 📸 Screenshots

### Homepage - Browse Cafes
![Homepage]()
*Add screenshot showing city dropdown and cafe list with ratings*

### Cafe Details Page
![Cafe Details]()
*Add screenshot showing detailed cafe information and reviews*

### Review System
![Reviews]()
*Add screenshot showing review form and voting system*

### Admin Panel
![Admin Panel]()
*Add screenshot showing the edit interface for managing cafes*

---

## 🚀 Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package installer)

### Step-by-Step Setup

1. **Navigate to Project Directory**
   ```bash
   cd e:\PythonProject\DjangoProject
   ```

2. **Create Virtual Environment** (if not exists)
   ```bash
   python -m venv .venv
   ```

3. **Activate Virtual Environment**
   
   On Windows:
   ```bash
   .venv\Scripts\activate
   ```
   
   On Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. **Install Django**
   ```bash
   pip install django
   ```

5. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Load Sample Data** (Optional - includes 12 cafes and reviews)
   ```bash
   python manage.py seed_data
   ```

7. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Open Your Browser**
   
   Visit: `http://127.0.0.1:8000/`

---

## 💡 Usage Guide

### Browsing Cafes

1. Visit the homepage at `http://127.0.0.1:8000/`
2. Select a city from the dropdown (Jaipur, Delhi, or Gurgaon)
3. Browse the list of cafes with their ratings
4. Use the search bar to find specific cafes
5. Sort by name or rating using the sort dropdown
6. Click on any cafe name to view full details

![Browse Cafes]()
*Add image showing the browsing interface*

### Viewing Cafe Details

1. Click on a cafe name from the homepage
2. View comprehensive information:
   - All ratings (Coffee, WiFi, Ambiance)
   - Power socket availability
   - Location on Google Maps
3. Click "Open in Google Maps" to navigate
4. Scroll down to read reviews from other visitors

![Cafe Details]()
*Add image showing cafe details page*

### Submitting a Review

1. Navigate to any cafe details page
2. Scroll to the "Leave a Review" section
3. Type your review in the text area
4. (Optional) Enter your email address
   - Leave blank to submit anonymously
5. Click "Submit Review" button
6. Your review will appear in the list

![Submit Review]()
*Add image showing review form*

### Voting on Reviews

1. Find reviews on any cafe details page
2. Read through existing reviews
3. Click 👍 **Agree** if you agree with a review
4. Click 👎 **Disagree** if you disagree
5. Vote counts update automatically

![Vote on Reviews]()
*Add image showing review voting*

---

## 🔐 Admin Panel

The admin panel allows you to manage cafes without using Django's default admin interface. It's protected by a secret key.

### Accessing the Admin Panel

**URL**: `http://127.0.0.1:8000/edit/?key=my_secret_admin_key_2024`

**Default Secret Key**: `my_secret_admin_key_2024`

![Admin Login]()
*Add image showing admin panel access*

### Adding a New Cafe

1. Access the admin panel using the secret key
2. Find the "Add New Cafe" form at the top
3. Fill in all fields:
   - **Cafe Name**: Enter the cafe name
   - **City**: Select Jaipur, Delhi, or Gurgaon
   - **Google Maps URL**: Paste the complete Google Maps link
   - **Coffee Rating**: Enter 1-5
   - **WiFi Rating**: Enter 1-5
   - **Ambiance Rating**: Enter 1-5
   - **Has Power Sockets**: Check if available
4. Click "Add Cafe"

![Add Cafe]()
*Add image showing add cafe form*

### Editing a Cafe

1. Access the admin panel
2. Find the cafe you want to edit in the list
3. Click the "Edit" button next to the cafe
4. Modify any fields in the inline form
5. Click "Save Changes" to update

![Edit Cafe]()
*Add image showing edit interface*

### Deleting a Cafe

1. Access the admin panel
2. Find the cafe you want to delete
3. Click the "Delete" button
4. Confirm the deletion when prompted

### Changing the Secret Key

#### Option 1: Environment Variable (Recommended)

**Windows (PowerShell)**:
```powershell
$env:ADMIN_SECRET_KEY="your_new_secret_key"
python manage.py runserver
```

**Windows (Command Prompt)**:
```cmd
set ADMIN_SECRET_KEY=your_new_secret_key
python manage.py runserver
```

**Linux/Mac**:
```bash
export ADMIN_SECRET_KEY="your_new_secret_key"
python manage.py runserver
```

#### Option 2: Edit settings.py

Open `DjangoProject/settings.py` and modify:
```python
ADMIN_SECRET_KEY = os.environ.get('ADMIN_SECRET_KEY', 'your_new_secret_key')
```

---

## 🛠️ Technologies Used

- **Backend Framework**: Django 5.2.8
- **Database**: SQLite3
- **Frontend**: 
  - HTML5
  - CSS3
  - Bootstrap 5.3 (UI Framework)
  - Bootstrap Icons
- **Python Version**: 3.12.6

---

## 📁 Project Structure

```
DjangoProject/
├── cafes/                          # Main application
│   ├── models.py                   # Database models (Cafe, Review)
│   ├── views.py                    # View functions and logic
│   ├── urls.py                     # URL routing for cafe app
│   ├── admin.py                    # Admin configuration
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py       # Sample data generation
│   └── migrations/                 # Database migrations
├── DjangoProject/                  # Project configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Main URL configuration
│   └── wsgi.py                     # WSGI configuration
├── templates/
│   └── cafes/
│       ├── base.html              # Base template with Bootstrap
│       ├── homepage.html          # Homepage with cafe list
│       ├── cafe_detail.html       # Cafe details and reviews
│       └── edit.html              # Admin panel interface
├── static/                         # Static files (CSS, JS, images)
├── db.sqlite3                     # SQLite database file
├── manage.py                      # Django management script
└── README.md                      # This file
```

### Database Models

**Cafe Model**:
- name (CharField)
- city (CharField: Jaipur/Delhi/Gurgaon)
- map_url (URLField)
- coffee_rating (IntegerField: 0-5)
- wifi_rating (IntegerField: 0-5)
- ambiance_rating (IntegerField: 0-5)
- has_sockets (BooleanField)

**Review Model**:
- cafe (ForeignKey to Cafe)
- email (EmailField, nullable)
- review_text (TextField)
- agree_count (IntegerField)
- disagree_count (IntegerField)
- created_at (DateTimeField)

---

## 🚦 Quick Commands

### Development
```bash
# Start server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load sample data
python manage.py seed_data
```

### Access URLs
- Homepage: `http://127.0.0.1:8000/`
- Admin Panel: `http://127.0.0.1:8000/edit/?key=my_secret_admin_key_2024`
- Cafe Details: `http://127.0.0.1:8000/cafe/<id>/`

---

## 📝 License

This project is created for educational purposes and is open source.

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or new features.

---

**Happy Cafe Hunting! ☕**
