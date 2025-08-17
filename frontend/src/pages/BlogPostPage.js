import React from 'react';
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
  Divider,
  Chip,
  Stack,
  Avatar,
  IconButton,
  TextField,
  // useTheme,
  // useMediaQuery,
} from '@mui/material';
import {
  Bookmark as BookmarkIcon,
  Share as ShareIcon,
  CalendarToday as CalendarIcon,
  Person as PersonIcon,
  ArrowBack as BackIcon,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const BlogPostPage = () => {
  const { id } = useParams();
  // const theme = useTheme();
  // const isMobile = useMediaQuery(theme.breakpoints.down('md'));

  // Mock blog post data - replace with actual data from your backend
  const post = {
    id: id,
    title: 'Getting Started with React Hooks',
    content: `
      <p>React Hooks have revolutionized how we write React components. Introduced in React 16.8, hooks allow you to use state and other React features without writing classes.</p>
      
      <h2>Why Use Hooks?</h2>
      <p>Hooks solve several problems in React:</p>
      <ul>
        <li>It's hard to reuse stateful logic between components</li>
        <li>Complex components become hard to understand</li>
        <li>Classes confuse both people and machines</li>
      </ul>
      
      <h2>Basic Hooks</h2>
      <h3>useState</h3>
      <p>The useState hook lets you add React state to function components:</p>
      <pre><code>const [count, setCount] = useState(0);</code></pre>
      
      <h3>useEffect</h3>
      <p>The Effect Hook lets you perform side effects in function components:</p>
      <pre><code>useEffect(() => {
        document.title = \`You clicked \${count} times\`;
      });</code></pre>
      
      <h2>Custom Hooks</h2>
      <p>Building your own hooks lets you extract component logic into reusable functions.</p>
      <p>For example, this custom hook tracks window size:</p>
      <pre><code>function useWindowSize() {
        const [size, setSize] = useState([0, 0]);
        useEffect(() => {
          function updateSize() {
            setSize([window.innerWidth, window.innerHeight]);
          }
          window.addEventListener('resize', updateSize);
          updateSize();
          return () => window.removeEventListener('resize', updateSize);
        }, []);
        return size;
      }</code></pre>
      
      <h2>Rules of Hooks</h2>
      <p>Hooks have two important rules:</p>
      <ol>
        <li>Only call hooks at the top level</li>
        <li>Only call hooks from React functions</li>
      </ol>
      
      <h2>Conclusion</h2>
      <p>Hooks provide a more direct API to the React concepts you already know: props, state, context, refs, and lifecycle. They don't fundamentally change how React works, but they make your code cleaner and easier to understand.</p>
    `,
    image: 'https://source.unsplash.com/800x450/?react,javascript',
    category: 'react',
    author: 'Jane Smith',
    authorAvatar: 'https://source.unsplash.com/100x100/?portrait,woman',
    authorBio: 'Senior React Developer with 5+ years of experience. Loves teaching and sharing knowledge about frontend technologies.',
    date: 'May 15, 2023',
    readTime: '5 min read',
    tags: ['react', 'hooks', 'frontend'],
    relatedPosts: [
      {
        id: 4,
        title: 'Building Scalable APIs with Node.js',
        excerpt: 'Best practices for creating scalable and maintainable APIs',
        image: 'https://source.unsplash.com/400x250/?nodejs,api',
        date: 'March 22, 2023',
      },
      {
        id: 5,
        title: 'CSS Grid vs Flexbox: When to Use Each',
        excerpt: 'A comprehensive comparison between CSS Grid and Flexbox',
        image: 'https://source.unsplash.com/400x250/?css,design',
        date: 'March 15, 2023',
      },
    ],
  };

  return (
    <Box sx={{ py: 4 }}>
      <Container maxWidth="lg">
        <Button
          startIcon={<BackIcon />}
          component={Link}
          to="/blog"
          sx={{ mb: 3 }}
        >
          Back to Blog
        </Button>

        <Grid container spacing={4}>
          {/* Main Content */}
          <Grid item xs={12} md={8}>
            <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 700 }}>
              {post.title}
            </Typography>

            <Box sx={{ display: 'flex', alignItems: 'center', mb: 4 }}>
              <Avatar src={post.authorAvatar} sx={{ mr: 2 }} />
              <Box>
                <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                  {post.author}
                </Typography>
                <Box sx={{ display: 'flex', alignItems: 'center' }}>
                  <CalendarIcon fontSize="small" sx={{ mr: 1, color: 'text.secondary' }} />
                  <Typography variant="body2" color="text.secondary" sx={{ mr: 2 }}>
                    {post.date}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {post.readTime}
                  </Typography>
                </Box>
              </Box>
            </Box>

            <CardMedia
              component="img"
              height="450"
              image={post.image}
              alt={post.title}
              sx={{ borderRadius: 2, mb: 4 }}
            />

            <Stack direction="row" spacing={1} sx={{ mb: 4 }}>
              {post.tags.map((tag, index) => (
                <Chip
                  key={index}
                  label={tag}
                  size="small"
                  color="primary"
                  variant="outlined"
                />
              ))}
            </Stack>

            <Box
              sx={{
                '& h2': { 
                  fontSize: '1.75rem',
                  fontWeight: 600,
                  mt: 4,
                  mb: 2,
                },
                '& h3': { 
                  fontSize: '1.5rem',
                  fontWeight: 600,
                  mt: 3,
                  mb: 1.5,
                },
                '& p': {
                  fontSize: '1.1rem',
                  lineHeight: 1.8,
                  mb: 2,
                },
                '& ul, & ol': {
                  pl: 3,
                  mb: 2,
                  '& li': {
                    mb: 1,
                  },
                },
                '& pre': {
                  // backgroundColor: theme.palette.mode === 'dark' ? '#1E1E1E' : '#f5f5f5',
                  p: 2,
                  borderRadius: 1,
                  overflowX: 'auto',
                  mb: 2,
                },
                '& code': {
                  fontFamily: 'monospace',
                },
              }}
              dangerouslySetInnerHTML={{ __html: post.content }}
            />

            <Divider sx={{ my: 4 }} />

            <Box sx={{ display: 'flex', alignItems: 'center', mb: 4 }}>
              <Avatar src={post.authorAvatar} sx={{ width: 80, height: 80, mr: 3 }} />
              <Box>
                <Typography variant="h6" component="h3" gutterBottom sx={{ fontWeight: 600 }}>
                  About {post.author}
                </Typography>
                <Typography variant="body1" paragraph>
                  {post.authorBio}
                </Typography>
              </Box>
            </Box>

            <Box sx={{ display: 'flex', gap: 1, mb: 4 }}>
              <IconButton aria-label="bookmark" color="primary">
                <BookmarkIcon />
              </IconButton>
              <IconButton aria-label="share" color="primary">
                <ShareIcon />
              </IconButton>
            </Box>
          </Grid>

          {/* Sidebar */}
          <Grid item xs={12} md={4}>
            <Card sx={{ position: 'sticky', top: 20, mb: 4 }}>
              <CardContent>
                <Typography variant="h6" component="h3" gutterBottom sx={{ fontWeight: 600 }}>
                  Related Posts
                </Typography>
                <Stack spacing={2}>
                  {post.relatedPosts.map(relatedPost => (
                    <Card key={relatedPost.id} sx={{ display: 'flex' }}>
                      <CardMedia
                        component="img"
                        sx={{ width: 100, display: { xs: 'none', sm: 'block' } }}
                        image={relatedPost.image}
                        alt={relatedPost.title}
                      />
                      <Box sx={{ display: 'flex', flexDirection: 'column', p: 1.5 }}>
                        <Typography variant="subtitle2" component="h4" sx={{ fontWeight: 600 }}>
                          {relatedPost.title}
                        </Typography>
                        <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                          {relatedPost.date}
                        </Typography>
                        <Button
                          size="small"
                          color="primary"
                          component={Link}
                          to={`/blog/${relatedPost.id}`}
                          sx={{ alignSelf: 'flex-start', mt: 'auto' }}
                        >
                          Read
                        </Button>
                      </Box>
                    </Card>
                  ))}
                </Stack>
              </CardContent>
            </Card>

            <Card>
              <CardContent>
                <Typography variant="h6" component="h3" gutterBottom sx={{ fontWeight: 600 }}>
                  Newsletter
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                  Stay updated with our latest posts
                </Typography>
                <TextField
                  fullWidth
                  label="Your Email"
                  variant="outlined"
                  size="small"
                  sx={{ mb: 2 }}
                />
                <Button
                  fullWidth
                  variant="contained"
                  color="primary"
                >
                  Subscribe
                </Button>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default BlogPostPage;