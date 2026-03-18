import React from 'react';
import { motion } from 'framer-motion';
import { Rocket, BarChart2, Globe, Mail } from 'lucide-react';

const Hero = () => {
  return (
    <section className="pt-32 pb-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-blue-50/50 to-white overflow-hidden">
      <div className="max-w-7xl mx-auto text-center relative">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <span className="inline-block px-4 py-1.5 mb-6 text-sm font-semibold tracking-wide text-blue-600 uppercase bg-blue-100/50 rounded-full border border-blue-200">
            Powered by AI Marketing
          </span>
          <h1 className="text-5xl md:text-7xl font-extrabold text-gray-900 tracking-tight leading-tight mb-8">
            Scale your brand with <br />
            <span className="text-blue-600 relative inline-block">
              MarketFlow
              <svg className="absolute -bottom-2 left-0 w-full" height="8" viewBox="0 0 100 8" preserveAspectRatio="none">
                <path d="M0 7C30 7 70 1 100 1" stroke="#3b82f6" strokeWidth="2" fill="none" />
              </svg>
            </span>
          </h1>
          <p className="max-w-2xl mx-auto text-xl text-gray-600 leading-relaxed mb-10 px-4">
            The all-in-one marketing suite that combines data-driven analytics, SEO automation, and high-converting campaigns.
          </p>
          <div className="flex flex-col sm:flex-row justify-center items-center gap-4">
            <button className="w-full sm:w-auto px-8 py-4 bg-blue-600 text-white font-bold rounded-2xl hover:bg-blue-700 transition-all shadow-xl shadow-blue-200 hover:scale-105 active:scale-95">
              Start Free Trial
            </button>
            <button className="w-full sm:w-auto px-8 py-4 bg-white text-blue-600 font-bold rounded-2xl border-2 border-blue-600 hover:bg-blue-50 transition-all hover:scale-105 active:scale-95">
              Watch Demo
            </button>
          </div>
        </motion.div>

        {/* Floating elements animation */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.4, duration: 1 }}
          className="relative mt-20 max-w-5xl mx-auto"
        >
          <div className="bg-white rounded-3xl shadow-2xl border border-gray-100 overflow-hidden aspect-video relative group">
            {/* Mock Dashboard UI */}
            <div className="absolute inset-0 bg-gray-50 flex flex-col">
              <div className="h-10 bg-white border-b border-gray-200 flex items-center px-4 gap-2">
                <div className="w-3 h-3 rounded-full bg-red-400" />
                <div className="w-3 h-3 rounded-full bg-yellow-400" />
                <div className="w-3 h-3 rounded-full bg-green-400" />
              </div>
              <div className="flex-1 p-6 grid grid-cols-12 gap-6">
                <div className="col-span-3 space-y-4">
                   <div className="h-8 bg-blue-100 rounded-lg animate-pulse" />
                   <div className="h-8 bg-gray-100 rounded-lg" />
                   <div className="h-8 bg-gray-100 rounded-lg" />
                   <div className="h-8 bg-gray-100 rounded-lg" />
                </div>
                <div className="col-span-9 grid grid-cols-3 gap-4">
                  <div className="h-32 bg-white rounded-xl shadow-sm border border-gray-100 p-4">
                     <div className="w-8 h-8 rounded-full bg-blue-50 mb-2 flex items-center justify-center text-blue-600"><BarChart2 size={16}/></div>
                     <div className="h-4 w-16 bg-gray-100 rounded mb-2" />
                     <div className="h-6 w-24 bg-gray-200 rounded" />
                  </div>
                  <div className="h-32 bg-white rounded-xl shadow-sm border border-gray-100 p-4">
                     <div className="w-8 h-8 rounded-full bg-green-50 mb-2 flex items-center justify-center text-green-600"><Globe size={16}/></div>
                     <div className="h-4 w-16 bg-gray-100 rounded mb-2" />
                     <div className="h-6 w-24 bg-gray-200 rounded" />
                  </div>
                  <div className="h-32 bg-white rounded-xl shadow-sm border border-gray-100 p-4">
                     <div className="w-8 h-8 rounded-full bg-purple-50 mb-2 flex items-center justify-center text-purple-600"><Mail size={16}/></div>
                     <div className="h-4 w-16 bg-gray-100 rounded mb-2" />
                     <div className="h-6 w-24 bg-gray-200 rounded" />
                  </div>
                  <div className="col-span-3 h-48 bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex flex-col justify-end gap-2 overflow-hidden">
                     <div className="flex items-end gap-2 h-full">
                        <div className="flex-1 bg-blue-200 rounded-t h-1/4 animate-bounce" />
                        <div className="flex-1 bg-blue-400 rounded-t h-2/4 animate-bounce [animation-delay:0.1s]" />
                        <div className="flex-1 bg-blue-600 rounded-t h-4/4 animate-bounce [animation-delay:0.2s]" />
                        <div className="flex-1 bg-blue-300 rounded-t h-3/4 animate-bounce [animation-delay:0.3s]" />
                        <div className="flex-1 bg-blue-500 rounded-t h-2/4 animate-bounce [animation-delay:0.4s]" />
                     </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="absolute inset-0 bg-blue-600/5 group-hover:bg-transparent transition-colors duration-500 pointer-events-none" />
          </div>

          {/* Abstract floating circles */}
          <div className="absolute -z-10 -top-10 -left-10 w-40 h-40 bg-blue-200/30 rounded-full blur-3xl animate-pulse" />
          <div className="absolute -z-10 -bottom-20 -right-20 w-60 h-60 bg-indigo-200/30 rounded-full blur-3xl animate-pulse [animation-delay:1s]" />
        </motion.div>
      </div>
    </section>
  );
};

export default Hero;
