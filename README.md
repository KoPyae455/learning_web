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
- **PostgreSQL**: Production database
- **SQLite**: Development database
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
│   └── api/                # REST API endpoints
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── utils/          # Utility functions
│   └── public/             # Static files
├── media/                  # User uploaded files
├── static/                 # Static files
└── requirements.txt        # Python dependencies
```

## Setup Instructions

### Backend Setup

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   ```bash
   cd backend
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Install Node.js Dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Run Development Server**:
   ```bash
   npm start
   ```

## Environment Variables

Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## API Endpoints

- **Authentication**: `/api/auth/`
- **Courses**: `/api/courses/`
- **Videos**: `/api/videos/`
- **Blog**: `/api/blog/`
- **Users**: `/api/users/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use this project for learning and development!
