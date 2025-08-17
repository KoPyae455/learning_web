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
  Stack,
  TextField,
  InputAdornment,
  Tabs,
  Tab,
  Pagination,
  // useTheme,
  // useMediaQuery,
  IconButton,
} from '@mui/material';
import {
  Search as SearchIcon,
  FilterList as FilterIcon,
  Bookmark as BookmarkIcon,
  Share as ShareIcon,
  CalendarToday as CalendarIcon,
  Person as PersonIcon,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const BlogPage = () => {
  // const theme = useTheme();
  // const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState('all');
  const [currentPage, setCurrentPage] = useState(1);
  const postsPerPage = 6;

  // Mock blog posts - replace with actual data from your backend
  const blogPosts = [
    {
      id: 1,
      title: 'Getting Started with React Hooks',
      excerpt: 'Learn how to use React Hooks to simplify your functional components',
      image: 'https://source.unsplash.com/600x400/?react,javascript',
      category: 'react',
      author: 'Jane Smith',
      date: 'May 15, 2023',
      readTime: '5 min read',
      tags: ['react', 'hooks', 'frontend'],
    },
    {
      id: 2,
      title: 'The Future of Web Development in 2023',
      excerpt: 'Explore the latest trends and technologies shaping web development',
      image: 'https://source.unsplash.com/600x400/?web,development',
      category: 'web',
      author: 'John Doe',
      date: 'April 28, 2023',
      readTime: '8 min read',
      tags: ['web', 'trends', 'technology'],
    },
    {
      id: 3,
      title: 'Python Tips and Tricks for Beginners',
      excerpt: 'Essential Python tips that every beginner should know',
      image: 'https://source.unsplash.com/600x400/?python,code',
      category: 'python',
      author: 'Mike Johnson',
      date: 'April 10, 2023',
      readTime: '6 min read',
      tags: ['python', 'beginners', 'programming'],
    },
    {
      id: 4,
      title: 'Building Scalable APIs with Node.js',
      excerpt: 'Best practices for creating scalable and maintainable APIs',
      image: 'https://source.unsplash.com/600x400/?nodejs,api',
      category: 'node',
      author: 'Sarah Williams',
      date: 'March 22, 2023',
      readTime: '10 min read',
      tags: ['nodejs', 'backend', 'api'],
    },
    {
      id: 5,
      title: 'CSS Grid vs Flexbox: When to Use Each',
      excerpt: 'A comprehensive comparison between CSS Grid and Flexbox',
      image: 'https://source.unsplash.com/600x400/?css,design',
      category: 'css',
      author: 'David Brown',
      date: 'March 15, 2023',
      readTime: '7 min read',
      tags: ['css', 'frontend', 'design'],
    },
    {
      id: 6,
      title: 'Introduction to Machine Learning Concepts',
      excerpt: 'Fundamental concepts you need to understand machine learning',
      image: 'https://source.unsplash.com/600x400/?machine,learning',
      category: 'ml',
      author: 'Emily Davis',
      date: 'February 28, 2023',
      readTime: '12 min read',
      tags: ['ml', 'ai', 'datascience'],
    },
  ];

  const categories = [
    { id: 'all', label: 'All Posts' },
    { id: 'react', label: 'React' },
    { id: 'web', label: 'Web Development' },
    { id: 'python', label: 'Python' },
    { id: 'node', label: 'Node.js' },
    { id: 'css', label: 'CSS' },
    { id: 'ml', label: 'Machine Learning' },
  ];

  const filteredPosts = blogPosts.filter(post => {
    const matchesSearch = post.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         post.excerpt.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategory = activeTab === 'all' || post.category === activeTab;
    return matchesSearch && matchesCategory;
  });

  // Pagination logic
  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentPosts = filteredPosts.slice(indexOfFirstPost, indexOfLastPost);
  const totalPages = Math.ceil(filteredPosts.length / postsPerPage);

  const handlePageChange = (event, value) => {
    setCurrentPage(value);
  };

  return (
    <Box sx={{ py: 4 }}>
      <Container maxWidth="lg">
        {/* Page Header */}
        <Box sx={{ mb: 6, textAlign: 'center' }}>
          <Typography variant="h2" component="h1" gutterBottom sx={{ fontWeight: 700 }}>
            IT Blog
          </Typography>
          <Typography variant="h6" color="text.secondary">
            Stay updated with the latest trends, tutorials, and insights in technology
          </Typography>
        </Box>

        {/* Search and Filter Bar */}
        <Box sx={{ mb: 4 }}>
          <Grid container spacing={2} alignItems="center">
            <Grid item xs={12} md={8}>
              <TextField
                fullWidth
                variant="outlined"
                placeholder="Search blog posts..."
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
                sx={{ height: '56px' }}
              >
                Filters
              </Button>
            </Grid>
          </Grid>
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

        {/* Blog Posts Grid */}
        {currentPosts.length > 0 ? (
          <>
            <Grid container spacing={4} sx={{ mb: 4 }}>
              {currentPosts.map(post => (
                <Grid item xs={12} sm={6} md={4} key={post.id}>
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
                      image={post.image}
                      alt={post.title}
                    />
                    <CardContent sx={{ flexGrow: 1 }}>
                      <Chip
                        label={post.category}
                        size="small"
                        color="primary"
                        variant="outlined"
                        sx={{ mb: 1.5 }}
                      />
                      <Typography variant="h6" component="h3" gutterBottom sx={{ fontWeight: 600 }}>
                        {post.title}
                      </Typography>
                      <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                        {post.excerpt}
                      </Typography>
                      <Stack direction="row" spacing={1} sx={{ mb: 1 }}>
                        {post.tags.map((tag, index) => (
                          <Chip
                            key={index}
                            label={tag}
                            size="small"
                            variant="outlined"
                          />
                        ))}
                      </Stack>
                      <Box sx={{ display: 'flex', alignItems: 'center', mt: 2 }}>
                        <PersonIcon fontSize="small" sx={{ mr: 1, color: 'text.secondary' }} />
                        <Typography variant="body2" color="text.secondary" sx={{ mr: 2 }}>
                          {post.author}
                        </Typography>
                        <CalendarIcon fontSize="small" sx={{ mr: 1, color: 'text.secondary' }} />
                        <Typography variant="body2" color="text.secondary">
                          {post.date}
                        </Typography>
                      </Box>
                    </CardContent>
                    <CardActions sx={{ justifyContent: 'space-between' }}>
                      <Typography variant="body2" color="text.secondary">
                        {post.readTime}
                      </Typography>
                      <Box>
                        <IconButton aria-label="bookmark" size="small">
                          <BookmarkIcon fontSize="small" />
                        </IconButton>
                        <IconButton aria-label="share" size="small">
                          <ShareIcon fontSize="small" />
                        </IconButton>
                        <Button
                          size="small"
                          color="primary"
                          component={Link}
                          to={`/blog/${post.id}`}
                          sx={{ ml: 1 }}
                        >
                          Read More
                        </Button>
                      </Box>
                    </CardActions>
                  </Card>
                </Grid>
              ))}
            </Grid>

            {/* Pagination */}
            {totalPages > 1 && (
              <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
                <Pagination
                  count={totalPages}
                  page={currentPage}
                  onChange={handlePageChange}
                  color="primary"
                  // size={isMobile ? 'small' : 'medium'}
                />
              </Box>
            )}
          </>
        ) : (
          <Box sx={{ textAlign: 'center', py: 8 }}>
            <Typography variant="h5" gutterBottom>
              No blog posts found
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

export default BlogPage;