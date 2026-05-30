"# AI Reel Generator - Project Foundation (PHASE 0)

## 📋 Project Overview

**AI Reel Generator** is a local application designed to generate short-form cinematic videos from stories. This project foundation provides a robust architecture and development environment for future AI-powered features including story generation, character consistency, image generation, voice synthesis, and video rendering.

**Current Status:** Foundation Phase ✅
- ✅ Project structure initialized
- ✅ Frontend and backend scaffolding complete
- ✅ Database and cache infrastructure ready
- ✅ Docker containerization configured
- ✅ Development environment setup
- ⏳ Ready for Phase 1: Backend Core

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Client Browser                        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
        ┌──────────────────────────────────┐
        │     Next.js Frontend (3000)       │
        │  - React 19                       │
        │  - TypeScript                     │
        │  - TailwindCSS + Shadcn UI        │
        └──────────────────┬────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │  FastAPI Backend (8000)           │
        │  - Python 3.12                    │
        │  - SQLAlchemy ORM                 │
        │  - Async/Await                    │
        └──────────┬───────────────┬────────┘
                   │               │
        ┌──────────▼───┐   ┌──────▼──────────┐
        │  PostgreSQL  │   │   Redis Cache   │
        │   (5432)     │   │    (6379)       │
        └──────────────┘   └─────────────────┘
```

### Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Frontend** | Next.js | 15.0.0 |
| | React | 19.0.0 |
| | TypeScript | 5.3.3 |
| | TailwindCSS | 3.4.1 |
| **Backend** | FastAPI | 0.109.0 |
| | Python | 3.12 |
| | SQLAlchemy | 2.0.23 |
| | Alembic | 1.13.1 |
| **Database** | PostgreSQL | 16 |
| **Cache** | Redis | 7 |
| **Containerization** | Docker | Latest |
| | Docker Compose | 3.9 |

---

## 📦 Project Structure

```
ai-reel-generator/
├── frontend/                    # Next.js Frontend
│   ├── src/
│   │   ├── app/               # Next.js app directory
│   │   ├── components/        # React components
│   │   ├── hooks/             # Custom React hooks
│   │   ├── lib/               # Utility functions
│   │   ├── services/          # API services
│   │   ├── store/             # Global state management
│   │   └── types/             # TypeScript types
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── next.config.js
│   ├── .env.example
│   └── .env
│
├── backend/                     # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API routes
│   │   ├── core/              # Core configuration
│   │   ├── db/                # Database & cache
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   ├── repositories/      # Data access layer
│   │   ├── utils/             # Utility functions
│   │   ├── main.py            # FastAPI app factory
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── run.py
│   ├── .env.example
│   └── .env
│
├── docker/                      # Docker configuration
│   ├── Dockerfile.frontend
│   └── Dockerfile.backend
│
├── scripts/                     # Automation scripts
│   ├── setup.sh               # Initial setup
│   ├── start.sh               # Start services
│   ├── stop.sh                # Stop services
│   └── logs.sh                # View logs
│
├── storage/                     # Media storage
│   ├── images/
│   ├── videos/
│   ├── audio/
│   ├── subtitles/
│   └── renders/
│
├── docs/                        # Documentation
│   ├── Phase-00-Project-Foundation.md
│   ├── Phase-01-Backend-Core.md
│   ├── Phase-02-Database-Project-Management.md
│   └── ... (future phases)
│
├── docker-compose.yml          # Container orchestration
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
└── .github/                    # GitHub configuration

```

---

## 🔧 Requirements

### System Requirements
- **OS**: Windows, macOS, or Linux
- **Docker**: 20.10+
- **Docker Compose**: 1.29+
- **Git**: 2.30+
- **Disk Space**: 10GB minimum for development
- **RAM**: 8GB minimum recommended

### Local Development (without Docker)
- **Node.js**: 20.0+
- **npm** or **yarn**: Latest
- **Python**: 3.12+
- **PostgreSQL**: 14+
- **Redis**: 7+

---

## 🚀 Installation

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-reel-generator
   ```

2. **Run setup script**
   ```bash
   # On macOS/Linux
   chmod +x scripts/setup.sh
   ./scripts/setup.sh
   
   # On Windows (using Git Bash or WSL)
   bash scripts/setup.sh
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Local Development Setup

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Start development server
npm run dev
```

Frontend will be available at: http://localhost:3000

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Configure environment variables
# Edit .env with your PostgreSQL and Redis URLs

# Start backend
python run.py
```

Backend will be available at: http://localhost:8000

---

## 🐳 Docker Setup

### Start All Services

```bash
docker-compose up -d
```

### Stop All Services

```bash
docker-compose down
```

### View Service Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f postgres
docker-compose logs -f redis
```

### Environment Variables

Create `.env` files in both `frontend/` and `backend/` directories:

**frontend/.env**
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
NODE_ENV=development
```

**backend/.env**
```env
DATABASE_URL=postgresql://ai_user:ai_password@localhost:5432/ai_reel_generator
REDIS_URL=redis://localhost:6379/0
APP_NAME=AI Reel Generator
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO
HOST=0.0.0.0
PORT=8000
RELOAD=true
```

---

## 🔌 Services Configuration

### PostgreSQL
- **Container**: `ai_reel_postgres`
- **Host**: localhost
- **Port**: 5432
- **User**: ai_user
- **Password**: ai_password
- **Database**: ai_reel_generator

### Redis
- **Container**: `ai_reel_redis`
- **Host**: localhost
- **Port**: 6379
- **Connection String**: redis://localhost:6379/0

### FastAPI Backend
- **Container**: `ai_reel_backend`
- **Host**: localhost
- **Port**: 8000
- **Health Endpoint**: GET /api/v1/health

### Next.js Frontend
- **Container**: `ai_reel_frontend`
- **Host**: localhost
- **Port**: 3000

---

## 📚 Local Development

### Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Development with hot reload
npm run dev

# Type checking
npm run type-check

# Build for production
npm run build

# Start production server
npm start

# Run linter
npm run lint
```

