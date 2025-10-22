# AgroLens Setup Guide

##  Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- MongoDB (local or Atlas)
- Git

### 1. Clone Repository
```bash
git clone https://github.com/Kusum-k/agrolens-ai-crop-forecast.git
cd agrolens-ai-crop-forecast
```

### 2. Backend Setup
```bash
cd backend
npm install
cp .env.example .env
# Edit .env with your configuration
npm run dev
```

### 3. AI Service Setup
```bash
cd ../ai-service
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python app.py
```

### 4. Frontend Setup
```bash
cd ../frontend
npm install
cp .env.example .env
# Edit .env with backend URL
npm start
```

##  Docker Setup

### Quick Start with Docker Compose
```bash
docker-compose up -d
```

This will start all services:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- AI Service: http://localhost:5001
- MongoDB: localhost:27017

##  Configuration

### Required API Keys
1. **OpenWeatherMap API**: Get from https://openweathermap.org/api
2. **NASA Earth Data**: Register at https://earthdata.nasa.gov/

### Environment Variables

#### Backend (.env)
```env
NODE_ENV=development
MONGODB_URI=mongodb://localhost:27017/agrolens
JWT_SECRET=your_super_secret_jwt_key_here
OPENWEATHER_API_KEY=your_openweather_api_key
NASA_API_KEY=your_nasa_api_key
```

#### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:5000/api
```

#### AI Service (.env)
```env
FLASK_ENV=development
OPENWEATHER_API_KEY=your_openweather_api_key
NASA_API_KEY=your_nasa_api_key
```

##  Usage

1. **Register**: Create a farmer account
2. **Add Crops**: Register your crops with location details
3. **Monitor**: View disease risk predictions on dashboard
4. **Alerts**: Receive notifications when risk is high
5. **Act**: Follow AI-generated recommendations

##  Testing

### Backend Tests
```bash
cd backend
npm test
```

### AI Service Tests
```bash
cd ai-service
python -m pytest tests/
```

##  Deployment

### Vercel (Frontend)
```bash
cd frontend
vercel --prod
```

### Render (Backend & AI Service)
1. Connect GitHub repository
2. Set environment variables
3. Deploy automatically

### MongoDB Atlas
1. Create cluster at https://cloud.mongodb.com
2. Update MONGODB_URI in environment

##  API Documentation

### Authentication Endpoints
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Crop Management
- `GET /api/crops` - List user crops
- `POST /api/crops` - Add new crop
- `PUT /api/crops/:id` - Update crop
- `DELETE /api/crops/:id` - Delete crop

### Predictions
- `GET /api/predictions` - Get predictions history
- `POST /api/predictions` - Request new prediction

### AI Service
- `POST /predict` - Get disease risk prediction
- `GET /health` - Service health check

##  Development

### Project Structure
```
agrolens-ai-crop-forecast/
├── frontend/           # React.js application
│   ├── src/
│   │   ├── components/ # Reusable components
│   │   ├── pages/      # Page components
│   │   ├── context/    # React context
│   │   └── services/   # API services
├── backend/            # Node.js API server
│   ├── models/         # MongoDB models
│   ├── routes/         # API routes
│   ├── middleware/     # Custom middleware
│   └── services/       # Business logic
├── ai-service/         # Python ML service
│   ├── models/         # ML models
│   ├── services/       # External APIs
│   └── utils/          # Utilities
└── deployment/         # Deployment configs
```

### Adding New Features
1. Create feature branch
2. Implement changes
3. Add tests
4. Submit pull request

## Troubleshooting

### Common Issues

**MongoDB Connection Error**
- Ensure MongoDB is running
- Check connection string in .env

**API Key Errors**
- Verify API keys are valid
- Check rate limits

**Port Conflicts**
- Change ports in environment files
- Kill processes using ports

### Logs
- Backend: Check console output
- AI Service: Check Flask logs
- Frontend: Check browser console


