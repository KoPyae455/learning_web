import React from 'react';
import Navbar from './Navbar';
import { Container, Box } from '@mui/material';
import Footer from './Footer';

const PageLayout = ({ children }) => {
  return (
    <Box sx={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Container maxWidth="lg" sx={{ flex: 1, py: 4 }}>
        {children}
      </Container>
      <Footer />
    </Box>
  );
};

export default PageLayout;
