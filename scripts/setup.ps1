# Development setup script for Windows PowerShell

Write-Host "[*] AI Reel Generator - Development Setup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is installed
Write-Host "Checking Docker installation..." -ForegroundColor Yellow
try {
    $dockerVersion = docker --version
    Write-Host "[+] Docker is installed: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "[-] Docker is not installed. Please install Docker first." -ForegroundColor Red
    exit 1
}

# Check if Docker Compose is installed
Write-Host "Checking Docker Compose installation..." -ForegroundColor Yellow
try {
    $composeVersion = docker-compose --version
    Write-Host "[+] Docker Compose is installed: $composeVersion" -ForegroundColor Green
} catch {
    Write-Host "[-] Docker Compose is not installed. Please install Docker Compose first." -ForegroundColor Red
    exit 1
}

Write-Host ""

# Create necessary directories
Write-Host "[*] Creating storage directories..." -ForegroundColor Yellow
$dirs = @("storage/images", "storage/videos", "storage/audio", "storage/subtitles", "storage/renders")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "    Created $dir"
    } else {
        Write-Host "    $dir already exists"
    }
}

Write-Host ""

# Copy environment files if they don't exist
Write-Host "[*] Setting up environment files..." -ForegroundColor Yellow

if (-not (Test-Path "frontend/.env")) {
    if (Test-Path "frontend/.env.example") {
        Copy-Item "frontend/.env.example" "frontend/.env"
        Write-Host "[+] Created frontend/.env" -ForegroundColor Green
    } else {
        Write-Host "[!] frontend/.env.example not found, creating frontend/.env with defaults..." -ForegroundColor Yellow
        $frontendEnv = @"
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
NODE_ENV=development
"@
        $frontendEnv | Out-File -FilePath "frontend/.env" -Encoding UTF8
        Write-Host "[+] Created frontend/.env" -ForegroundColor Green
    }
} else {
    Write-Host "    frontend/.env already exists" -ForegroundColor Gray
}

if (-not (Test-Path "backend/.env")) {
    if (Test-Path "backend/.env.example") {
        Copy-Item "backend/.env.example" "backend/.env"
        Write-Host "[+] Created backend/.env" -ForegroundColor Green
    } else {
        Write-Host "[!] backend/.env.example not found, creating backend/.env with defaults..." -ForegroundColor Yellow
        $backendEnv = @"
DATABASE_URL=postgresql://postgres:root@localhost:5433/ai_reel_generator
REDIS_URL=redis://localhost:6379/0
APP_NAME=AI Reel Generator
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO
HOST=0.0.0.0
PORT=8000
RELOAD=true
"@
        $backendEnv | Out-File -FilePath "backend/.env" -Encoding UTF8
        Write-Host "[+] Created backend/.env" -ForegroundColor Green
    }
} else {
    Write-Host "    backend/.env already exists" -ForegroundColor Gray
}

Write-Host ""

# Start Docker containers
Write-Host "[*] Starting Docker containers..." -ForegroundColor Yellow
docker-compose up -d
if ($LASTEXITCODE -ne 0) {
    Write-Host "[-] Failed to start Docker containers" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Wait for services to be ready
Write-Host "[*] Waiting for services to be ready (10 seconds)..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

Write-Host ""

# Check database connection
Write-Host "[*] Checking database connection..." -ForegroundColor Yellow
try {
    docker-compose exec -T postgres pg_isready -U ai_user -d ai_reel_generator
    Write-Host "[+] Database is ready" -ForegroundColor Green
} catch {
    Write-Host "[!] Database connection check failed (may still be initializing)" -ForegroundColor Yellow
}

Write-Host ""

# Check Redis connection
Write-Host "[*] Checking Redis connection..." -ForegroundColor Yellow
try {
    docker-compose exec -T redis redis-cli ping
    Write-Host "[+] Redis is ready" -ForegroundColor Green
} catch {
    Write-Host "[!] Redis connection check failed (may still be initializing)" -ForegroundColor Yellow
}

Write-Host ""

# Check backend health
Write-Host "[*] Checking backend health..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/health" -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
    Write-Host "[+] Backend is healthy" -ForegroundColor Green
} catch {
    Write-Host "[!] Backend not ready yet (may still be initializing)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[+] Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "[*] Available URLs:" -ForegroundColor Cyan
Write-Host "    Frontend: http://localhost:3000"
Write-Host "    Backend:  http://localhost:8000"
Write-Host "    API Docs: http://localhost:8000/docs"
Write-Host ""
Write-Host "[*] Useful commands:" -ForegroundColor Cyan
Write-Host "    docker-compose logs -f backend     - View backend logs"
Write-Host "    docker-compose logs -f frontend    - View frontend logs"
Write-Host "    docker-compose down                - Stop all services"
Write-Host "    docker-compose up -d               - Start all services"
Write-Host ""
