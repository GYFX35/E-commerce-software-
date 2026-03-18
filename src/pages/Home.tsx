import React from 'react';
import MainLayout from '../layouts/MainLayout';
import Hero from '../components/Hero';
import Features from '../components/Features';
import ToolsPreview from '../components/ToolsPreview';

const Home = () => {
  return (
    <MainLayout>
      <Hero />
      <Features />
      <ToolsPreview />
    </MainLayout>
  );
};

export default Home;
