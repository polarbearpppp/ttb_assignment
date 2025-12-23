# TTB Customer Scoring API

A full-stack web application that predicts customer spending categories based on income and monthly spend ratio. Built with FastAPI backend and Next.js frontend, containerized with Docker.

## 📋 Project Overview

This project consists of:
- **Backend API**: FastAPI service that predicts customer spending categories (low, medium, high)
- **Frontend UI**: Next.js React application for submitting customer data and viewing predictions
- **Docker Compose**: Orchestrates backend, frontend, and testing services

## 🏗️ Project Structure

```
ttb_assignment/
├── backend/                    # FastAPI application
│   ├── main.py                 # Main API endpoints
│   ├── schema.py               # Pydantic models for request/response validation
│   ├── main_test.py            # Automated test suite
│   ├── test_case.json          # Test case data
│   ├── requirements.txt         # Python dependencies
│   ├── Dockerfile              # Backend container configuration
│   └── __pycache__/            # Python cache files
├── frontend/                   # Next.js React application
│   ├── app/                    # App directory with pages
│   │   ├── page.tsx            # Main prediction form page
│   │   ├── layout.tsx          # Root layout component
│   │   └── globals.css         # Global styles
│   ├── public/                 # Static assets
│   ├── package.json            # Node.js dependencies
│   ├── tsconfig.json           # TypeScript configuration
│   ├── next.config.ts          # Next.js configuration
│   ├── postcss.config.mjs       # PostCSS configuration
│   ├── eslint.config.mjs       # ESLint configuration
│   ├── Dockerfile              # Frontend container configuration
│   └── README.md               # Frontend-specific documentation
├── docker-compose.yml          # Docker Compose configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local development)
- Python 3.10+ (for local development)

### Using Docker Compose (Recommended)

```bash
# Start all services
docker-compose up --build

# Services will be available at:
# - Frontend: http://localhost:3000
# - Backend API: http://localhost:8000
# - API Docs: http://localhost:8000/docs
```

### Local Development

#### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

#### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 📚 API Documentation

### Base URL
- **Local**: `http://localhost:8000`
- **Production**: Will depend on deployment

### Endpoints

#### POST /predict
Predicts customer spending category based on income and average monthly spend.

**Request:**
```json
{
  "customer_id": "CUST001",
  "feature": {
    "age": 35,
    "income": 50000,
    "avg_monthly_spend": 3500
  }
}
```

**Response:**
```json
{
  "customer_id": "CUST001",
  "prediction": "high",
  "confidence": 0.85
}
```

**Prediction Categories:**
- **low**: Spend ratio < 10% of income
- **medium**: Spend ratio 10-30% of income
- **high**: Spend ratio > 30% of income

#### GET /docs
Interactive API documentation (Swagger UI)

## 🧪 Testing

### Run Tests with Docker Compose
```bash
docker-compose up --build
# Tests automatically run in the 'tester' service
```

### Run Tests Locally
```bash
cd backend
python main_test.py
```

Test cases are defined in `backend/test_case.json` and cover various spending scenarios.

## 📦 Dependencies

### Backend
- **FastAPI** 0.127.0 - Modern Python web framework
- **Uvicorn** 0.40.0 - ASGI server
- **Pydantic** 2.12.5 - Data validation
- **Pytest** 9.0.2 - Testing framework
- **Requests** 2.32.5 - HTTP client
- **CORS Middleware** - Cross-origin request support

### Frontend
- **Next.js** 16.1.0 - React framework
- **React** 19.2.3 - UI library
- **React Hook Form** 7.69.0 - Form state management
- **Tailwind CSS** 4 - Utility-first CSS framework
- **TypeScript** 5 - Type-safe JavaScript
- **ESLint** 9 - Code linting

## 🐳 Docker Services

### Backend Service
- Port: 8000
- Restarts automatically if it crashes
- Includes health check

### Frontend Service
- Port: 3000
- Depends on backend service
- Environment variable: `NEXT_PUBLIC_API_URL=http://localhost:8000`

### Tester Service
- Runs automated tests
- Depends on backend service health
- Exits after tests complete

## 🔒 Features

- ✅ REST API with FastAPI
- ✅ Type-safe request/response validation with Pydantic
- ✅ CORS support for frontend communication
- ✅ Responsive web UI with Next.js
- ✅ Form validation with React Hook Form
- ✅ Interactive API documentation (Swagger)
- ✅ Containerized with Docker
- ✅ Automated test suite
- ✅ TypeScript support throughout


## 🛠️ Development Workflow

1. **Make changes** to backend or frontend code
2. **Run locally** with `npm run dev` (frontend) and `uvicorn main:app --reload` (backend)
3. **Test** your changes with the test suite
4. **Build Docker image** and test with `docker-compose up --build`
5. **Commit** and push to repository



