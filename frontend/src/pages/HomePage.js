import React from 'react';
import {
  Box,
  Container,
  Typography,
  Button,
  Grid,
  Card,
  CardContent,
  CardMedia,
  CardActions,
  Chip,
  Stack,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import {
  School as SchoolIcon,
  VideoLibrary as VideoIcon,
  Article as ArticleIcon,
  TrendingUp as TrendingIcon,
  Star as StarIcon,
  People as PeopleIcon,
  AccessTime as TimeIcon,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';


const HomePage = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const { isAuthenticated } = useAuth();

  const features = [
    {
      icon: <SchoolIcon sx={{ fontSize: 40 }} />,
      title: 'Expert-Led Courses',
      description: 'Learn from industry professionals with real-world experience',
    },
    {
      icon: <VideoIcon sx={{ fontSize: 40 }} />,
      title: 'Video Lessons',
      description: 'High-quality video content with interactive learning experiences',
    },
    {
      icon: <ArticleIcon sx={{ fontSize: 40 }} />,
      title: 'IT Blog',
      description: 'Stay updated with the latest trends and insights in technology',
    },
    {
      icon: <TrendingIcon sx={{ fontSize: 40 }} />,
      title: 'Progress Tracking',
      description: 'Monitor your learning progress and earn certificates',
    },
  ];

  const featuredCourses = [
    {
      id: 1,
      title: 'Complete Python Programming',
      description: 'Master Python from basics to advanced concepts',
      image: 'https://source.unsplash.com/400x250/?python,programming',
      instructor: 'Elon Pyae',
      rating: 4.8,
      students: 120,
      duration: '12 hours',
      level: 'Beginner',
      price: '$49.99',
      isFree: false,
    },
    {
      id: 2,
      title: 'Web Development Fundamentals',
      description: 'Learn HTML, CSS, and JavaScript basics',
      image: 'https://source.unsplash.com/400x250/?web,development',
      instructor: 'Jane Smith',
      rating: 4.9,
      students: 2100,
      duration: '8 hours',
      level: 'Beginner',
      price: 'Free',
      isFree: true,
    },
    {
      id: 3,
      title: 'Data Science Essentials',
      description: 'Introduction to data analysis and visualization',
      image: 'https://source.unsplash.com/400x250/?data,science',
      instructor: 'Mike Johnson',
      rating: 4.7,
      students: 890,
      duration: '15 hours',
      level: 'Intermediate',
      price: '$79.99',
      isFree: false,
    },
  ];

  const stats = [
    { label: 'Students', value: '10K+', icon: <PeopleIcon /> },
    { label: 'Courses', value: '200+', icon: <SchoolIcon /> },
    { label: 'Instructors', value: '50+', icon: <PeopleIcon /> },
    { label: 'Hours of Content', value: '1000+', icon: <TimeIcon /> },
  ];

  return (
    <Box>
      {/* Hero Section */}
      <Box
        sx={{
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          color: 'white',
          py: { xs: 8, md: 12 },
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        <Container maxWidth="lg">
          <Grid container spacing={4} alignItems="center">
            <Grid item xs={12} md={6}>
              <Typography
                variant={isMobile ? 'h3' : 'h1'}
                component="h1"
                gutterBottom
                sx={{ fontWeight: 700 }}
              >
                Master New Skills
                <br />
                <Box component="span" sx={{ color: 'secondary.light' }}>
                  Online
                </Box>
              </Typography>
              <Typography
                variant={isMobile ? 'h6' : 'h5'}
                sx={{ mb: 4, opacity: 0.9, lineHeight: 1.6 }}
              >
                Transform your career with our comprehensive online learning platform.
                Access expert-led courses, video lessons, and stay updated with our IT blog.
              </Typography>
              <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2}>
                {!isAuthenticated ? (
                  <>
                    <Button
                      variant="contained"
                      color="secondary"
                      size="large"
                      component={Link}
                      to="/register"
                      sx={{ px: 4, py: 1.5, fontSize: '1.1rem' }}
                    >
                      Get Started
                    </Button>
                    <Button
                      variant="outlined"
                      color="inherit"
                      size="large"
                      component={Link}
                      to="/courses"
                      sx={{ px: 4, py: 1.5, fontSize: '1.1rem' }}
                    >
                      Browse Courses
                    </Button>
                  </>
                ) : (
                  <Button
                    variant="contained"
                    color="secondary"
                    size="large"
                    component={Link}
                    to="/dashboard"
                    sx={{ px: 4, py: 1.5, fontSize: '1.1rem' }}
                  >
                    Go to Dashboard
                  </Button>
                )}
              </Stack>
            </Grid>
            <Grid item xs={12} md={6}>
              <Box
                sx={{
                  display: 'flex',
                  justifyContent: 'center',
                  alignItems: 'center',
                  height: '100%',
                }}
              >
                <Box
                  component="img"
                  src="https://media.geeksforgeeks.org/wp-content/uploads/20240319155102/what-is-ai-artificial-intelligence.webp"
                  alt="Online Learning"
                  sx={{
                    width: '100%',
                    maxWidth: 500,
                    borderRadius: 4,
                    boxShadow: '0 20px 40px rgba(0,0,0,0.3)',
                  }}
                />
              </Box>
            </Grid>
          </Grid>
        </Container>
      </Box>

      {/* Stats Section */}
      <Container maxWidth="lg" sx={{ py: 6 }}>
        <Grid container spacing={4}>
          {stats.map((stat, index) => (
            <Grid item xs={6} md={3} key={index}>
              <Box
                sx={{
                  textAlign: 'center',
                  p: 3,
                  borderRadius: 2,
                  backgroundColor: 'background.paper',
                  boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                }}
              >
                <Box sx={{ color: 'primary.main', mb: 1 }}>{stat.icon}</Box>
                <Typography variant="h4" component="div" sx={{ fontWeight: 700, mb: 1 }}>
                  {stat.value}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {stat.label}
                </Typography>
              </Box>
            </Grid>
          ))}
        </Grid>
      </Container>

      {/* Features Section */}
      <Box sx={{ py: 8, backgroundColor: 'background.default' }}>
        <Container maxWidth="lg">
          <Typography
            variant="h2"
            component="h2"
            align="center"
            gutterBottom
            sx={{ mb: 6, fontWeight: 600 }}
          >
            Why Choose Our Platform?
          </Typography>
          <Grid container spacing={4}>
            {features.map((feature, index) => (
              <Grid item xs={12} sm={6} md={3} key={index}>
                <Box
                  sx={{
                    textAlign: 'center',
                    p: 3,
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                  }}
                >
                  <Box sx={{ color: 'primary.main', mb: 2 }}>{feature.icon}</Box>
                  <Typography variant="h6" component="h3" gutterBottom sx={{ fontWeight: 600 }}>
                    {feature.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" sx={{ lineHeight: 1.6 }}>
                    {feature.description}
                  </Typography>
                </Box>
              </Grid>
            ))}
          </Grid>
        </Container>
      </Box>

      {/* Featured Courses Section */}
      <Container maxWidth="lg" sx={{ py: 8 }}>
        <Box sx={{ textAlign: 'center', mb: 6 }}>
          <Typography variant="h2" component="h2" gutterBottom sx={{ fontWeight: 600 }}>
            Featured Courses
          </Typography>
          <Typography variant="h6" color="text.secondary" sx={{ maxWidth: 600, mx: 'auto' }}>
            Start your learning journey with our most popular courses
          </Typography>
        </Box>

        <Grid container spacing={4}>
          {featuredCourses.map((course) => (
            <Grid item xs={12} sm={6} md={4} key={course.id}>
              <Card
                sx={{
                  height: '100%',
                  display: 'flex',
                  flexDirection: 'column',
                  transition: 'transform 0.2s, box-shadow 0.2s',
                  '&:hover': {
                    transform: 'translateY(-4px)',
                    boxShadow: '0 8px 25px rgba(0,0,0,0.15)',
                  },
                }}
              >
                <CardMedia
                  component="img"
                  height="200"
                  image={course.image}
                  alt={course.title}
                />
                <CardContent sx={{ flexGrow: 1 }}>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                    <Chip
                      label={course.level}
                      size="small"
                      color="primary"
                      variant="outlined"
                    />
                    <Typography variant="h6" color="primary" sx={{ fontWeight: 600 }}>
                      {course.price}
                    </Typography>
                  </Box>
                  <Typography variant="h6" component="h3" gutterBottom sx={{ fontWeight: 600 }}>
                    {course.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                    {course.description}
                  </Typography>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
                    <StarIcon sx={{ color: 'warning.main', fontSize: 20 }} />
                    <Typography variant="body2" sx={{ fontWeight: 600 }}>
                      {course.rating}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      ({course.students} students)
                    </Typography>
                  </Box>
                  <Typography variant="body2" color="text.secondary">
                    {course.duration} • {course.instructor}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button
                    size="small"
                    color="primary"
                    component={Link}
                    to={`/courses/${course.id}`}
                    sx={{ textTransform: 'none' }}
                  >
                    Learn More
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>

        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button
            variant="contained"
            color="primary"
            size="large"
            component={Link}
            to="/courses"
            sx={{ px: 6, py: 1.5, fontSize: '1.1rem' }}
          >
            View All Courses
          </Button>
        </Box>
      </Container>
    </Box>
  );
};

export default HomePage;
