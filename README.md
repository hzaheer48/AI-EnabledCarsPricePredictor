# AI-Enabled Used Cars Price Predictor

## Overview

This project focuses on predicting the prices of used cars in Pakistan using an AI-based approach. The data for training the model was scraped from PakWheels, a popular website dedicated to selling cars in Pakistan. The web scraping was performed using a Python spider.

## Features

- **Web Scraping:** Utilized Python spider to collect data from the PakWheels website.
- **Model Training:** Employed GradientBoostingRegressor for training the predictive model.
- **Model Accuracy:** Achieved an impressive accuracy of approximately 90% during training.
- **Model Persistence:** The trained model has been saved for later use.
- **GUI with Flask:** Implemented a user-friendly web interface using Flask for users to input information and receive price predictions.

## Requirements

- Python 3.x
- Flask
- scikit-learn

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/used-cars-price-predictor.git
   cd used-cars-price-predictor
   
1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   
1. **Run the Flask app:**

   ```bash
   python app.py

4. **Open your browser and navigate to http://localhost:5000 to use the application.**


## Model Training
   The model training process is detailed in the model_training.ipynb notebook. For optimal results, consider retraining the model with updated data.
   
## Screenshots
   ![Alt text](/screenshots/screenshot_1.png?raw=true "Optional Title")

## Contributions
   Feel free to contribute to this project by opening issues or creating pull requests.
