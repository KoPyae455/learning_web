# Learning Platform Setup Guide

This guide will help you set up and run the Learning Platform project on your local machine.

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

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
├── static/                 # Static files
└── README.md               # Project documentation
```

## Backend Setup (Django)

### 1. Create Virtual Environment

```bash
# Navigate to project directory
cd learning-web

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Python Dependencies

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy environment example file
cp env.example .env

# Edit .env file with your configuration
# SECRET_KEY=your-secret-key-here
# DEBUG=True
# ALLOWED_HOSTS=localhost,127.0.0.1
# CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 4. Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 5. Run Django Server

```bash
# Start development server
python manage.py runserver

# Server will run on http://localhost:8000
# Admin panel: http://localhost:8000/admin/
```

## Frontend Setup (React)

### 1. Install Node.js Dependencies

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### 2. Environment Configuration

```bash
# Create .env file in frontend directory
echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

### 3. Run React Development Server

```bash
# Start development server
npm start

# App will open in browser at http://localhost:3000
```

## Database Models

### User Management
- **User**: Custom user model with extended fields
- **UserProfile**: Extended user profile information
- **UserActivity**: Track user learning activities

### Course Management
- **Category**: Course categories
- **Course**: Main course information
- **Lesson**: Individual lessons within courses
- **CourseEnrollment**: Student enrollment tracking
- **CourseRating**: Course ratings and reviews
- **LessonProgress**: Individual lesson progress
- **CourseCertificate**: Completion certificates

### Video Management
- **Video**: Video file information and metadata
- **VideoStream**: Track streaming sessions
- **VideoAnalytics**: Video performance metrics
- **VideoComment**: User comments on videos
- **VideoBookmark**: User bookmarks

### Blog System
- **BlogCategory**: Blog post categories
- **BlogTag**: Blog post tags
- **BlogPost**: Blog post content
- **BlogComment**: User comments
- **BlogLike**: User likes
- **BlogBookmark**: User bookmarks
- **BlogView**: View tracking
- **BlogNewsletter**: Newsletter subscriptions

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/me/` - Current user info
- `PUT /api/auth/profile/update/` - Update profile

### Courses
- `GET /api/courses/` - List all courses
- `GET /api/courses/{slug}/` - Course details
- `POST /api/courses/create/` - Create course (instructors)
- `PUT /api/courses/{slug}/edit/` - Update course
- `POST /api/courses/{slug}/enroll/` - Enroll in course

### Videos
- `GET /api/videos/` - List videos
- `GET /api/videos/{id}/` - Video details
- `POST /api/videos/create/` - Upload video
- `GET /api/videos/{id}/stream/` - Stream video

### Blog
- `GET /api/blog/` - List blog posts
- `GET /api/blog/{slug}/` - Blog post details
- `POST /api/blog/create/` - Create blog post
- `GET /api/blog/categories/` - List categories

## Features

### For Students
- Browse and enroll in courses
- Watch video lessons
- Track learning progress
- Earn certificates
- Read IT blog posts
- Rate and review courses

### For Instructors
- Create and manage courses
- Upload video content
- Monitor student progress
- Manage course content
- View analytics

### For Administrators
- User management
- Course moderation
- Content management
- Analytics dashboard
- System configuration

## Development Workflow

### Backend Development
1. Make changes to models in `backend/apps/`
2. Create and apply migrations
3. Update serializers and views
4. Test API endpoints
5. Update admin interface if needed

### Frontend Development
1. Make changes to React components
2. Update routing if needed
3. Test UI components
4. Ensure responsive design
5. Test API integration

## Testing

### Backend Testing
```bash
# Run Django tests
python manage.py test

# Run specific app tests
python manage.py test accounts
python manage.py test courses
python manage.py test videos
python manage.py test blog
```

### Frontend Testing
```bash
# Run React tests
npm test

# Run tests with coverage
npm test -- --coverage
```

## Deployment

### Backend Deployment
1. Set `DEBUG=False` in production
2. Configure production database (PostgreSQL)
3. Set up static file serving
4. Configure media file storage
5. Set up SSL certificates
6. Configure production server (Gunicorn)

### Frontend Deployment
1. Build production version: `npm run build`
2. Serve static files from web server
3. Configure API URL for production
4. Set up CDN for static assets

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check database configuration
   - Ensure database is running
   - Verify connection credentials

2. **Migration Errors**
   - Delete migration files and recreate
   - Check model dependencies
   - Verify database schema

3. **CORS Issues**
   - Check CORS configuration in Django
   - Verify frontend API URL
   - Check browser console for errors

4. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check static file configuration
   - Verify file permissions

5. **Video Upload Issues**
   - Check file size limits
   - Verify supported formats
   - Check storage configuration

### Getting Help

- Check Django and React documentation
- Review error logs in console
- Verify environment configuration
- Check API endpoint responses
- Test with different browsers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
