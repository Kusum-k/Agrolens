const mongoose = require('mongoose');

const cropSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  name: {
    type: String,
    required: true,
    trim: true
  },
  variety: {
    type: String,
    trim: true
  },
  plantingDate: {
    type: Date,
    required: true
  },
  expectedHarvestDate: {
    type: Date
  },
  location: {
    coordinates: {
      latitude: {
        type: Number,
        required: true
      },
      longitude: {
        type: Number,
        required: true
      }
    },
    address: {
      type: String,
      required: true
    }
  },
  fieldSize: {
    value: Number,
    unit: {
      type: String,
      enum: ['acres', 'hectares', 'square_meters'],
      default: 'acres'
    }
  },
  soilType: {
    type: String,
    enum: ['clay', 'sandy', 'loamy', 'silty', 'peaty', 'chalky'],
    default: 'loamy'
  },
  irrigationType: {
    type: String,
    enum: ['drip', 'sprinkler', 'flood', 'rain_fed'],
    default: 'rain_fed'
  },
  currentStage: {
    type: String,
    enum: ['seedling', 'vegetative', 'flowering', 'fruiting', 'maturity'],
    default: 'seedling'
  },
  isActive: {
    type: Boolean,
    default: true
  }
}, {
  timestamps: true
});

// Index for geospatial queries
cropSchema.index({ 'location.coordinates': '2dsphere' });

module.exports = mongoose.model('Crop', cropSchema);