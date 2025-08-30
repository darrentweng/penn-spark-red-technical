import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { 
  AcademicCapIcon, 
  UserGroupIcon, 
  LightBulbIcon,
  ArrowRightIcon 
} from '@heroicons/react/24/outline';

const Home = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="max-w-6xl mx-auto">
      {/* Hero Section */}
      <div className="text-center py-16">
        <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
          Learn Skills from
          <span className="text-primary-600"> Peers</span>
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
          SkillSwap connects learners with peers who can teach small skills. 
          Share your knowledge, learn from others, and grow together.
        </p>
        
        {isAuthenticated ? (
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/skills" className="btn-primary text-lg px-8 py-3">
              Browse Skills
            </Link>
            <Link to="/add-skill" className="btn-secondary text-lg px-8 py-3">
              Share a Skill
            </Link>
          </div>
        ) : (
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/register" className="btn-primary text-lg px-8 py-3">
              Get Started
            </Link>
            <Link to="/login" className="btn-secondary text-lg px-8 py-3">
              Sign In
            </Link>
          </div>
        )}
      </div>

      {/* Features Section */}
      <div className="grid md:grid-cols-3 gap-8 py-16">
        <div className="text-center">
          <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <AcademicCapIcon className="h-8 w-8 text-primary-600" />
          </div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Learn Skills</h3>
          <p className="text-gray-600">
            Discover skills from programming to cooking, taught by real people who know them best.
          </p>
        </div>
        
        <div className="text-center">
          <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <UserGroupIcon className="h-8 w-8 text-primary-600" />
          </div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Connect with Peers</h3>
          <p className="text-gray-600">
            Build relationships with fellow learners and teachers in your community.
          </p>
        </div>
        
        <div className="text-center">
          <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <LightBulbIcon className="h-8 w-8 text-primary-600" />
          </div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Share Knowledge</h3>
          <p className="text-gray-600">
            Teach others what you know and contribute to the learning community.
          </p>
        </div>
      </div>

      {/* CTA Section */}
      {!isAuthenticated && (
        <div className="bg-primary-50 rounded-2xl p-8 text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            Ready to start learning?
          </h2>
          <p className="text-gray-600 mb-6">
            Join thousands of learners and teachers on SkillSwap today.
          </p>
          <Link 
            to="/register" 
            className="inline-flex items-center space-x-2 btn-primary text-lg px-8 py-3"
          >
            <span>Create Account</span>
            <ArrowRightIcon className="h-5 w-5" />
          </Link>
        </div>
      )}
    </div>
  );
};

export default Home;
