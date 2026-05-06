# Learning Platform

A modern, full-stack learning platform built with Django and React, inspired by Coursera and Udemy.

## Features

- **User Authentication**: Sign up, login, and profile management
- **Course Management**: Create, edit, and manage courses with categories
- **Video Lessons**: Upload and stream video content with progress tracking
- **IT Blog**: Rich text blog system for IT articles and tutorials
- **Progress Tracking**: Monitor learning progress and completion
- **Responsive Design**: Modern UI that works on all devices
- **Admin Panel**: Comprehensive admin interface for content management

## Tech Stack

### Backend
- **Django 4.2.7**: Python web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Production database (SQLite for development)
- **Celery**: Background task processing
- **Redis**: Caching and message broker

### Frontend
- **React 18**: Modern JavaScript framework
- **Material-UI**: Component library for beautiful UI
- **Axios**: HTTP client for API calls
- **React Router**: Client-side routing

## Project Structure

```
learning-platform/
├── backend/                 # Django backend
│   ├── core/               # Main Django project
│   ├── accounts/           # User authentication
│   ├── courses/            # Course management
│   ├── videos/             # Video handling
│   ├── blog/               # Blog system
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── src/                # Source code
│   ├── public/             # Static files
│   └── package.json        # Node.js dependencies
├── media/                  # User uploaded files
└── README.md               # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Backend Setup (Django)

1. **Create and Activate Virtual Environment**:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install Python Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Environment Configuration**:
   Create a `.env` file in the `backend` directory based on `env.example`:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:3000
   ```

4. **Database Setup**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run Django Server**:
   ```bash
   python manage.py runserver
   ```
   The backend will be available at `http://localhost:8000`.

### Frontend Setup (React)

1. **Install Node.js Dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Environment Configuration**:
   Create a `.env` file in the `frontend` directory:
   ```env
   REACT_APP_API_URL=http://localhost:8000
   ```

3. **Run React Development Server**:
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`.

## API Endpoints Overview

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/me/` - Current user info

### Courses
- `GET /api/courses/` - List all courses
- `GET /api/courses/{slug}/` - Course details
- `POST /api/courses/create/` - Create course (instructors)

### Videos
- `GET /api/videos/` - List videos
- `GET /api/videos/{id}/` - Video details
- `POST /api/videos/create/` - Upload video

### Blog
- `GET /api/blog/` - List blog posts
- `GET /api/blog/{slug}/` - Blog post details
- `POST /api/blog/create/` - Create blog post

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use this project for learning and development!
