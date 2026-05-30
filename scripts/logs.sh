#!/bin/bash
# View logs for a specific service or all services

SERVICE=${1:-all}

if [ "$SERVICE" = "all" ]; then
    docker-compose logs -f
elif [ "$SERVICE" = "backend" ]; then
    docker-compose logs -f backend
elif [ "$SERVICE" = "frontend" ]; then
    docker-compose logs -f frontend
elif [ "$SERVICE" = "postgres" ]; then
    docker-compose logs -f postgres
elif [ "$SERVICE" = "redis" ]; then
    docker-compose logs -f redis
else
    echo "Usage: ./logs.sh [backend|frontend|postgres|redis|all]"
    exit 1
fi
