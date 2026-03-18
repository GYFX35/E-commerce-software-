import React from 'react';
import { Rocket, Twitter, Linkedin, Facebook, Github, Heart } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-gray-900 pt-20 pb-10 px-4 sm:px-6 lg:px-8 text-gray-400">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-20">
          <div className="space-y-6">
            <div className="flex items-center gap-2 text-white">
              <Rocket className="h-8 w-8 text-blue-500" />
              <span className="text-2xl font-bold tracking-tight">MarketFlow</span>
            </div>
            <p className="text-gray-400 max-w-xs">
              The only platform that helps you automate, analyze, and optimize your entire marketing funnel from one central hub.
            </p>
            <div className="flex gap-4">
              <a href="#" className="p-2 bg-gray-800 rounded-lg hover:text-white hover:bg-gray-700 transition-all"><Twitter size={20}/></a>
              <a href="#" className="p-2 bg-gray-800 rounded-lg hover:text-white hover:bg-gray-700 transition-all"><Linkedin size={20}/></a>
              <a href="#" className="p-2 bg-gray-800 rounded-lg hover:text-white hover:bg-gray-700 transition-all"><Facebook size={20}/></a>
              <a href="#" className="p-2 bg-gray-800 rounded-lg hover:text-white hover:bg-gray-700 transition-all"><Github size={20}/></a>
            </div>
          </div>

          <div>
            <h4 className="text-white font-bold mb-6">Product</h4>
            <ul className="space-y-4">
              <li><a href="#" className="hover:text-white transition-colors">Analytics</a></li>
              <li><a href="#" className="hover:text-white transition-colors">SEO Optimizer</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Social Management</a></li>
              <li><a href="#" className="hover:text-white transition-colors">CRM Integrations</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-white font-bold mb-6">Company</h4>
            <ul className="space-y-4">
              <li><a href="#" className="hover:text-white transition-colors">About Us</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Our Team</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Careers</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Press Kit</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-white font-bold mb-6">Legal</h4>
            <ul className="space-y-4">
              <li><a href="#" className="hover:text-white transition-colors">Privacy Policy</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Terms of Service</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Cookie Policy</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Security</a></li>
            </ul>
          </div>
        </div>

        <div className="pt-8 border-t border-gray-800 flex flex-col md:flex-row justify-between items-center gap-4 text-sm">
          <p>© 2024 MarketFlow Inc. All rights reserved.</p>
          <p className="flex items-center gap-1">Made with <Heart size={14} className="text-red-500 fill-red-500"/> for marketers everywhere.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
