import React from 'react';
import { Menu, X, Rocket, BarChart2, Globe, Mail } from 'lucide-react';

const Navbar = () => {
  const [isOpen, setIsOpen] = React.useState(false);

  return (
    <nav className="fixed w-full bg-white/80 backdrop-blur-md z-50 border-b border-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <div className="flex items-center gap-2">
            <Rocket className="h-8 w-8 text-blue-600" />
            <span className="text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              MarketFlow
            </span>
          </div>

          <div className="hidden md:flex items-center space-x-8">
            <a href="#features" className="text-gray-600 hover:text-blue-600 transition-colors">Features</a>
            <a href="#tools" className="text-gray-600 hover:text-blue-600 transition-colors">Tools</a>
            <a href="#pricing" className="text-gray-600 hover:text-blue-600 transition-colors">Pricing</a>
            <button className="bg-blue-600 text-white px-5 py-2 rounded-full font-medium hover:bg-blue-700 transition-all shadow-lg shadow-blue-200">
              Get Started
            </button>
          </div>

          <div className="md:hidden flex items-center">
            <button onClick={() => setIsOpen(!isOpen)} className="text-gray-600">
              {isOpen ? <X /> : <Menu />}
            </button>
          </div>
        </div>
      </div>

      {isOpen && (
        <div className="md:hidden bg-white border-b border-gray-100 py-4 px-4 space-y-4">
          <a href="#features" className="block text-gray-600 font-medium">Features</a>
          <a href="#tools" className="block text-gray-600 font-medium">Tools</a>
          <a href="#pricing" className="block text-gray-600 font-medium">Pricing</a>
          <button className="w-full bg-blue-600 text-white px-5 py-2 rounded-xl font-medium">
            Get Started
          </button>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
