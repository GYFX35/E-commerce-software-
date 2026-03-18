import React from 'react';
import { motion } from 'framer-motion';
import {
  BarChart,
  Search,
  Send,
  CheckCircle,
  TrendingUp,
  Globe,
  ArrowUpRight,
  Target,
  FileSearch,
  Users
} from 'lucide-react';

const ToolsPreview = () => {
  return (
    <section id="tools" className="py-24 px-4 sm:px-6 lg:px-8 bg-gray-50 overflow-hidden">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="text-sm font-bold tracking-widest text-blue-600 uppercase mb-4 block">
            The MarketFlow Toolkit
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold text-gray-900 mb-6">
            Everything your marketing <br className="hidden md:block" /> team <span className="text-blue-600">needs to succeed</span>
          </h2>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          {/* Tool 1: Analytics Dashboard */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="space-y-8"
          >
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-100 text-blue-600 text-xs font-bold uppercase">
               <TrendingUp size={14}/> Analytics
            </div>
            <h3 className="text-3xl font-extrabold text-gray-900">Advanced Analytics Dashboard</h3>
            <p className="text-lg text-gray-600 leading-relaxed">
              Understand every touchpoint of your customer journey with deep-dive analytics.
              Our AI automatically identifies your best-performing channels and segments.
            </p>
            <ul className="space-y-4">
              {["Custom conversion tracking", "Multi-channel attribution", "Cohort analysis", "Real-time user monitoring"].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-gray-700 font-medium">
                  <CheckCircle className="text-blue-600" size={20} />
                  {item}
                </li>
              ))}
            </ul>
          </motion.div>

          <motion.div
             initial={{ opacity: 0, scale: 0.9 }}
             whileInView={{ opacity: 1, scale: 1 }}
             viewport={{ once: true }}
             className="relative"
          >
             <div className="bg-white rounded-3xl p-8 shadow-2xl border border-gray-100">
                <div className="flex items-center justify-between mb-8">
                   <h4 className="font-bold text-gray-900">Weekly Performance</h4>
                   <div className="px-3 py-1 bg-green-100 text-green-700 rounded-lg text-sm font-bold">+24.5%</div>
                </div>
                <div className="flex items-end gap-3 h-48 mb-8">
                   {[40, 70, 45, 90, 65, 80, 55].map((h, i) => (
                      <motion.div
                        key={i}
                        initial={{ height: 0 }}
                        whileInView={{ height: `${h}%` }}
                        viewport={{ once: true }}
                        transition={{ delay: i * 0.1 }}
                        className="flex-1 bg-blue-600/10 hover:bg-blue-600 transition-colors rounded-t-lg group relative cursor-pointer"
                      >
                         <div className="absolute -top-8 left-1/2 -translate-x-1/2 bg-gray-900 text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">
                           ${h * 123}
                         </div>
                      </motion.div>
                   ))}
                </div>
                <div className="grid grid-cols-2 gap-4">
                   <div className="p-4 bg-gray-50 rounded-2xl border border-gray-100">
                      <div className="text-xs text-gray-500 font-bold mb-1">VISITORS</div>
                      <div className="text-2xl font-black text-gray-900">12,408</div>
                   </div>
                   <div className="p-4 bg-gray-50 rounded-2xl border border-gray-100">
                      <div className="text-xs text-gray-500 font-bold mb-1">CONVERSIONS</div>
                      <div className="text-2xl font-black text-gray-900">1,245</div>
                   </div>
                </div>
             </div>
             {/* Floating Mini card */}
             <div className="absolute -top-6 -right-6 bg-white p-4 rounded-2xl shadow-xl border border-gray-100 hidden md:block animate-bounce [animation-duration:3s]">
                <div className="flex items-center gap-3">
                   <div className="p-2 bg-amber-100 rounded-lg"><Target className="text-amber-600" size={16}/></div>
                   <div>
                      <div className="text-[10px] font-bold text-gray-400">TARGET REACHED</div>
                      <div className="text-sm font-black text-gray-900">92% of Goal</div>
                   </div>
                </div>
             </div>
          </motion.div>
        </div>

        <div className="mt-32 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          {/* Tool 2: SEO Mock */}
          <motion.div
             initial={{ opacity: 0, scale: 0.9 }}
             whileInView={{ opacity: 1, scale: 1 }}
             viewport={{ once: true }}
             className="order-2 lg:order-1 relative"
          >
             <div className="bg-white rounded-3xl p-8 shadow-2xl border border-gray-100">
                <div className="flex items-center gap-4 mb-8">
                   <div className="flex-1 bg-gray-100 h-10 rounded-xl px-4 flex items-center gap-2">
                      <Globe size={16} className="text-gray-400"/>
                      <span className="text-sm text-gray-500 font-medium">marketflow.com</span>
                   </div>
                   <button className="bg-blue-600 text-white px-4 py-2 rounded-xl text-sm font-bold">Analyze</button>
                </div>
                <div className="space-y-6">
                   {[
                     { label: "SEO Health", val: "94/100", color: "text-green-600", bg: "bg-green-100" },
                     { label: "Top Keyword", val: "Marketing Suite", color: "text-blue-600", bg: "bg-blue-100" },
                     { label: "Backlinks", val: "24.2k", color: "text-purple-600", bg: "bg-purple-100" }
                   ].map((item, i) => (
                      <div key={i} className="flex items-center justify-between p-4 bg-gray-50 rounded-2xl border border-gray-100">
                         <div className="flex items-center gap-3">
                            <div className={`p-2 ${item.bg} ${item.color} rounded-lg`}><CheckCircle size={16}/></div>
                            <span className="font-bold text-gray-700">{item.label}</span>
                         </div>
                         <span className={`font-black ${item.color}`}>{item.val}</span>
                      </div>
                   ))}
                </div>
             </div>
             {/* Decorative element */}
             <div className="absolute -bottom-8 -left-8 w-24 h-24 bg-blue-600/10 rounded-full blur-2xl" />
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="order-1 lg:order-2 space-y-8"
          >
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-green-100 text-green-600 text-xs font-bold uppercase">
               <FileSearch size={14}/> SEO & Content
            </div>
            <h3 className="text-3xl font-extrabold text-gray-900">Master Search Results</h3>
            <p className="text-lg text-gray-600 leading-relaxed">
              Don't leave your ranking to chance. Our SEO engine analyzes top competitors and tells you exactly what content to create to outrank them.
            </p>
            <ul className="space-y-4">
              {["Competitor keyword gaps", "On-page optimization tips", "Automated rank tracking", "Link building opportunities"].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-gray-700 font-medium">
                  <CheckCircle className="text-green-600" size={20} />
                  {item}
                </li>
              ))}
            </ul>
            <button className="flex items-center gap-2 text-blue-600 font-extrabold text-lg hover:gap-4 transition-all">
              Try SEO Tools <ArrowUpRight size={20}/>
            </button>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default ToolsPreview;
