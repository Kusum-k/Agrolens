const mongoose = require('mongoose');

const predictionSchema = new mongoose.Schema({
  crop: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Crop',
    required: true
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  riskScore: {
    type: Number,
    required: true,
    min: 0,
    max: 1
  },
  riskLevel: {
    type: String,
    enum: ['low', 'medium', 'high', 'critical'],
    required: true
  },
  predictedDiseases: [{
    name: {
      type: String,
      required: true
    },
    probability: {
      type: Number,
      required: true,
      min: 0,
      max: 1
    },
    severity: {
      type: String,
      enum: ['mild', 'moderate', 'severe'],
      required: true
    }
  }],
  weatherData: {
    temperature: {
      current: Number,
      min: Number,
      max: Number
    },
    humidity: Number,
    rainfall: Number,
    windSpeed: Number,
    pressure: Number
  },
  soilData: {
    moisture: Number,
    ph: Number,
    nutrients: {
      nitrogen: Number,
      phosphorus: Number,
      potassium: Number
    }
  },
  satelliteData: {
    ndvi: Number,
    evi: Number,
    moistureIndex: Number
  },
  recommendations: [{
    type: {
      type: String,
      enum: ['preventive', 'treatment', 'monitoring'],
      required: true
    },
    action: {
      type: String,
      required: true
    },
    priority: {
      type: String,
      enum: ['low', 'medium', 'high', 'urgent'],
      required: true
    },
    timeframe: String
  }],
  modelVersion: {
    type: String,
    required: true
  },
  confidence: {
    type: Number,
    min: 0,
    max: 1
  }
}, {
  timestamps: true
});

// Index for efficient queries
predictionSchema.index({ crop: 1, createdAt: -1 });
predictionSchema.index({ user: 1, createdAt: -1 });
predictionSchema.index({ riskLevel: 1, createdAt: -1 });

module.exports = mongoose.model('Prediction', predictionSchema);