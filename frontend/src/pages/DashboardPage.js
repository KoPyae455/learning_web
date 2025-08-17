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
  Avatar,
  LinearProgress,
  Divider,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import {
  School as SchoolIcon,
  TrendingUp as TrendingIcon,
  Bookmark as BookmarkIcon,
  Star as StarIcon,
  Schedule as ScheduleIcon,
  CheckCircle as CheckIcon,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const DashboardPage = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));

  // Mock data - replace with actual data from your backend
  const enrolledCourses = [
    {
      id: 1,
      title: 'Complete Python Programming',
      progress: 65,
      lastAccessed: '2 days ago',
      image: 'https://source.unsplash.com/400x250/?python,programming',
      nextLesson: 'Functions and Modules',
    },
    {
      id: 2,
      title: 'Web Development Fundamentals',
      progress: 30,
      lastAccessed: '1 week ago',
      image: 'https://source.unsplash.com/400x250/?web,development',
      nextLesson: 'CSS Flexbox',
    },
    {
      id: 3,
      title: 'Data Science Essentials',
      progress: 90,
      lastAccessed: 'Yesterday',
      image: 'https://source.unsplash.com/400x250/?data,science',
      nextLesson: 'Final Project',
    },
  ];

  const recommendedCourses = [
    {
      id: 4,
      title: 'Advanced JavaScript Patterns',
      category: 'Programming',
      image: 'https://source.unsplash.com/400x250/?javascript,code',
    },
    {
      id: 5,
      title: 'UI/UX Design Principles',
      category: 'Design',
      image: 'https://source.unsplash.com/400x250/?design,ui',
    },
  ];

  const achievements = [
    { title: '7-Day Streak', icon: <TrendingIcon />, progress: 100 },
    { title: 'Course Explorer', icon: <SchoolIcon />, progress: 75 },
    { title: 'Quick Learner', icon: <CheckIcon />, progress: 50 },
  ];

  return (
    <Box sx={{ py: 4 }}>
      <Container maxWidth="lg">
        {/* Dashboard Header */}
        <Box sx={{ mb: 4 }}>
          <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 700 }}>
            My Dashboard
          </Typography>
          <Typography variant="h6" color="text.secondary">
            Welcome back! Continue your learning journey.
          </Typography>
        </Box>

        {/* Stats Cards */}
        <Grid container spacing={3} sx={{ mb: 4 }}>
          <Grid item xs={12} sm={6} md={3}>
            <Card sx={{ height: '100%' }}>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <Avatar sx={{ bgcolor: 'primary.light', mr: 2 }}>
                    <SchoolIcon sx={{ color: 'primary.main' }} />
                  </Avatar>
                  <Box>
                    <Typography variant="h6" sx={{ fontWeight: 600 }}>
                      3
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Active Courses
                    </Typography>
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card sx={{ height: '100%' }}>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <Avatar sx={{ bgcolor: 'success.light', mr: 2 }}>
                    <CheckIcon sx={{ color: 'success.main' }} />
                  </Avatar>
                  <Box>
                    <Typography variant="h6" sx={{ fontWeight: 600 }}>
                      62%
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Completion Rate
                    </Typography>
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card sx={{ height: '100%' }}>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <Avatar sx={{ bgcolor: 'warning.light', mr: 2 }}>
                    <StarIcon sx={{ color: 'warning.main' }} />
                  </Avatar>
                  <Box>
                    <Typography variant="h6" sx={{ fontWeight: 600 }}>
                      4.8
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Average Rating
                    </Typography>
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card sx={{ height: '100%' }}>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <Avatar sx={{ bgcolor: 'info.light', mr: 2 }}>
                    <ScheduleIcon sx={{ color: 'info.main' }} />
                  </Avatar>
                  <Box>
                    <Typography variant="h6" sx={{ fontWeight: 600 }}>
                      3 days
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Learning Streak
                    </Typography>
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        </Grid>

        {/* My Courses Section */}
        <Box sx={{ mb: 6 }}>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
            <Typography variant="h5" component="h2" sx={{ fontWeight: 600 }}>
              My Courses
            </Typography>
            <Button
              variant="outlined"
              color="primary"
              component={Link}
              to="/courses"
            >
              Browse All Courses
            </Button>
          </Box>

          <Grid container spacing={3}>
            {enrolledCourses.map((course) => (
              <Grid item xs={12} md={6} key={course.id}>
                <Card sx={{ display: 'flex', height: '100%' }}>
                  <CardMedia
                    component="img"
                    sx={{ width: 150, display: { xs: 'none', sm: 'block' } }}
                    image={course.image}
                    alt={course.title}
                  />
                  <Box sx={{ display: 'flex', flexDirection: 'column', flexGrow: 1 }}>
                    <CardContent sx={{ flex: '1 0 auto' }}>
                      <Typography variant="h6" component="h3" sx={{ fontWeight: 600 }}>
                        {course.title}
                      </Typography>
                      <Box sx={{ mt: 2, mb: 1 }}>
                        <LinearProgress
                          variant="determinate"
                          value={course.progress}
                          sx={{ height: 8, borderRadius: 4, mb: 1 }}
                        />
                        <Typography variant="body2" color="text.secondary">
                          {course.progress}% complete • Last accessed: {course.lastAccessed}
                        </Typography>
                      </Box>
                      <Typography variant="body2" sx={{ mt: 1 }}>
                        Next: {course.nextLesson}
                      </Typography>
                    </CardContent>
                    <CardActions sx={{ justifyContent: 'flex-end' }}>
                      <Button
                        size="small"
                        color="primary"
                        component={Link}
                        to={`/learn/${course.id}`}
                      >
                        Continue
                      </Button>
                    </CardActions>
                  </Box>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Box>

        {/* Recommended Courses Section */}
        <Box sx={{ mb: 6 }}>
          <Typography variant="h5" component="h2" sx={{ fontWeight: 600, mb: 3 }}>
            Recommended For You
          </Typography>

          <Grid container spacing={3}>
            {recommendedCourses.map((course) => (
              <Grid item xs={12} sm={6} key={course.id}>
                <Card sx={{ height: '100%' }}>
                  <CardMedia
                    component="img"
                    height="140"
                    image={course.image}
                    alt={course.title}
                  />
                  <CardContent>
                    <Typography variant="h6" component="h3" sx={{ fontWeight: 600 }}>
                      {course.title}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                      {course.category}
                    </Typography>
                    <Button
                      size="small"
                      color="primary"
                      component={Link}
                      to={`/course/${course.id}`}
                    >
                      View Course
                    </Button>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Box>

        {/* Achievements Section */}
        <Box>
          <Typography variant="h5" component="h2" sx={{ fontWeight: 600, mb: 3 }}>
            My Achievements
          </Typography>

          <Grid container spacing={3}>
            {achievements.map((achievement, index) => (
              <Grid item xs={12} sm={4} key={index}>
                <Card sx={{ height: '100%' }}>
                  <CardContent>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                      <Avatar sx={{ bgcolor: 'primary.light', mr: 2 }}>
                        {achievement.icon}
                      </Avatar>
                      <Typography variant="h6" sx={{ fontWeight: 600 }}>
                        {achievement.title}
                      </Typography>
                    </Box>
                    <LinearProgress
                      variant="determinate"
                      value={achievement.progress}
                      sx={{ height: 8, borderRadius: 4 }}
                    />
                    <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                      {achievement.progress}% complete
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Box>
      </Container>
    </Box>
  );
};

export default DashboardPage;