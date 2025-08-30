import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { skillsAPI } from '../services/api';
import EditSkillModal from '../components/EditSkillModal';
import { 
  PlusIcon, 
  MagnifyingGlassIcon,
  AcademicCapIcon,
  TagIcon,
  UserIcon,
  CalendarIcon,
  PencilIcon,
  TrashIcon,
  CheckCircleIcon
} from '@heroicons/react/24/outline';

const Skills = () => {
  const [skills, setSkills] = useState([]);
  const [mySkills, setMySkills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [editingSkill, setEditingSkill] = useState(null);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('all'); // 'all' or 'my'
  const [message, setMessage] = useState({ type: '', text: '' });
  
  const { user } = useAuth();

  useEffect(() => {
    fetchSkills();
  }, []);

  // Clear messages after 3 seconds
  useEffect(() => {
    if (message.text) {
      const timer = setTimeout(() => setMessage({ type: '', text: '' }), 3000);
      return () => clearTimeout(timer);
    }
  }, [message]);

  const fetchSkills = async () => {
    try {
      setLoading(true);
      const [allSkillsResponse, mySkillsResponse] = await Promise.all([
        skillsAPI.getAll(),
        skillsAPI.getMySkills()
      ]);
      setSkills(allSkillsResponse.data);
      setMySkills(mySkillsResponse.data);
    } catch (error) {
      console.error('Error fetching skills:', error);
      setMessage({ type: 'error', text: 'Failed to load skills' });
    } finally {
      setLoading(false);
    }
  };

  const handleEditSkill = (skill) => {
    setEditingSkill(skill);
    setIsEditModalOpen(true);
  };

  const handleSaveSkill = async (skillId, updatedData) => {
    try {
      await skillsAPI.update(skillId, updatedData);
      // Refresh the skills list
      await fetchSkills();
      setMessage({ type: 'success', text: 'Skill updated successfully!' });
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to update skill');
    }
  };

  const handleDeleteSkill = async (skillId) => {
    try {
      await skillsAPI.delete(skillId);
      // Refresh the skills list
      await fetchSkills();
      setMessage({ type: 'success', text: 'Skill deleted successfully!' });
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to delete skill');
    }
  };

  const closeEditModal = () => {
    setIsEditModalOpen(false);
    setEditingSkill(null);
  };

  // Get the skills to display based on active tab
  const getDisplaySkills = () => {
    const skillsToFilter = activeTab === 'all' ? skills : mySkills;
    
    return skillsToFilter.filter(skill => {
      const matchesSearch = skill.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           skill.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           skill.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase()));
      
      const matchesDifficulty = difficultyFilter === 'all' || skill.difficulty === difficultyFilter;
      
      return matchesSearch && matchesDifficulty;
    });
  };

  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'beginner':
        return 'bg-green-100 text-green-800';
      case 'intermediate':
        return 'bg-yellow-100 text-yellow-800';
      case 'advanced':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const isOwner = (skill) => {
    return user && skill.owner_id === user.id;
  };

  const displaySkills = getDisplaySkills();

  if (loading) {
    return (
      <div className="flex items-center justify-center py-16">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Skills</h1>
          <p className="text-gray-600">Discover skills you can learn from peers</p>
        </div>
        <Link 
          to="/add-skill" 
          className="btn-primary inline-flex items-center space-x-2 mt-4 sm:mt-0"
        >
          <PlusIcon className="h-5 w-5" />
          <span>Add Skill</span>
        </Link>
      </div>

      {/* Message Display */}
      {message.text && (
        <div className={`mb-6 p-4 rounded-lg flex items-center space-x-2 ${
          message.type === 'success' 
            ? 'bg-green-50 border border-green-200 text-green-700' 
            : 'bg-red-50 border border-red-200 text-red-700'
        }`}>
          {message.type === 'success' ? (
            <CheckCircleIcon className="h-5 w-5 text-green-500" />
          ) : (
            <AcademicCapIcon className="h-5 w-5 text-red-500" />
          )}
          <span>{message.text}</span>
        </div>
      )}

      {/* Tabs */}
      <div className="border-b border-gray-200 mb-6">
        <nav className="-mb-px flex space-x-8">
          <button
            onClick={() => setActiveTab('all')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'all'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            All Skills ({skills.length})
          </button>
          <button
            onClick={() => setActiveTab('my')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'my'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            My Skills ({mySkills.length})
          </button>
        </nav>
      </div>

      {/* Search and Filters */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
        <div className="flex flex-col md:flex-row gap-4">
          {/* Search */}
          <div className="flex-1 relative">
            <MagnifyingGlassIcon className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
            <input
              type="text"
              placeholder="Search skills, descriptions, or tags..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            />
          </div>
          
          {/* Difficulty Filter */}
          <div className="md:w-48">
            <select
              value={difficultyFilter}
              onChange={(e) => setDifficultyFilter(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            >
              <option value="all">All Difficulties</option>
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
        </div>
      </div>

      {/* Skills Grid */}
      {displaySkills.length === 0 ? (
        <div className="text-center py-16">
          <AcademicCapIcon className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No skills found</h3>
          <p className="text-gray-600 mb-6">
            {searchTerm || difficultyFilter !== 'all' 
              ? 'Try adjusting your search or filters'
              : activeTab === 'my' 
                ? "You haven't added any skills yet"
                : 'Be the first to add a skill!'
            }
          </p>
          {!searchTerm && difficultyFilter === 'all' && (
            <Link to="/add-skill" className="btn-primary">
              {activeTab === 'my' ? 'Add Your First Skill' : 'Add First Skill'}
            </Link>
          )}
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {displaySkills.map((skill) => (
            <div key={skill.id} className="card hover:shadow-lg transition-shadow duration-200">
              {/* Header with title, difficulty, and action buttons */}
              <div className="flex justify-between items-start mb-4">
                <div className="flex-1 mr-2">
                  <h3 className="text-xl font-semibold text-gray-900 line-clamp-2">
                    {skill.title}
                  </h3>
                </div>
                <div className="flex items-center space-x-2">
                  <span className={`px-2 py-1 text-xs font-medium rounded-full ${getDifficultyColor(skill.difficulty)}`}>
                    {skill.difficulty}
                  </span>
                  
                  {/* Action buttons for skill owner */}
                  {isOwner(skill) && (
                    <div className="flex space-x-1">
                      <button
                        onClick={() => handleEditSkill(skill)}
                        className="p-1 text-gray-400 hover:text-primary-600 transition-colors"
                        title="Edit skill"
                      >
                        <PencilIcon className="h-4 w-4" />
                      </button>
                    </div>
                  )}
                </div>
              </div>
              
              <p className="text-gray-600 mb-4 line-clamp-3">
                {skill.description}
              </p>
              
              {/* Tags */}
              {skill.tags.length > 0 && (
                <div className="flex flex-wrap gap-2 mb-4">
                  {skill.tags.slice(0, 3).map((tag, index) => (
                    <span 
                      key={index}
                      className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-primary-100 text-primary-800"
                    >
                      <TagIcon className="h-3 w-3 mr-1" />
                      {tag}
                    </span>
                  ))}
                  {skill.tags.length > 3 && (
                    <span className="text-xs text-gray-500">
                      +{skill.tags.length - 3} more
                    </span>
                  )}
                </div>
              )}
              
              {/* Footer */}
              <div className="flex items-center justify-between text-sm text-gray-500">
                <div className="flex items-center space-x-1">
                  <UserIcon className="h-4 w-4" />
                  <span>{isOwner(skill) ? 'You' : `Owner ID: ${skill.owner_id}`}</span>
                </div>
                <div className="flex items-center space-x-1">
                  <CalendarIcon className="h-4 w-4" />
                  <span>{new Date(skill.created_at).toLocaleDateString()}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Edit Skill Modal */}
      <EditSkillModal
        skill={editingSkill}
        isOpen={isEditModalOpen}
        onClose={closeEditModal}
        onSave={handleSaveSkill}
        onDelete={handleDeleteSkill}
      />
    </div>
  );
};

export default Skills;
