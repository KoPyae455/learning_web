import React, { useState } from 'react';
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
  // Stack,
  TextField,
  InputAdornment,
  Tabs,
  Tab,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import {
  Search as SearchIcon,
  FilterList as FilterIcon,
  Star as StarIcon,
  // People as PeopleIcon,
  // Schedule as ScheduleIcon,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const CoursesPage = () => {
  // const theme = useTheme();
  // const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState('all');
  const [showFilters, setShowFilters] = useState(false);

  // Mock data - replace with actual data from your backend
  const courses = [
    {
      id: 1,
      title: 'Complete Python Programming',
      description: 'Master Python from basics to advanced concepts',
      image: 'https://source.unsplash.com/400x250/?python,programming',
      category: 'programming',
      instructor: 'John Doe',
      rating: 4.8,
      students: 1250,
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
      category: 'web',
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
      category: 'data',
      instructor: 'Mike Johnson',
      rating: 4.7,
      students: 890,
      duration: '15 hours',
      level: 'Intermediate',
      price: '$79.99',
      isFree: false,
    },
    {
      id: 4,
      title: 'Mobile App Development with React Native',
      description: 'Build cross-platform mobile apps with React Native',
      image: 'https://source.unsplash.com/400x250/?mobile,app',
      category: 'mobile',
      instructor: 'Sarah Williams',
      rating: 4.6,
      students: 1500,
      duration: '10 hours',
      level: 'Intermediate',
      price: '$59.99',
      isFree: false,
    },
    {
      id: 5,
      title: 'UI/UX Design Principles',
      description: 'Learn the fundamentals of user interface and experience design',
      image: 'https://source.unsplash.com/400x250/?design,ui',
      category: 'design',
      instructor: 'David Brown',
      rating: 4.5,
      students: 1800,
      duration: '6 hours',
      level: 'Beginner',
      price: 'Free',
      isFree: true,
    },
    {
      id: 6,
      title: 'Advanced JavaScript Patterns',
      description: 'Master advanced JavaScript concepts and patterns',
      image: 'https://source.unsplash.com/400x250/?javascript,code',
      category: 'programming',
      instructor: 'Emily Davis',
      rating: 4.9,
      students: 950,
      duration: '14 hours',
      level: 'Advanced',
      price: '$69.99',
      isFree: false,
    },
  ];

  const filteredCourses = courses.filter(course => {
    const matchesSearch = course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         course.description.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategory = activeTab === 'all' || course.category === activeTab;
    return matchesSearch && matchesCategory;
  });

  const categories = [
    { id: 'all', label: 'All Courses' },
    { id: 'programming', label: 'Programming' },
    { id: 'web', label: 'Web Development' },
    { id: 'data', label: 'Data Science' },
    { id: 'mobile', label: 'Mobile Development' },
    { id: 'design', label: 'Design' },
  ];

  return (
    <Box sx={{ py: 4 }}>
      <Container maxWidth="lg">
        {/* Page Header */}
        <Box sx={{ mb: 6 }}>
          <Typography variant="h2" component="h1" gutterBottom sx={{ fontWeight: 700 }}>
            Explore Our Courses
          </Typography>
          <Typography variant="h6" color="text.secondary">
            Find the perfect course to advance your skills
          </Typography>
        </Box>

        {/* Search and Filter Bar */}
        <Box sx={{ mb: 4 }}>
          <Grid container spacing={2} alignItems="center">
            <Grid item xs={12} md={8}>
              <TextField
                fullWidth
                variant="outlined"
                placeholder="Search courses..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">
                      <SearchIcon />
                    </InputAdornment>
                  ),
                }}
              />
            </Grid>
            <Grid item xs={12} md={4}>
              <Button
                fullWidth
                variant="outlined"
                startIcon={<FilterIcon />}
                onClick={() => setShowFilters(!showFilters)}
                sx={{ height: '56px' }}
              >
                Filters
              </Button>
            </Grid>
          </Grid>

          {showFilters && (
            <Box sx={{ mt: 3, p: 3, backgroundColor: 'background.paper', borderRadius: 2 }}>
              <Typography variant="h6" gutterBottom>
                Filters
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={6} md={3}>
                  <TextField
                    select
                    fullWidth
                    label="Level"
                    SelectProps={{ native: true }}
                    variant="outlined"
                  >
                    <option value="">All Levels</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                  </TextField>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                  <TextField
                    select
                    fullWidth
                    label="Price"
                    SelectProps={{ native: true }}
                    variant="outlined"
                  >
                    <option value="">All Prices</option>
                    <option value="free">Free</option>
                    <option value="paid">Paid</option>
                  </TextField>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                  <TextField
                    select
                    fullWidth
                    label="Duration"
                    SelectProps={{ native: true }}
                    variant="outlined"
                  >
                    <option value="">Any Duration</option>
                    <option value="short">0-5 hours</option>
                    <option value="medium">5-10 hours</option>
                    <option value="long">10+ hours</option>
                  </TextField>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                  <TextField
                    select
                    fullWidth
                    label="Rating"
                    SelectProps={{ native: true }}
                    variant="outlined"
                  >
                    <option value="">Any Rating</option>
                    <option value="4.5">4.5+ stars</option>
                    <option value="4">4+ stars</option>
                    <option value="3">3+ stars</option>
                  </TextField>
                </Grid>
              </Grid>
            </Box>
          )}
        </Box>

        {/* Category Tabs */}
        <Box sx={{ mb: 4 }}>
          <Tabs
            value={activeTab}
            onChange={(e, newValue) => setActiveTab(newValue)}
            variant="scrollable"
            scrollButtons="auto"
            allowScrollButtonsMobile
          >
            {categories.map(category => (
              <Tab key={category.id} value={category.id} label={category.label} />
            ))}
          </Tabs>
        </Box>

        {/* Courses Grid */}
        {filteredCourses.length > 0 ? (
          <Grid container spacing={4}>
            {filteredCourses.map(course => (
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
                      to={`/course/${course.id}`}
                      sx={{ textTransform: 'none' }}
                    >
                      Learn More
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
            ))}
          </Grid>
        ) : (
          <Box sx={{ textAlign: 'center', py: 8 }}>
            <Typography variant="h5" gutterBottom>
              No courses found
            </Typography>
            <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
              Try adjusting your search or filters
            </Typography>
            <Button
              variant="outlined"
              color="primary"
              onClick={() => {
                setSearchQuery('');
                setActiveTab('all');
                setShowFilters(false);
              }}
            >
              Clear all filters
            </Button>
          </Box>
        )}
      </Container>
    </Box>
  );
};

export default CoursesPage;