# Customer Churn Prediction

A machine learning web application that predicts customer churn for a telecom company using a Flask-based web interface.

## 📊 Project Overview

This project implements a predictive model to identify customers who are likely to churn (leave the company). The web application provides:

- Interactive home page with prediction interface
- Model performance metrics visualization
- ML pipeline documentation
- REST API for real-time predictions

## 🛠️ Technology Stack

- **Python**: Programming language
- **Flask**: Web framework for serving the ML model
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **seaborn & matplotlib**: Data visualization

## 📁 Project Structure

```
Customer-Churn-Prediction/
├── app.py                    # Main Flask application
├── model.pkl                 # Pre-trained ML model
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── data/
│   └── Telco_Customer_Churn_lyst1769326950438.csv  # Dataset
├── notebooks/
│   └── customer_churn_prediction_prod.ipynb        # Jupyter notebooks
└── templates/
    ├── home.html             # Home page template
    ├── model_metrics.html    # Model metrics display
    ├── pipeline.html         # ML pipeline documentation
    ├── layout.html           # Base layout template
    ├── header.html           # Header template
    └── footer.html           # Footer template
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12+
- Anaconda/Miniconda installed

### Using Conda Environment (Recommended)

```bash
# Create a new conda environment
conda create -p .venv python==3.12 -y

# Activate the environment
conda activate .venv/

# Install core dependencies
conda install pandas numpy seaborn scikit-learn -y

# Install Flask
conda install flask -y

# Install ipykernel for running notebooks in VS Code
conda install ipykernel --update-deps --force-reinstall -y
```

### Alternative: Using pip within conda environment

```bash
# Create and activate environment
conda create -p .venv python==3.12 -y
conda activate .venv/

# Install dependencies using requirements.txt
pip install -r requirements.txt

# Or install individually
pip install pandas numpy seaborn scikit-learn flask
```

## 📓 Running the Jupyter Notebook in VS Code

The Jupyter notebook can be opened and run directly in VS Code:

1. Open VS Code and navigate to the project folder
2. Open the notebook file: `notebooks/customer_churn_prediction_prod.ipynb`
3. VS Code will automatically detect the Python environment - select the conda kernel (.venv) from the kernel selector (top right of the notebook)
4. Run cells as needed

### Notebook Contents

The notebook typically includes:

- Data loading and exploration
- Data preprocessing
- Feature engineering
- Model training and evaluation
- Model serialization (saving to model.pkl)

## 🌐 Running the Flask Application

```bash
# Make sure you're in the project directory
cd Customer-Churn-Prediction

# Activate conda environment
conda activate .venv/

# Run the Flask app
python app.py
```

The application will start on `http://localhost:5000`

## 📡 API Endpoints

| Endpoint             | Method | Description                    |
| -------------------- | ------ | ------------------------------ |
| `/`                  | GET    | Home page                      |
| `/model_metrics`     | GET    | Model performance metrics page |
| `/pipeline`          | GET    | ML pipeline documentation      |
| `/model_metrics_api` | GET    | Get model metrics as JSON      |
| `/predict_api`       | POST   | Make a prediction              |
| `/sample/<type>`     | GET    | Get sample customer data       |

### Prediction API Example

**Request:**

```bash
curl -X POST http://localhost:5000/predict_api \
  -H "Content-Type: application/json" \
  -d '{
    "customerID": "1234-ABCDE",
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.0,
    "TotalCharges": 840.0
  }'
```

**Response:**

```json
{
  "prediction": "No",
  "probability": 0.15,
  "actual": "No"
}
```

## 📈 Model Performance

The model has been trained on the Telco Customer Churn dataset with the following performance metrics:

- **Accuracy**: ~80%+
- **Precision**: High precision in predicting churners
- **Recall**: Good recall rate for identifying potential churners
- **F1 Score**: Balanced performance measure

View detailed metrics at `/model_metrics` when the app is running.

## 🔧 Features

1. **Real-time Predictions**: Get instant churn predictions for new customers
2. **Probability Scores**: See the likelihood of churn (0-1)
3. **Sample Data**: Test with randomly sampled customer data
4. **Model Insights**: View comprehensive model performance metrics
5. **Pipeline Documentation**: Understand the ML workflow

## 📝 License

MIT License

## 👤 Author

Gourav Namdev

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
