# 🎓 AI-Powered Student Intelligence System

An end-to-end Data Science project that predicts student performance based on study habits, lifestyle, and academic factors. The project will evolve into a full-stack application with ML model deployment on cloud.

---

## 📅 Day 1: Project Setup & Data Pipeline

### ✅ Work Completed
- Created structured project architecture
- Set up GitHub repository
- Integrated Google Colab with GitHub workflow
- Loaded dataset from Google Drive
- Built modular Python scripts:
  - `load_data.py` → for dataset loading
  - `preprocess.py` → for initial preprocessing
- Created `main.py` to run pipeline
- Defined:
  - **Target variable:** `G3` (final grade)
  - **Features:** all columns except `G1`, `G2`, `G3`

---

### 🧠 Key Learning
- Importance of correct CSV delimiter (`,` vs `;`)
- Avoiding data leakage by removing `G1` and `G2`
- Structuring ML projects using modular `.py` files instead of notebooks

---

### 📊 Dataset Info
- Total Records: 395 students
- Features: ~30 input features
- Target: Final Grade (`G3`)

---

## 📅 Day 2: Data Cleaning, Encoding & EDA

### ✅ Work Completed
- Implemented data cleaning module
- Handled missing values
- Built feature encoding pipeline using one-hot encoding
- Performed Exploratory Data Analysis (EDA)
- Generated visual insights:
  - Study Time vs Final Grade
  - Absences vs Final Grade

---

### 📊 Key Insights
- Higher study time generally leads to better grades
- More absences tend to reduce performance

---

### 🧠 Key Learning
- Importance of encoding categorical variables
- Data visualization for pattern discovery
- Building modular ML pipelines

---

## 📅 Day 3: SQL Database Integration

### ✅ Work Completed
- Created SQLite database
- Designed students table
- Inserted cleaned student records
- Retrieved data from database
- Built reusable database module

### Technologies Used
- Python
- SQLite
- Pandas

### Key Learning
- Database design
- SQL integration with Python
- ETL workflow (CSV → SQL)

---

## 📅 Day 4: Machine Learning Model Training

### 🎯 Objective
Train and evaluate a machine learning model using data retrieved from the SQLite database instead of directly using CSV files.

---

### ✅ Work Completed

#### Database-Driven Training
- Retrieved student records from SQLite database
- Used SQL data as the source for model training
- Established a complete data pipeline from database to machine learning model

#### Machine Learning Pipeline
- Split data into training and testing datasets
- Trained a Random Forest Regressor model
- Generated predictions on test data
- Evaluated model performance using standard metrics

#### Model Persistence
- Saved the trained model using Joblib
- Generated a reusable `.pkl` file for future deployment

---

### 📁 New Files Added

src/models/train_model.py
src/models/evaluate_model.py
models/student_model.pkl

## 📅 Day 5: Feature Engineering & Model Comparison

### 🎯 Objective
Improve the machine learning pipeline by comparing multiple algorithms and selecting the best-performing model.

---

### ✅ Work Completed

- Created feature engineering module
- Prepared training and target datasets
- Implemented train-test split
- Trained multiple machine learning models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Compared model performance using R² Score
- Selected the best-performing model
- Saved the final model for deployment

---

### 📊 Models Compared

| Model | Purpose |
|---------|---------|
| Linear Regression | Baseline Model |
| Decision Tree | Non-linear Learning |
| Random Forest | Ensemble Learning |

---

### 🧠 Key Learnings

- Feature engineering workflows
- Model benchmarking
- Performance evaluation
- Model selection strategies

---

### 📁 New Files Added

src/features/feature_engineering.py

src/models/compare_models.py

src/models/train_best_model.py

models/best_student_model.pkl

---


## 📅 Day 6: Feature Engineering & Hyperparameter Tuning

### 🎯 Objective
Improve model performance using full-feature training, hyperparameter optimization, and feature importance analysis.

---

### ✅ Work Completed

- Expanded feature set beyond basic academic attributes
- Applied one-hot encoding to categorical variables
- Implemented hyperparameter tuning using GridSearchCV
- Optimized Random Forest model
- Generated feature importance rankings
- Identified top predictors of student performance

---

### 📊 Techniques Used

- Feature Engineering
- One-Hot Encoding
- GridSearchCV
- Random Forest Regression
- Feature Importance Analysis

---

### 🧠 Key Learnings

- Impact of feature selection on model performance
- Hyperparameter optimization workflows
- Model interpretability using feature importance

---
## 📅 Day 7: Prediction Service Layer

### 🎯 Objective
Convert the trained machine learning model into a reusable prediction service.

### ✅ Work Completed

- Created model loading module
- Built prediction pipeline
- Developed service layer
- Enabled real-time grade prediction
- Tested prediction using trained model

### 📁 New Files Added

pipelines/predict_pipeline.py

src/models/predict.py

src/services/prediction_service.py

### 🧠 Key Learnings

- Model serving fundamentals
- Loading models with Joblib
- Building reusable prediction functions
- Separating training and prediction workflows

## 📅 Day 8: FastAPI Backend Development

### 🎯 Objective

Expose the machine learning model through REST API endpoints using FastAPI.

---

### ✅ Work Completed

- Installed FastAPI framework
- Created API request schema using Pydantic
- Built FastAPI application
- Implemented health check endpoint
- Implemented prediction endpoint
- Connected API with trained ML model

---

### 📁 New Files Added

src/api/app.py

src/api/schema.py

---

### 🌐 API Endpoints

GET /

Returns API status message.

GET /health

Returns system health status.

POST /predict

Accepts student attributes and returns predicted grade.

---

### Example Request

{
    "studytime": 4,
    "failures": 0,
    "absences": 2
}

### Example Response

{
    "predicted_grade": 15.3
}

---

### 🧠 Key Learnings

- FastAPI fundamentals
- REST API development
- Request validation using Pydantic
- Integrating ML models with APIs

---

## 📅 Day 9: API Validation, Logging & Testing

### 🎯 Objective

Enhance API reliability through validation, logging, and testing.

---

### ✅ Work Completed

- Added input validation using Pydantic
- Implemented API request logging
- Added exception handling
- Enabled automatic API documentation
- Created API testing module

---

### 📁 New Files Added

src/api/logger.py

tests/test_api.py

---

### 🌐 API Features

- Request Validation
- Error Handling
- Logging
- Interactive Documentation
- Automated Testing

---

### 🧠 Key Learnings

- Production API practices
- Logging and monitoring
- Validation using Pydantic
- API testing fundamentals

---

## 📅 Day 10: Streamlit Dashboard

### 🎯 Objective

Build a user-friendly web interface for grade prediction.

---

### ✅ Work Completed

- Created Streamlit dashboard
- Added interactive sliders
- Connected dashboard to prediction service
- Displayed prediction results in real time

---

### 📁 New Files Added

dashboard/app.py

---

### 🖥️ Dashboard Features

- Study Time Input
- Failures Input
- Absences Input
- Predict Button
- Instant Grade Prediction

---

### 🧠 Key Learnings

- Streamlit fundamentals
- Building ML dashboards
- Frontend integration with ML models
- Interactive user interfaces

---

