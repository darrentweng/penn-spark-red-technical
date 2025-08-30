# SkillSwap Backend

This is the FastAPI backend for the SkillSwap application, a peer-to-peer microlearning and mentorship platform.

## Features

- **User Authentication**: JWT-based authentication with user registration and login
- **Skills Management**: Full CRUD operations for skills with tagging system
- **User Management**: User profiles and management
- **Database**: PostgreSQL with SQLAlchemy ORM
- **API Documentation**: Automatic OpenAPI/Swagger documentation

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Installation

1. **Clone the repository and navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your database credentials and JWT secret
   ```

5. **Set up PostgreSQL database:**
   - Create a database named `skillswap_db`
   - Update the `DATABASE_URL` in your `.env` file

6. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

### Running the Application

**Development mode:**
```bash
python run.py
```

**Production mode:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`
- **OpenAPI schema**: `http://localhost:8000/openapi.json`

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user info

### Skills
- `GET /skills/` - List all skills
- `POST /skills/` - Create a new skill
- `GET /skills/{skill_id}` - Get a specific skill
- `PUT /skills/{skill_id}` - Update a skill
- `DELETE /skills/{skill_id}` - Delete a skill
- `GET /skills/my-skills/` - Get current user's skills

### Users
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get a specific user
- `GET /users/profile/me` - Get current user's profile

## Database Models

- **User**: id, username, email, password_hash, created_at, updated_at
- **Skill**: id, title, description, difficulty, owner_id, created_at, updated_at
- **Tag**: id, name
- **Message**: id, sender_id, receiver_id, content, created_at

## Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Database Migrations
```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

### Code Formatting
```bash
# Install formatting tools
pip install black isort

# Format code
black .
isort .
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://username:password@localhost:5432/skillswap_db` |
| `SECRET_KEY` | JWT secret key | `your-secret-key-here` |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration time | `30` |
| `DEBUG` | Debug mode | `True` |

## Security Features

- Password hashing with bcrypt
- JWT token authentication
- CORS middleware configuration
- Input validation with Pydantic schemas
- SQL injection protection with SQLAlchemy ORM

