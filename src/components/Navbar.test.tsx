import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import Navbar from '../components/Navbar';

describe('Navbar', () => {
  it('renders the brand name', () => {
    render(<Navbar />);
    expect(screen.getByText('MarketFlow')).toBeInTheDocument();
  });

  it('renders navigation links', () => {
    render(<Navbar />);
    expect(screen.getByText('Features')).toBeInTheDocument();
    expect(screen.getByText('Tools')).toBeInTheDocument();
    expect(screen.getByText('Pricing')).toBeInTheDocument();
  });
});
