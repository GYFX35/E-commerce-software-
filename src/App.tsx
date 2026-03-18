import React from 'react';
import { HelmetProvider, Helmet } from 'react-helmet-async';
import Home from './pages/Home';

function App() {
  return (
    <HelmetProvider>
      <div className="font-sans antialiased text-gray-900">
        <Helmet>
          <title>MarketFlow | All-in-One AI Marketing Toolkit</title>
          <meta name="description" content="Scale your brand with MarketFlow. The ultimate suite of marketing tools for analytics, SEO, and social automation." />
          <meta name="keywords" content="marketing tools, SEO optimization, real-time analytics, social automation, marketflow" />
          <meta property="og:title" content="MarketFlow | Scale Your Brand" />
          <meta property="og:description" content="AI-driven marketing suite for modern growth teams." />
          <meta property="og:type" content="website" />
          <meta name="twitter:card" content="summary_large_image" />
          <meta name="twitter:title" content="MarketFlow | AI Marketing Toolkit" />
          <meta name="twitter:description" content="Scale your brand with modern analytics and automation tools." />
          <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
        </Helmet>
        <Home />
      </div>
    </HelmetProvider>
  );
}

export default App;
