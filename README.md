# SkillSwap

SkillSwap is a peer-to-peer microlearning and mentorship web application that allows users to teach or learn small skills from one another. The platform connects learners with peers who can provide guidance, tracks learning progress, and encourages sharing of interactive content.

---

## Features

**Implemented Features:**
- User authentication: register, login, logout, profile management
- Create, read, update, and delete skills
- Search and filter skills by category, difficulty, or tags
- Responsive React-based UI
- Interactive skill cards and modals
- FastAPI backend with Python
- SQLite database for users and skills
- REST API endpoints for full CRUD functionality

**What's Next:**
- Simple messaging between learners and teachers
- Session booking system
- Track lessons and learning progress
- Micro-quiz integration per skill
- Animations for onboarding and skill selection
- Leaderboards for top teachers/learners

---

## Tech Stack

- **Frontend:** React, HTML, CSS, JavaScript
- **Backend:** Python + FastAPI
- **Database:** SQLite 

---

## Time spent
I spent 5 active hours on the application developing the core features. In that time, I was unable to deploy the application to netlify/heroku, so I included installation instructions below.

## Installation

### Prerequisites
- Python 3.8+ 
- Node.js 16+ and npm
- Git

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/skillswap.git
cd skillswap
```

2. Install dependencies:

```bash
# Frontend
cd frontend
npm install

# Backend
cd ../backend
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
# Copy the example environment file
cd backend
cp env.example .env
```

Edit the `.env` file and set:
- `DATABASE_URL`: Database connection string (default: `sqlite:///./skillswap.db`)
- `SECRET_KEY`: A secure random string for JWT tokens
- `ALGORITHM`: JWT algorithm (default: `HS256`)



4. Run the application:

```bash
# Terminal 1 - Backend (runs on http://localhost:8000)
cd backend
python run.py

# Terminal 2 - Frontend (runs on http://localhost:5173)
cd frontend
npm run dev
```

5. Verify installation:
- Backend API: Visit http://localhost:8000/docs for the interactive API documentation
- Frontend: Visit http://localhost:5173 in your browser
- Database: Check that `skillswap.db` file was created in the backend directory