### Backend Development

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Start development server (auto-reload enabled)
python run.py

# Run tests (future)
pytest

# Generate API documentation
# Automatically available at http://localhost:8000/docs
```

### Database Migrations (Future)

When you need to create database migrations:

```bash
cd backend

# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1
```

---

## 🔑 API Endpoints (Phase 0)

### Health Check
- **Endpoint**: `GET /api/v1/health`
- **Description**: Returns application health status including database and Redis connectivity
- **Response**:
```json
{
  "status": "ok",
  "timestamp": "2026-05-30T10:30:00.000Z",
  "database": {
    "status": "healthy",
    "timestamp": "2026-05-30T10:30:00.000Z"
  },
  "redis": {
    "status": "healthy",
    "timestamp": "2026-05-30T10:30:00.000Z"
  }
}
```

---

## 🧪 Verification Checklist

Run through this checklist to verify your setup:

- [ ] Docker containers are running: `docker ps`
- [ ] Frontend accessible: http://localhost:3000
- [ ] Backend accessible: http://localhost:8000
- [ ] API documentation: http://localhost:8000/docs
- [ ] Health check passing: http://localhost:8000/api/v1/health
- [ ] Database connected: Check backend logs
- [ ] Redis connected: Check backend logs
- [ ] No errors in console/logs
- [ ] Environment variables properly set
- [ ] Storage directories created

### Manual Testing

```bash
# Test Backend Health
curl http://localhost:8000/api/v1/health

# Test Frontend (should return HTML)
curl http://localhost:3000

# Check Database Connection
docker-compose exec postgres psql -U ai_user -d ai_reel_generator -c "SELECT 1"

# Check Redis Connection
docker-compose exec redis redis-cli ping
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 3000
lsof -i :3000  # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Kill the process and retry
```

### Docker Compose Up Fails
```bash
# Clear all containers and volumes
docker-compose down -v

# Rebuild containers
docker-compose up -d --build
```

### Database Connection Error
1. Check PostgreSQL is running: `docker-compose logs postgres`
2. Verify DATABASE_URL in backend/.env
3. Ensure credentials are correct

### Redis Connection Error
1. Check Redis is running: `docker-compose logs redis`
2. Verify REDIS_URL in backend/.env

### Frontend Build Failures
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Backend Import Errors
```bash
cd backend
pip install --upgrade -r requirements.txt
```

---

## 📖 Documentation

Detailed phase documentation is available in the `docs/` directory:

- **Phase-00-Project-Foundation.md** (Current) - Project structure and setup
- **Phase-01-Backend-Core.md** (Next) - Core backend infrastructure
- **Phase-02-Database-Project-Management.md** - Database schemas and management
- **Phase-03-Story-Generator.md** - Story generation engine
- **Phase-04-Character-Consistency-Engine.md** - Character management
- **Phase-05-Image-Generation.md** - Image generation integration
- **Phase-06-Video-Generation.md** - Video generation pipeline
- **Phase-07-Voice-Generation.md** - Voice synthesis
- **Phase-08-Subtitle-Generation.md** - Subtitle generation
- **Phase-09-FFmpeg-Render-Engine.md** - Video rendering
- **Phase-10-Dashboard-UI.md** - User dashboard
- **Phase-11-Queue-System.md** - Background job processing
- **Phase-12-Docker-Local-Production-Setup.md** - Production deployment

---

## 🔄 Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Commit frequently with meaningful messages
   - Follow the existing code style

3. **Test your changes**
   - Test locally before committing
   - Ensure all services are running

4. **Create a pull request**
   - Push to your feature branch
   - Create PR with clear description

---

## 📝 Commit Convention

Use conventional commits for clear commit history:

```
chore: [description]      # Maintenance tasks
feat: [description]       # New features
fix: [description]        # Bug fixes
docs: [description]       # Documentation
test: [description]       # Tests
refactor: [description]   # Code refactoring
```

Example:
```bash
git commit -m "feat: add health check endpoint"
git commit -m "fix: database connection timeout"
git commit -m "chore: initialize AI Reel Generator foundation"
```

---

## 🔒 Security Notes

⚠️ **Development Environment Only**

The current setup is configured for development. For production:

1. Change default database credentials
2. Change default Redis password
3. Set `DEBUG=false`
4. Configure CORS properly
5. Use environment secrets management
6. Enable HTTPS
7. Add authentication/authorization
8. Use strong passwords
9. Configure firewall rules
10. Enable database backups

---

## 📞 Support

For issues or questions:

1. Check the documentation in `docs/` directory
2. Review troubleshooting section above
3. Check logs: `docker-compose logs -f [service]`
4. Create an issue with detailed description

---

## 📄 License

[Add your license here]

---

## 🎯 Next Steps

After verifying this foundation setup:

1. ✅ **Phase 0 Completed** - Foundation
2. → **Phase 1** - Backend Core Infrastructure
3. → **Phase 2** - Database Project Management
4. → **Phase 3** - Story Generator
5. → **Phase 4** - Character Consistency Engine
... and more

---

**Last Updated**: May 30, 2026  
**Status**: Foundation Phase Complete ✅  
**Version**: 0.1.0" 
