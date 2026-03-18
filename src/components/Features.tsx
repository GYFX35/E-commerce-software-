import React from 'react';
import { motion } from 'framer-motion';
import {
  BarChart3,
  Search,
  Mail,
  Zap,
  Users,
  ShieldCheck,
  ArrowRight
} from 'lucide-react';

const Features = () => {
  const features = [
    {
      title: "Real-time Analytics",
      description: "Get detailed insights into your customer behavior with our intuitive analytics dashboard. Track conversions as they happen.",
      icon: <BarChart3 className="text-blue-600" />,
      colorClass: "bg-blue-50"
    },
    {
      title: "SEO Optimization",
      description: "Improve your search engine rankings with automated keyword research and page performance auditing tools.",
      icon: <Search className="text-green-600" />,
      colorClass: "bg-green-50"
    },
    {
      title: "Campaign Management",
      description: "Manage multiple marketing campaigns across all platforms from a single, unified interface. Stay organized and efficient.",
      icon: <Mail className="text-purple-600" />,
      colorClass: "bg-purple-50"
    },
    {
      title: "Social Automation",
      description: "Schedule posts, track engagement, and automate your social media presence to reach your audience effectively.",
      icon: <Zap className="text-amber-600" />,
      colorClass: "bg-amber-50"
    },
    {
      title: "Customer CRM",
      description: "Build lasting relationships with a integrated CRM that tracks every interaction and optimizes your sales funnel.",
      icon: <Users className="text-rose-600" />,
      colorClass: "bg-rose-50"
    },
    {
      title: "Secure & Scalable",
      description: "Enterprise-grade security and a platform that grows with your business. We handle the infrastructure so you can focus on growth.",
      icon: <ShieldCheck className="text-indigo-600" />,
      colorClass: "bg-indigo-50"
    }
  ];

  return (
    <section id="features" className="py-24 px-4 sm:px-6 lg:px-8 bg-white relative overflow-hidden">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-20">
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 mb-6">
            Everything you need to <span className="text-blue-600">grow faster</span>
          </h2>
          <p className="max-w-2xl mx-auto text-lg text-gray-600">
            Powerful marketing tools designed to give you a competitive edge. Built by marketers, for marketers.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative z-10">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              whileHover={{ y: -10 }}
              transition={{ type: "spring", stiffness: 300 }}
              className="p-8 bg-white rounded-3xl border border-gray-100 shadow-xl shadow-gray-200/50 flex flex-col items-start gap-4 group hover:border-blue-100 transition-colors"
            >
              <div className={`p-4 rounded-2xl ${feature.colorClass} flex items-center justify-center group-hover:scale-110 transition-transform`}>
                {feature.icon}
              </div>
              <h3 className="text-xl font-bold text-gray-900">{feature.title}</h3>
              <p className="text-gray-600 leading-relaxed mb-4">{feature.description}</p>
              <a href="#" className="mt-auto flex items-center gap-2 text-blue-600 font-semibold hover:gap-3 transition-all">
                Learn more <ArrowRight size={18} />
              </a>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
