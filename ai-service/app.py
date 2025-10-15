from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

from services.weather_service import WeatherService
from services.satellite_service import SatelliteService
from models.disease_predictor import DiseasePredictor
from utils.data_processor import DataProcessor

load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize services
weather_service = WeatherService()
satellite_service = SatelliteService()
disease_predictor = DiseasePredictor()
data_processor = DataProcessor()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'service': 'AgroLens AI Service'
    })

@app.route('/predict', methods=['POST'])
def predict_disease_risk():
    """
    Predict crop disease risk based on input parameters
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['crop_type', 'location', 'planting_date', 'soil_type']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Extract parameters
        crop_type = data['crop_type']
        location = data['location']
        planting_date = data['planting_date']
        soil_type = data['soil_type']
        current_stage = data.get('current_stage', 'vegetative')
        
        logger.info(f"Processing prediction request for {crop_type} at {location}")
        
        # Get weather data
        weather_data = weather_service.get_current_weather(
            location['latitude'], 
            location['longitude']
        )
        
        # Get satellite data
        satellite_data = satellite_service.get_vegetation_indices(
            location['latitude'], 
            location['longitude']
        )
        
        # Process and combine all data
        processed_data = data_processor.prepare_features({
            'crop_type': crop_type,
            'soil_type': soil_type,
            'current_stage': current_stage,
            'planting_date': planting_date,
            'weather': weather_data,
            'satellite': satellite_data
        })
        
        # Make prediction
        prediction_result = disease_predictor.predict(processed_data)
        
        # Generate recommendations
        recommendations = generate_recommendations(
            prediction_result, 
            crop_type, 
            current_stage
        )
        
        response = {
            'risk_score': float(prediction_result['risk_score']),
            'risk_level': prediction_result['risk_level'],
            'predicted_diseases': prediction_result['diseases'],
            'confidence': float(prediction_result['confidence']),
            'weather_data': weather_data,
            'satellite_data': satellite_data,
            'recommendations': recommendations,
            'model_version': disease_predictor.get_model_version(),
            'timestamp': datetime.utcnow().isoformat()
        }
        
        logger.info(f"Prediction completed with risk score: {prediction_result['risk_score']}")
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

def generate_recommendations(prediction_result, crop_type, current_stage):
    """Generate actionable recommendations based on prediction"""
    recommendations = []
    risk_score = prediction_result['risk_score']
    
    if risk_score >= 0.8:
        recommendations.extend([
            {
                'type': 'treatment',
                'action': 'Apply preventive fungicide spray immediately',
                'priority': 'urgent',
                'timeframe': 'within 24 hours'
            },
            {
                'type': 'monitoring',
                'action': 'Increase field inspection frequency to twice daily',
                'priority': 'high',
                'timeframe': 'starting immediately'
            }
        ])
    elif risk_score >= 0.6:
        recommendations.extend([
            {
                'type': 'preventive',
                'action': 'Improve field drainage and air circulation',
                'priority': 'high',
                'timeframe': 'within 48 hours'
            },
            {
                'type': 'monitoring',
                'action': 'Monitor for early disease symptoms',
                'priority': 'medium',
                'timeframe': 'daily for next week'
            }
        ])
    elif risk_score >= 0.4:
        recommendations.extend([
            {
                'type': 'preventive',
                'action': 'Adjust irrigation schedule to reduce humidity',
                'priority': 'medium',
                'timeframe': 'within 3 days'
            },
            {
                'type': 'monitoring',
                'action': 'Regular field inspection for disease signs',
                'priority': 'medium',
                'timeframe': 'every 2-3 days'
            }
        ])
    else:
        recommendations.append({
            'type': 'monitoring',
            'action': 'Continue regular monitoring and good agricultural practices',
            'priority': 'low',
            'timeframe': 'weekly'
        })
    
    return recommendations

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)