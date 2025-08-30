# SkillSwap Frontend

This is the React frontend for the SkillSwap application, a peer-to-peer microlearning and mentorship platform.

## Features

- **User Authentication**: Registration, login, and logout
- **Skills Management**: Browse, search, and create skills
- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Built with Tailwind CSS and Heroicons
- **Real-time Search**: Search skills by title, description, or tags
- **Filtering**: Filter skills by difficulty level

## Tech Stack

- **React 18** - Modern React with hooks
- **Vite** - Fast build tool and dev server
- **React Router** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Heroicons** - Beautiful SVG icons
- **Axios** - HTTP client for API calls

## Getting Started

### Prerequisites

- Node.js 16+ and npm
- Backend server running (see backend README)

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── Navbar.jsx      # Navigation bar
│   └── LoadingSpinner.jsx
├── contexts/           # React contexts
│   └── AuthContext.jsx # Authentication state
├── pages/              # Page components
│   ├── Home.jsx        # Landing page
│   ├── Login.jsx       # User login
│   ├── Register.jsx    # User registration
│   ├── Skills.jsx      # Skills listing
│   └── AddSkill.jsx    # Create new skill
├── services/           # API services
│   └── api.js         # HTTP client and API calls
├── App.jsx             # Main app component
├── main.jsx           # App entry point
└── index.css          # Global styles
```

## API Integration

The frontend communicates with the backend through the `/api` proxy configured in `vite.config.js`. All API calls are handled in `src/services/api.js`.

### Authentication Flow

1. **Registration**: User creates account → redirected to login
2. **Login**: User authenticates → receives JWT token
3. **Protected Routes**: Token automatically included in API requests
4. **Logout**: Token removed, user redirected to home

### Skills Management

- **Browse Skills**: View all available skills with search and filtering
- **Create Skill**: Add new skills with title, description, difficulty, and tags
- **Search**: Find skills by title, description, or tags
- **Filter**: Filter by difficulty level (beginner, intermediate, advanced)

## Styling

The app uses Tailwind CSS with custom component classes defined in `src/index.css`:

- `.btn-primary` - Primary button styling
- `.btn-secondary` - Secondary button styling
- `.input-field` - Form input styling
- `.card` - Card container styling

## Responsive Design

The interface is fully responsive and works on:
- **Mobile**: Single column layout, stacked navigation
- **Tablet**: Two-column skills grid
- **Desktop**: Three-column skills grid, horizontal navigation

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Deployment

### Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory, ready for deployment to any static hosting service.

### Environment Variables

No environment variables are needed for the frontend as it uses the proxy configuration in `vite.config.js`.

## Contributing

1. Follow the existing code style
2. Use functional components with hooks
3. Implement responsive design
4. Add proper error handling
5. Test on multiple screen sizes

## Next Steps

This completes Phase 2 of the SkillSwap application. Future enhancements could include:

- **Skill Details**: Individual skill pages with more information
- **User Profiles**: Detailed user profiles and skill history
- **Messaging**: Communication between learners and teachers
- **Progress Tracking**: Learning progress and achievements
- **Notifications**: Real-time updates and alerts
