# AgroLens - AI-Driven Crop Disease Forecast Platform

 **Predicting crop diseases before they happen**

AgroLens is an AI-powered web platform that predicts crop disease outbreaks based on weather data, soil conditions, and satellite-based vegetation indices. It provides farmers with early warnings and actionable advice to prevent crop losses.

##  Features

- **Predictive AI**: Forecasts disease probability before visible symptoms
- **Real-time Data**: Integrates weather and satellite vegetation data
- **Smart Alerts**: Automated email/SMS notifications for high-risk conditions
- **Farmer Dashboard**: User-friendly interface for crop and location management
- **Historical Analytics**: Tracks predictions and outcomes for continuous improvement

## Technology Stack

### Frontend
- React.js with Tailwind CSS
- Chart.js for data visualization
- Responsive mobile-first design

### Backend
- Node.js + Express.js REST API
- JWT Authentication
- MongoDB Atlas for data storage

### AI/ML
- Python Flask microservice
- TensorFlow/Scikit-learn models
- Weather & satellite data integration

### Cloud & APIs
- Firebase for notifications
- OpenWeatherMap API
- NASA Earth Data API
- Vercel/Render deployment

##  Real-World Impact

Contributes to UN SDGs:
- **Goal 2**: Zero Hunger - Preventing crop losses
- **Goal 13**: Climate Action - Sustainable farming practices

##  Project Structure

```
agrolens-ai-crop/
├── frontend/          # React.js dashboard
├── backend/           # Node.js API server
├── ai-service/        # Python ML microservice
├── docs/              # Documentation
└── deployment/        # Deployment configs
```

## Quick Start

1. Clone the repository
2. Install dependencies for each service
3. Set up environment variables
4. Run development servers
5. Access the dashboard at localhost:3000

##  Workflow

1. Farmer registers and selects crop/location
2. System fetches real-time weather/soil data
3. AI model predicts disease risk probability
4. Dashboard displays risk score and advisory
5. Automated alerts sent if risk exceeds threshold
6. Data stored for analytics and model improvement
