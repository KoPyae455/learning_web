import React, { useState } from 'react';
import {
  Box,
  Container,
  Typography,
  Button,
  TextField,
  Link,
  Divider,
  Stack,
  IconButton,
  InputAdornment,
  useTheme,
  //useMediaQuery,
  CircularProgress,
  Grid,
  Checkbox,
  FormControlLabel,
} from '@mui/material';
import {
  Email as EmailIcon,
  Lock as LockIcon,
  Visibility as VisibilityIcon,
  VisibilityOff as VisibilityOffIcon,
  Person as PersonIcon,
} from '@mui/icons-material';
import { Link as RouterLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

// Social Media Icons
import GoogleIcon from '@mui/icons-material/Google';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import LinkedInIcon from '@mui/icons-material/LinkedIn';

const RegisterPage = () => {
  const theme = useTheme();
  //const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const { register } = useAuth();
  const navigate = useNavigate();

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [acceptedTerms, setAcceptedTerms] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (password !== confirmPassword) {
      return setError("Passwords don't match");
    }

    try {
      setError('');
      setLoading(true);
      await register(name, email, password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Failed to create an account');
      console.error(err);
    }
    setLoading(false);
  };

  const handleSocialRegister = (provider) => {
    // Implement social register functionality here
    console.log(`Registering with ${provider}`);
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
        backgroundColor: theme.palette.background.default,
      }}
    >
      {/* Main Content */}
      <Container
        maxWidth="sm"
        sx={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          py: 8,
        }}
      >
        <Box
          sx={{
            backgroundColor: theme.palette.background.paper,
            borderRadius: 4,
            boxShadow: theme.shadows[3],
            p: 4,
          }}
        >
          {/* Header */}
          <Box sx={{ textAlign: 'center', mb: 4 }}>
            <Typography variant="h4" component="h1" sx={{ fontWeight: 700, mb: 1 }}>
              Create Your Account
            </Typography>
            <Typography variant="body1" color="text.secondary">
              Join our learning community today
            </Typography>
          </Box>

          {/* Error Message */}
          {error && (
            <Box
              sx={{
                backgroundColor: theme.palette.error.light,
                color: theme.palette.error.dark,
                p: 2,
                borderRadius: 2,
                mb: 3,
              }}
            >
              <Typography variant="body2">{error}</Typography>
            </Box>
          )}

          {/* Register Form */}
          <Box component="form" onSubmit={handleSubmit} sx={{ mb: 3 }}>
            <TextField
              fullWidth
              label="Full Name"
              variant="outlined"
              margin="normal"
              required
              value={name}
              onChange={(e) => setName(e.target.value)}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <PersonIcon color="action" />
                  </InputAdornment>
                ),
              }}
            />
            <TextField
              fullWidth
              label="Email Address"
              variant="outlined"
              margin="normal"
              required
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <EmailIcon color="action" />
                  </InputAdornment>
                ),
              }}
            />
            <TextField
              fullWidth
              label="Password"
              variant="outlined"
              margin="normal"
              required
              type={showPassword ? 'text' : 'password'}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <LockIcon color="action" />
                  </InputAdornment>
                ),
                endAdornment: (
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={() => setShowPassword(!showPassword)}
                      edge="end"
                    >
                      {showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
                    </IconButton>
                  </InputAdornment>
                ),
              }}
            />
            <TextField
              fullWidth
              label="Confirm Password"
              variant="outlined"
              margin="normal"
              required
              type={showPassword ? 'text' : 'password'}
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <LockIcon color="action" />
                  </InputAdornment>
                ),
              }}
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={acceptedTerms}
                  onChange={(e) => setAcceptedTerms(e.target.checked)}
                  color="primary"
                />
              }
              label={
                <Typography variant="body2">
                  I agree to the{' '}
                  <Link component={RouterLink} to="/terms" color="primary">
                    Terms of Service
                  </Link>{' '}
                  and{' '}
                  <Link component={RouterLink} to="/privacy" color="primary">
                    Privacy Policy
                  </Link>
                </Typography>
              }
              sx={{ mt: 2, mb: 2 }}
            />
            <Button
              fullWidth
              size="large"
              variant="contained"
              color="primary"
              type="submit"
              disabled={loading || !acceptedTerms}
              sx={{ mt: 2, py: 1.5 }}
            >
              {loading ? (
                <CircularProgress size={24} color="inherit" />
              ) : (
                'Create Account'
              )}
            </Button>
          </Box>

          {/* Divider */}
          <Divider sx={{ my: 3 }}>
            <Typography variant="body2" color="text.secondary">
              OR SIGN UP WITH
            </Typography>
          </Divider>

          {/* Social Register Buttons */}
          <Stack direction="row" spacing={2} sx={{ mb: 3, justifyContent: 'center' }}>
            <IconButton
              onClick={() => handleSocialRegister('google')}
              sx={{
                backgroundColor: '#DB4437',
                color: 'white',
                '&:hover': { backgroundColor: '#C33D2E' },
              }}
            >
              <GoogleIcon />
            </IconButton>
            <IconButton
              onClick={() => handleSocialRegister('facebook')}
              sx={{
                backgroundColor: '#4267B2',
                color: 'white',
                '&:hover': { backgroundColor: '#3B5998' },
              }}
            >
              <FacebookIcon />
            </IconButton>
            <IconButton
              onClick={() => handleSocialRegister('twitter')}
              sx={{
                backgroundColor: '#1DA1F2',
                color: 'white',
                '&:hover': { backgroundColor: '#1991DA' },
              }}
            >
              <TwitterIcon />
            </IconButton>
            <IconButton
              onClick={() => handleSocialRegister('linkedin')}
              sx={{
                backgroundColor: '#0077B5',
                color: 'white',
                '&:hover': { backgroundColor: '#00669B' },
              }}
            >
              <LinkedInIcon />
            </IconButton>
          </Stack>

          {/* Login Link */}
          <Box sx={{ textAlign: 'center', mt: 3 }}>
            <Typography variant="body2" color="text.secondary">
              Already have an account?{' '}
              <Link component={RouterLink} to="/login" color="primary">
                Sign in
              </Link>
            </Typography>
          </Box>
        </Box>
      </Container>

      {/* Footer - Same as Login Page */}
      <Box
        component="footer"
        sx={{
          py: 4,
          backgroundColor: theme.palette.background.paper,
          borderTop: `1px solid ${theme.palette.divider}`,
        }}
      >
        <Container maxWidth="lg">
          <Grid container spacing={4}>
            {/* Platform Info */}
            <Grid item xs={12} md={4}>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
                Learning Platform
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Transform your career with our comprehensive online learning platform. 
                Access experienced courses, video lessons, and stay updated with our IT blog.
              </Typography>
            </Grid>

            {/* Learning Courses */}
            <Grid item xs={6} md={2}>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
                Learning Courses
              </Typography>
              <Stack spacing={1}>
                <Link component={RouterLink} to="/blog" color="text.secondary">
                  Blog
                </Link>
                <Link component={RouterLink} to="/certificates" color="text.secondary">
                  Certificates
                </Link>
                <Link component={RouterLink} to="/instructors" color="text.secondary">
                  Instructors
                </Link>
              </Stack>
            </Grid>

            {/* Support */}
            <Grid item xs={6} md={2}>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
                Support
              </Typography>
              <Stack spacing={1}>
                <Link component={RouterLink} to="/help-center" color="text.secondary">
                  Help Center
                </Link>
                <Link component={RouterLink} to="/contact" color="text.secondary">
                  Contact Us
                </Link>
                <Link component={RouterLink} to="/faq" color="text.secondary">
                  FAQ
                </Link>
                <Link component={RouterLink} to="/community" color="text.secondary">
                  Community
                </Link>
              </Stack>
            </Grid>

            {/* Company */}
            <Grid item xs={6} md={2}>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
                Company
              </Typography>
              <Stack spacing={1}>
                <Link component={RouterLink} to="/about" color="text.secondary">
                  About Us
                </Link>
                <Link component={RouterLink} to="/careers" color="text.secondary">
                  Careers
                </Link>
                <Link component={RouterLink} to="/privacy" color="text.secondary">
                  Privacy Policy
                </Link>
                <Link component={RouterLink} to="/terms" color="text.secondary">
                  Terms of Service
                </Link>
              </Stack>
            </Grid>

            {/* Social Media */}
            <Grid item xs={6} md={2}>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
                Follow Us
              </Typography>
              <Stack direction="row" spacing={1}>
                <IconButton 
                  component="a" 
                  href="https://facebook.com" 
                  target="_blank"
                  sx={{ color: theme.palette.text.secondary }}
                >
                  <FacebookIcon />
                </IconButton>
                <IconButton 
                  component="a" 
                  href="https://twitter.com" 
                  target="_blank"
                  sx={{ color: theme.palette.text.secondary }}
                >
                  <TwitterIcon />
                </IconButton>
                <IconButton 
                  component="a" 
                  href="https://linkedin.com" 
                  target="_blank"
                  sx={{ color: theme.palette.text.secondary }}
                >
                  <LinkedInIcon />
                </IconButton>
              </Stack>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </Box>
  );
};

export default RegisterPage;