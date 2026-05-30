#!/bin/bash
# Start all services

echo "🚀 Starting AI Reel Generator services..."
docker-compose up -d
echo "✅ All services started"
echo ""
echo "Waiting for services to be ready..."
sleep 5
echo ""
echo "🔗 Access the application:"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
