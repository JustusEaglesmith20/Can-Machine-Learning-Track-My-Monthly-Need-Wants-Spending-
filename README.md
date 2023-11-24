# Can Decision Tree Classifiers Perform Better than Neural Networks at Classifying my Personal Expenses?
# Personal Finance Dashboard Project

## Project Overview

### Can Decision Tree Classifiers Perform Better than Neural Networks at Classifying my Personal Expenses?

![Personal Finance Dashboard](https://i.imgur.com/p8PBgfP.gif)

In this project, I explore the intriguing possibility of a Decision Tree Classifier outperforming Neural Networks in classifying my personal expenses. This Jupyter notebook delves into the nuances of my transaction data, identifying patterns and anomalies. It plays a crucial role in refining my model, especially in differentiating necessary expenses ('Needs') from non-essential ones ('Wants').

### Purpose and Scope

The primary aim is to develop a Machine Learning model capable of accurately classifying transactions into 'Needs' or 'Wants'. The project also focuses on integrating this model into a web application using Flask, enabling dynamic visualization of monthly spending upon uploading new transaction data.

### Methodology

1. **Exploratory Data Analysis (EDA)**: Initial analysis to understand spending patterns and categorize transactions effectively.
2. **Model Development**: Training a Decision Tree Classifier and benchmarking its performance against a Neural Network model, with a focus on achieving high F1 scores.
3. **Application Development**: Embedding the chosen model into a Dash-based web application for real-time data visualization.

## Key Components

- **Data Handling**: Utilization of `pandas`, `numpy`, and data preprocessing techniques.
- **Machine Learning**: Implementation of `DecisionTreeClassifier` and exploration of Neural Network architectures.
- **Visualization**: Insightful plots using `matplotlib`, `seaborn`, and `wordcloud`.
- **Model Deployment**: Integration of the model into a Flask web app, enabling interactive data analysis and visualization.

## Exploratory Data Analysis (EDA)

Starting with a dataset of personal transactions, the EDA process involves:
- Categorizing transactions based on specific criteria.
- Performing statistical analysis to understand spending habits.
- Visualizing spending trends and patterns over different time frames.

## Model Training and Evaluation

1. **Decision Tree Classifier**: 
   - Trained on a subset of the data.
   - Evaluated for accuracy and F1 score.
   - Hyperparameter tuning with `GridSearchCV`.

2. **Neural Network Model**: 
   - Constructed using TensorFlow and Keras.
   - Assessed through validation and test accuracy, as well as F1 scores.

## Results and Insights

- The Decision Tree model outperformed the Neural Network in this specific context.
- Key insights were drawn from feature importances and spending categories.
- The 'purchase' keyword emerged as a significant indicator of transaction nature.

## Web Application: Personal Finance Dashboard

The project culminates in a Dash-based web app that allows users to:
- Upload their transaction data.
- Visualize the categorized spending dynamically.
- Interact with the data to gain deeper insights into their financial habits.

## Conclusion

This project demonstrates the efficacy of simple Machine Learning models in specific contexts and underscores the importance of methodical EDA and model selection. The integration of the model into a practical application highlights the real-world applicability of data science skills.

## Running the App

To run the application locally:

python app.py

Note: To run the application locally, use the command python app.py and access it via a web browser at: http://127.0.0.1:8050/
---

**Author**: Justus Eaglesmith  
**GitHub Repository**: https://github.com/JustusEaglesmith20/NN-or-Decision-Tree-for-Personal-Expense-Classification-  
**Portfolio**: https://github.com/JustusEaglesmith20

---
