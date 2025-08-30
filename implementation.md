# SkillSwap

SkillSwap is a peer-to-peer microlearning and mentorship web application that allows users to teach or learn small skills from one another. The platform connects learners with peers who can provide guidance, tracks learning progress, and encourages sharing of interactive content.

---

## Demo

> Add your live demo link here once deployed (e.g., Netlify + Heroku)

---

## Features

**Core Features:**
- User authentication: register, login, logout, profile management
- Create, read, update, and delete skills
- Search and filter skills by category, difficulty, or tags
- Simple messaging or session booking between learners and teachers
- Track lessons or micro-quiz completion (optional)

**Frontend:**
- Responsive React-based UI
- Interactive skill cards and modals
- Animations for onboarding and skill selection

**Backend:**
- FastAPI backend with Python
- SQLite database for users, skills, messages
- REST API endpoints for full CRUD functionality

**Optional Add-ons:**
- Micro-quiz integration per skill
- Leaderboards for top teachers/learners

---

## Tech Stack

- **Frontend:** React, HTML, CSS, JavaScript
- **Backend:** Python + FastAPI
- **Database:** SQLite 
- **Deployment:** Netlify (frontend), Heroku / Render (backend)

---

## Installation

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
npm install  # or pip install -r requirements.txt for Flask
```

3. Configure environment variables: .env file with database URL, JWT secret, and API keys (if any)

4. Run locally:

```bash
# Backend
npm start  # or flask run

# Frontend
cd frontend
npm startCg
```


## Phase 1: Core Backend & Database (1–1.5 hrs)

**Tasks:**
- Set up FastAPI project with proper folder structure (`/backend/app/`).
- Create database models using SQLAlchemy:
  - **Users**: id, username, email, password hash
  - **Skills**: id, title, description, tags, owner_id
  - Optional: Messages or Bookings (skip if short on time)
- Implement **user authentication endpoints**: register, login, logout (JWT or session token).
- Implement **CRUD endpoints for Skills**: create, read, update, delete.

**Why:** Backend is the foundation; all frontend features depend on these endpoints.

---

## Phase 2: Minimal Frontend (1–1.5 hrs)

**Tasks:**
- Set up React project (create-react-app or Vite).
- Implement **user registration/login pages**.
- Implement **Skill listing page** (read all skills from backend).
- Implement **Add Skill form** (create skill through backend API).
- Optional: Skill detail modal or page.

**Why:** Shows full-stack integration (React → FastAPI → DB).

---

## Phase 3: Polishing & Interactivity (1 hr)

**Tasks:**
- Implement **search/filter** skills by title or tags.
- Make UI **mobile-responsive** (CSS or Tailwind).
- Add **UI enhancements**: skill cards, modals for forms, simple animations for adding/deleting skills.

**Why:** Demonstrates product sense and frontend polish.

---

## Phase 4: Optional Extras if Time Permits (0.5–1 hr)

**Tasks:**
- Implement **message or session booking system** (optional).
- Implement **progress tracking / micro-quiz stub** (e.g., simple checkboxes or dummy data).
- Run **full app locally with Docker Compose** (optional).