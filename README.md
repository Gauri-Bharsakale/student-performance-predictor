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

```text
src/models/train_model.py
src/models/evaluate_model.py
models/student_model.pkl

