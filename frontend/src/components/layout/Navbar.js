import React, { useState } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  IconButton,
  Box,
  Menu,
  MenuItem,
  Avatar,
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import {
  Menu as MenuIcon,
  School as SchoolIcon,
  Article as ArticleIcon,
  Person as PersonIcon,
  Dashboard as DashboardIcon,
  Logout as LogoutIcon,
  Settings as SettingsIcon,
} from '@mui/icons-material';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';

const Navbar = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const [mobileOpen, setMobileOpen] = useState(false);
  const [anchorEl, setAnchorEl] = useState(null);

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleProfileMenuClose = () => {
    setAnchorEl(null);
  };

  const handleMobileDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const handleLogout = async () => {
    await logout();
    handleProfileMenuClose();
    navigate('/');
  };

  const handleNavigation = (path) => {
    navigate(path);
    setMobileOpen(false);
  };

  const isActive = (path) => {
    return location.pathname === path;
  };

  const navItems = [
    { text: 'Home', path: '/', icon: null },
    { text: 'Courses', path: '/courses', icon: <SchoolIcon /> },
    { text: 'Blog', path: '/blog', icon: <ArticleIcon /> },
  ];

  const userMenuItems = [
    { text: 'Profile', path: '/profile', icon: <PersonIcon /> },
    { text: 'Dashboard', path: '/dashboard', icon: <DashboardIcon /> },
    { text: 'Settings', path: '/settings', icon: <SettingsIcon /> },
  ];

  const drawer = (
    <Box>
      <Box sx={{ p: 2, textAlign: 'center' }}>
        <Typography variant="h6" color="primary">
          Learning Platform
        </Typography>
      </Box>
      <Divider />
      <List>
        {navItems.map((item) => (
          <ListItem
            key={item.text}
            button
            onClick={() => handleNavigation(item.path)}
            selected={isActive(item.path)}
            sx={{
              '&.Mui-selected': {
                backgroundColor: 'primary.light',
                color: 'primary.contrastText',
                '&:hover': {
                  backgroundColor: 'primary.main',
                },
              },
            }}
          >
            {item.icon && <ListItemIcon sx={{ color: 'inherit' }}>{item.icon}</ListItemIcon>}
            <ListItemText primary={item.text} />
          </ListItem>
        ))}
        <Divider />
        {isAuthenticated ? (
          <>
            {userMenuItems.map((item) => (
              <ListItem
                key={item.text}
                button
                onClick={() => handleNavigation(item.path)}
                selected={isActive(item.path)}
              >
                <ListItemIcon>{item.icon}</ListItemIcon>
                <ListItemText primary={item.text} />
              </ListItem>
            ))}
            <ListItem button onClick={handleLogout}>
              <ListItemIcon>
                <LogoutIcon />
              </ListItemIcon>
              <ListItemText primary="Logout" />
            </ListItem>
          </>
        ) : (
          <>
            <ListItem button onClick={() => handleNavigation('/login')}>
              <ListItemText primary="Login" />
            </ListItem>
            <ListItem button onClick={() => handleNavigation('/register')}>
              <ListItemText primary="Register" />
            </ListItem>
          </>
        )}
      </List>
    </Box>
  );

  return (
    <>
      <AppBar position="sticky" elevation={1}>
        <Toolbar>
          {isMobile && (
            <IconButton
              color="inherit"
              aria-label="open drawer"
              edge="start"
              onClick={handleMobileDrawerToggle}
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton>
          )}

          <Typography
            variant="h6"
            component={Link}
            to="/"
            sx={{
              flexGrow: 1,
              textDecoration: 'none',
              color: 'inherit',
              fontWeight: 700,
            }}
          >
            Learning Platform
          </Typography>

          {!isMobile && (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
              {navItems.map((item) => (
                <Button
                  key={item.text}
                  color="inherit"
                  component={Link}
                  to={item.path}
                  sx={{
                    textTransform: 'none',
                    fontWeight: isActive(item.path) ? 600 : 400,
                    borderBottom: isActive(item.path) ? '2px solid' : 'none',
                    borderColor: 'inherit',
                  }}
                >
                  {item.text}
                </Button>
              ))}

              {isAuthenticated ? (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <IconButton
                    onClick={handleProfileMenuOpen}
                    sx={{ p: 0 }}
                  >
                    <Avatar
                      alt={user?.full_name || user?.username}
                      src={user?.avatar}
                      sx={{ width: 32, height: 32 }}
                    >
                      {user?.full_name?.charAt(0) || user?.username?.charAt(0)}
                    </Avatar>
                  </IconButton>
                </Box>
              ) : (
                <Box sx={{ display: 'flex', gap: 1 }}>
                  <Button
                    color="inherit"
                    component={Link}
                    to="/login"
                    sx={{ textTransform: 'none' }}
                  >
                    Login
                  </Button>
                  <Button
                    variant="contained"
                    color="secondary"
                    component={Link}
                    to="/register"
                    sx={{ textTransform: 'none' }}
                  >
                    Register
                  </Button>
                </Box>
              )}
            </Box>
          )}
        </Toolbar>
      </AppBar>

      {/* Mobile Drawer */}
      <Drawer
        variant="temporary"
        open={mobileOpen}
        onClose={handleMobileDrawerToggle}
        ModalProps={{
          keepMounted: true, // Better open performance on mobile.
        }}
        sx={{
          display: { xs: 'block', md: 'none' },
          '& .MuiDrawer-paper': { boxSizing: 'border-box', width: 280 },
        }}
      >
        {drawer}
      </Drawer>

      {/* Profile Menu */}
      <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={handleProfileMenuClose}
        onClick={handleProfileMenuClose}
        PaperProps={{
          elevation: 0,
          sx: {
            overflow: 'visible',
            filter: 'drop-shadow(0px 2px 8px rgba(0,0,0,0.32))',
            mt: 1.5,
            '& .MuiAvatar-root': {
              width: 32,
              height: 32,
              ml: -0.5,
              mr: 1,
            },
          },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        <MenuItem onClick={() => handleNavigation('/profile')}>
          <Avatar /> Profile
        </MenuItem>
        <MenuItem onClick={() => handleNavigation('/dashboard')}>
          <DashboardIcon /> Dashboard
        </MenuItem>
        <Divider />
        <MenuItem onClick={handleLogout}>
          <LogoutIcon /> Logout
        </MenuItem>
      </Menu>
    </>
  );
};

export default Navbar;
