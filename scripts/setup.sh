#!/bin/bash
# Development setup script

echo "🚀 AI Reel Generator - Development Setup"
echo "=========================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Create necessary directories
echo "📁 Creating storage directories..."
mkdir -p storage/{images,videos,audio,subtitles,renders}

# Copy environment files if they don't exist
echo "⚙️  Setting up environment files..."
if [ ! -f frontend/.env ]; then
    cp frontend/.env.example frontend/.env
    echo "Created frontend/.env"
fi

if [ ! -f backend/.env ]; then
    cp backend/.env.example backend/.env
    echo "Created backend/.env"
fi

# Start Docker containers
echo "🐳 Starting Docker containers..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check database connection
echo "🔍 Checking database connection..."
docker-compose exec -T postgres pg_isready -U ai_user -d ai_reel_generator

# Check Redis connection
echo "🔍 Checking Redis connection..."
docker-compose exec -T redis redis-cli ping

# Check backend health
echo "🔍 Checking backend health..."
curl http://localhost:8000/api/v1/health || echo "Backend not ready yet"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Available URLs:"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "📚 Useful commands:"
echo "   docker-compose logs -f backend     - View backend logs"
echo "   docker-compose logs -f frontend    - View frontend logs"
echo "   docker-compose down                - Stop all services"
echo "   docker-compose up -d               - Start all services"
