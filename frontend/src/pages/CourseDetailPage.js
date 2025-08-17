import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import {
  Box,
  Container,
  Typography,
  Button,
  Grid,
  Card,
  CardContent,
  CardMedia,
  Tabs,
  Tab,
  Divider,
  Chip,
  Stack,
  Avatar,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  IconButton,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import {
  Star as StarIcon,
  People as PeopleIcon,
  Schedule as ScheduleIcon,
  PlayCircle as PlayIcon,
  Article as ArticleIcon,
  Quiz as QuizIcon,
  Assignment as AssignmentIcon,
  Bookmark as BookmarkIcon,
  Share as ShareIcon,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const CourseDetailPage = () => {
  const { id } = useParams();
  // const theme = useTheme();
  // const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const [activeTab, setActiveTab] = useState('overview');
  const [isEnrolled, setIsEnrolled] = useState(false);

  // Mock data - replace with actual data from your backend
  const course = {
    id: id,
    title: 'Complete Python Programming',
    instructor: 'John Doe',
    instructorAvatar: 'https://source.unsplash.com/100x100/?portrait',
    institution: 'Tech University',
    description: 'Master Python from basics to advanced concepts with this comprehensive course. Learn through hands-on projects and real-world examples.',
    longDescription: 'This course will take you from Python basics to advanced concepts. You\'ll learn about data structures, algorithms, object-oriented programming, and how to build real-world applications. By the end of the course, you\'ll be able to write efficient Python code and solve complex problems.',
    image: 'https://source.unsplash.com/800x450/?python,programming',
    rating: 4.8,
    reviews: 1250,
    students: 8500,
    duration: '12 hours',
    lectures: 45,
    projects: 5,
    level: 'Beginner',
    price: '$49.99',
    discountPrice: '$29.99',
    isDiscounted: true,
    whatYouWillLearn: [
      'Python syntax and basic programming concepts',
      'Data structures like lists, dictionaries, and tuples',
      'Object-oriented programming in Python',
      'Working with files and databases',
      'Building real-world applications',
      'Debugging and testing your code',
    ],
    requirements: [
      'No prior programming experience needed',
      'A computer with internet access',
      'Willingness to learn and practice',
    ],
    syllabus: [
      {
        week: 1,
        title: 'Python Basics',
        lectures: 8,
        duration: '2 hours',
        items: [
          { type: 'video', title: 'Introduction to Python', duration: '15 min' },
          { type: 'video', title: 'Variables and Data Types', duration: '20 min' },
          { type: 'article', title: 'Python Syntax Guide' },
          { type: 'quiz', title: 'Basic Concepts Quiz' },
        ],
      },
      {
        week: 2,
        title: 'Control Structures',
        lectures: 7,
        duration: '2.5 hours',
        items: [
          { type: 'video', title: 'Conditional Statements', duration: '25 min' },
          { type: 'video', title: 'Loops in Python', duration: '30 min' },
          { type: 'assignment', title: 'Control Flow Exercises' },
        ],
      },
      {
        week: 3,
        title: 'Functions and Modules',
        lectures: 6,
        duration: '2 hours',
        items: [
          { type: 'video', title: 'Defining Functions', duration: '20 min' },
          { type: 'video', title: 'Working with Modules', duration: '25 min' },
          { type: 'article', title: 'Python Standard Library' },
        ],
      },
      {
        week: 4,
        title: 'Data Structures',
        lectures: 8,
        duration: '3 hours',
        items: [
          { type: 'video', title: 'Lists and Tuples', duration: '30 min' },
          { type: 'video', title: 'Dictionaries and Sets', duration: '35 min' },
          { type: 'assignment', title: 'Data Structure Challenges' },
        ],
      },
      {
        week: 5,
        title: 'Object-Oriented Programming',
        lectures: 8,
        duration: '3 hours',
        items: [
          { type: 'video', title: 'Classes and Objects', duration: '25 min' },
          { type: 'video', title: 'Inheritance and Polymorphism', duration: '30 min' },
          { type: 'project', title: 'OOP Project' },
        ],
      },
      {
        week: 6,
        title: 'Final Project',
        lectures: 8,
        duration: '4 hours',
        items: [
          { type: 'video', title: 'Project Requirements', duration: '20 min' },
          { type: 'article', title: 'Project Guidelines' },
          { type: 'project', title: 'Complete Python Application' },
        ],
      },
    ],
    reviews: [
      {
        id: 1,
        author: 'Jane Smith',
        rating: 5,
        date: '2 weeks ago',
        comment: 'Excellent course! The instructor explains concepts clearly and the projects are very practical.',
      },
      {
        id: 2,
        author: 'Mike Johnson',
        rating: 4,
        date: '1 month ago',
        comment: 'Great content, but some sections could use more examples. Overall very satisfied.',
      },
    ],
  };

  const handleEnroll = () => {
    setIsEnrolled(true);
    // In a real app, you would call your backend API here
  };

  return (
    <Box sx={{ py: 4 }}>
      <Container maxWidth="lg">
        <Grid container spacing={4}>
          {/* Main Course Content */}
          <Grid item xs={12} md={8}>
            <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 700 }}>
              {course.title}
            </Typography>

            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar src={course.instructorAvatar} sx={{ mr: 2 }} />
              <Box>
                <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                  {course.instructor}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {course.institution}
                </Typography>
              </Box>
            </Box>

            <CardMedia
              component="img"
              height="450"
              image={course.image}
              alt={course.title}
              sx={{ borderRadius: 2, mb: 3 }}
            />

            {/* Course Tabs */}
            <Box sx={{ mb: 4 }}>
              <Tabs
                value={activeTab}
                onChange={(e, newValue) => setActiveTab(newValue)}
                variant="scrollable"
                scrollButtons="auto"
                allowScrollButtonsMobile
              >
                <Tab value="overview" label="Overview" />
                <Tab value="syllabus" label="Syllabus" />
                <Tab value="reviews" label="Reviews" />
              </Tabs>
            </Box>

            {/* Tab Content */}
            {activeTab === 'overview' && (
              <Box>
                <Typography variant="h5" gutterBottom sx={{ fontWeight: 600 }}>
                  About This Course
                </Typography>
                <Typography variant="body1" paragraph>
                  {course.longDescription}
                </Typography>

                <Typography variant="h5" gutterBottom sx={{ mt: 4, fontWeight: 600 }}>
                  What You'll Learn
                </Typography>
                <Grid container spacing={2} sx={{ mb: 4 }}>
                  {course.whatYouWillLearn.map((item, index) => (
                    <Grid item xs={12} sm={6} key={index}>
                      <Box sx={{ display: 'flex', alignItems: 'flex-start' }}>
                        <Box sx={{ color: 'primary.main', mr: 1.5, mt: 0.5 }}>
                          <PlayIcon fontSize="small" />
                        </Box>
                        <Typography variant="body1">{item}</Typography>
                      </Box>
                    </Grid>
                  ))}
                </Grid>

                <Typography variant="h5" gutterBottom sx={{ fontWeight: 600 }}>
                  Requirements
                </Typography>
                <List dense>
                  {course.requirements.map((req, index) => (
                    <ListItem key={index}>
                      <ListItemIcon sx={{ minWidth: 32 }}>
                        <PlayIcon fontSize="small" color="primary" />
                      </ListItemIcon>
                      <ListItemText primary={req} />
                    </ListItem>
                  ))}
                </List>
              </Box>
            )}

            {activeTab === 'syllabus' && (
              <Box>
                <Typography variant="h5" gutterBottom sx={{ fontWeight: 600 }}>
                  Course Content
                </Typography>
                <Box sx={{ mb: 2 }}>
                  <Typography variant="body2" color="text.secondary">
                    {course.lectures} lectures • {course.duration} total length
                  </Typography>
                </Box>

                {course.syllabus.map((week, weekIndex) => (
                  <Card key={weekIndex} sx={{ mb: 2 }}>
                    <CardContent>
                      <Typography variant="h6" sx={{ fontWeight: 600 }}>
                        Week {week.week}: {week.title}
                      </Typography>
                      <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                        {week.lectures} lectures • {week.duration}
                      </Typography>

                      <List dense>
                        {week.items.map((item, itemIndex) => (
                          <ListItem key={itemIndex} sx={{ py: 0.5 }}>
                            <ListItemIcon sx={{ minWidth: 32 }}>
                              {item.type === 'video' && <PlayIcon fontSize="small" color="primary" />}
                              {item.type === 'article' && <ArticleIcon fontSize="small" color="primary" />}
                              {item.type === 'quiz' && <QuizIcon fontSize="small" color="primary" />}
                              {item.type === 'assignment' && <AssignmentIcon fontSize="small" color="primary" />}
                              {item.type === 'project' && <AssignmentIcon fontSize="small" color="primary" />}
                            </ListItemIcon>
                            <ListItemText
                              primary={item.title}
                              secondary={item.duration || ''}
                            />
                          </ListItem>
                        ))}
                      </List>
                    </CardContent>
                  </Card>
                ))}
              </Box>
            )}

            {activeTab === 'reviews' && (
              <Box>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
                  <Typography variant="h5" sx={{ fontWeight: 600, mr: 2 }}>
                    Student Reviews
                  </Typography>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <StarIcon sx={{ color: 'warning.main', fontSize: 24, mr: 0.5 }} />
                    <Typography variant="h6" sx={{ fontWeight: 600 }}>
                      {course.rating}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" sx={{ ml: 1 }}>
                      ({course.reviews} reviews)
                    </Typography>
                  </Box>
                </Box>

                {course.reviews.map((review) => (
                  <Box key={review.id} sx={{ mb: 3 }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                      <Avatar sx={{ mr: 2 }}>{review.author.charAt(0)}</Avatar>
                      <Box>
                        <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                          {review.author}
                        </Typography>
                        <Box sx={{ display: 'flex', alignItems: 'center' }}>
                          <StarIcon sx={{ color: 'warning.main', fontSize: 16, mr: 0.5 }} />
                          <Typography variant="body2" color="text.secondary">
                            {review.rating} • {review.date}
                          </Typography>
                        </Box>
                      </Box>
                    </Box>
                    <Typography variant="body1">{review.comment}</Typography>
                  </Box>
                ))}

                <Button variant="outlined" color="primary" sx={{ mt: 2 }}>
                  Load More Reviews
                </Button>
              </Box>
            )}
          </Grid>

          {/* Sidebar */}
          <Grid item xs={12} md={4}>
            <Card sx={{ position: 'sticky', top: 20 }}>
              <CardContent>
                {course.isDiscounted && (
                  <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                    <Typography variant="h5" sx={{ fontWeight: 600, color: 'error.main', mr: 2 }}>
                      {course.discountPrice}
                    </Typography>
                    <Typography variant="body1" sx={{ textDecoration: 'line-through', color: 'text.secondary' }}>
                      {course.price}
                    </Typography>
                  </Box>
                )}
                {!course.isDiscounted && (
                  <Typography variant="h5" sx={{ fontWeight: 600, mb: 2 }}>
                    {course.price}
                  </Typography>
                )}

                {isEnrolled ? (
                  <Button
                    fullWidth
                    variant="contained"
                    color="primary"
                    size="large"
                    component={Link}
                    to={`/learn/${course.id}`}
                    sx={{ mb: 2 }}
                  >
                    Continue Learning
                  </Button>
                ) : (
                  <Button
                    fullWidth
                    variant="contained"
                    color="primary"
                    size="large"
                    onClick={handleEnroll}
                    sx={{ mb: 2 }}
                  >
                    Enroll Now
                  </Button>
                )}

                <Box sx={{ mb: 3 }}>
                  <Typography variant="subtitle2" gutterBottom sx={{ fontWeight: 600 }}>
                    This course includes:
                  </Typography>
                  <List dense>
                    <ListItem sx={{ px: 0, py: 0.5 }}>
                      <ListItemIcon sx={{ minWidth: 32 }}>
                        <PlayIcon fontSize="small" color="primary" />
                      </ListItemIcon>
                      <ListItemText primary={`${course.lectures} on-demand videos`} />
                    </ListItem>
                    <ListItem sx={{ px: 0, py: 0.5 }}>
                      <ListItemIcon sx={{ minWidth: 32 }}>
                        <ArticleIcon fontSize="small" color="primary" />
                      </ListItemIcon>
                      <ListItemText primary="Downloadable resources" />
                    </ListItem>
                    <ListItem sx={{ px: 0, py: 0.5 }}>
                      <ListItemIcon sx={{ minWidth: 32 }}>
                        <AssignmentIcon fontSize="small" color="primary" />
                      </ListItemIcon>
                      <ListItemText primary="Assignments" />
                    </ListItem>
                    <ListItem sx={{ px: 0, py: 0.5 }}>
                      <ListItemIcon sx={{ minWidth: 32 }}>
                        <QuizIcon fontSize="small" color="primary" />
                      </ListItemIcon>
                      <ListItemText primary="Quizzes" />
                    </ListItem>
                    <ListItem sx={{ px: 0, py: 0.5 }}>
                      <ListItemIcon sx={{ minWidth: 32 }}>
                        <ScheduleIcon fontSize="small" color="primary" />
                      </ListItemIcon>
                      <ListItemText primary="Full lifetime access" />
                    </ListItem>
                  </List>
                </Box>

                <Box sx={{ display: 'flex', gap: 1 }}>
                  <IconButton aria-label="bookmark" color="primary">
                    <BookmarkIcon />
                  </IconButton>
                  <IconButton aria-label="share" color="primary">
                    <ShareIcon />
                  </IconButton>
                </Box>
              </CardContent>
            </Card>

            <Card sx={{ mt: 3 }}>
              <CardContent>
                <Typography variant="h6" gutterBottom sx={{ fontWeight: 600 }}>
                  Course Details
                </Typography>
                <Box sx={{ mb: 2 }}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Instructor
                  </Typography>
                  <Typography variant="body1">{course.instructor}</Typography>
                </Box>
                <Box sx={{ mb: 2 }}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Level
                  </Typography>
                  <Typography variant="body1">{course.level}</Typography>
                </Box>
                <Box sx={{ mb: 2 }}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Duration
                  </Typography>
                  <Typography variant="body1">{course.duration}</Typography>
                </Box>
                <Box sx={{ mb: 2 }}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Students
                  </Typography>
                  <Typography variant="body1">{course.students.toLocaleString()}</Typography>
                </Box>
                <Box>
                  <Typography variant="subtitle2" color="text.secondary">
                    Language
                  </Typography>
                  <Typography variant="body1">English</Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default CourseDetailPage;