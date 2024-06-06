# Medical Insurance Cost Prediction Web App
This repository contains the code and resources for a web application that predicts medical insurance costs based on various factors such as age, sex, BMI, children, smoker status, and region.

# Overview
The Medical Insurance Cost Prediction Web App uses a machine learning model to predict the medical insurance costs of an individual. The prediction is based on input features like age, sex, BMI, number of children, smoking status, and region.The dataset used in this project is from Kaggle.

# Features
-User-friendly web interface for inputting individual details.
-Real-time prediction of medical insurance costs.
-Visualization of feature importance.
-Detailed exploratory data analysis (EDA).
-Model evaluation metrics for performance assessment.
-Easy to use and extend.

# Usage
Open your web browser and navigate to http://localhost:8501.
Input the details like age, sex, BMI, number of children, smoking status, and region.
Click on the "Predict" button to get the predicted medical insurance cost.

# Exploratory Data Analysis (EDA)
The EDA process involved analyzing the dataset to understand the distribution and relationships of the features. Key steps included:

Visualizing the distribution of numerical features (age, BMI, charges).
Examining the correlation between features and the target variable.
Checking for missing values and outliers.
Analyzing categorical features (sex, smoker, region) using bar plots.

#  Model
The machine learning model used for prediction is a linear regression model trained on the Medical Cost Personal Datasets. The linear regression algorithm is chosen for its simplicity and interpretability, making it suitable for this regression problem.

Training the Model
Data Preprocessing: The dataset was cleaned and preprocessed to handle categorical variables using one-hot encoding. Missing values were handled appropriately.
Feature Selection: The features used for training include:
Age
Sex
BMI
Number of children
Smoking status
Region

Model Training: A linear regression model was trained using the Scikit-learn library. The model learns the relationship between the features and the target variable (medical insurance cost).

# Evaluation
The model is evaluated using R-squared score. R Squared Error: 0.9892091367803421. The evaluation results help in understanding the performance of the model.

# Technologies
Python: Programming language
Streamlit: Framework for building the web app
Scikit-learn: Machine learning library
Pandas: Data manipulation library
NumPy: Numerical computing library
Matplotlib/Seaborn: Data visualization libraries

# Results
The final model provides predictions for gold prices with a certain accuracy. The results are visualized using plots and graphs to show the actual vs. predicted prices.


# Contributing
Contributions are welcome! If you have any improvements or suggestions, feel free to open a pull request or create an issue.

# Deployment
The application is deployed using Streamlit. You can access it here = https://ml-project-8-gold-price-prediction-s7ye4yjuuzal5idhfppksf.streamlit.app/
