# 📱 Google Play Store App Success Predictor

This project is a machine learning web application built using **Streamlit** that predicts whether an app on the Google Play Store will be **successful or unsuccessful** based on its attributes such as category, rating, installs, type, etc.

## 🔍 Project Overview

Using historical data from the Google Play Store, this app helps developers and analysts predict an app's potential success. The model was trained using various app features and deployed via a simple and interactive Streamlit interface.

## 🧠 Features

- Predict app success based on input fields:
  - Category
  - Rating
  - Reviews
  - Installs
  - Type (Free/Paid)
  - Content Rating
  - Genre
- Clean and interactive UI using Streamlit
- ML model trained using a dataset from the Google Play Store

## 🗂️ Project Structure

```bash
.
├── PlayStore.ipynb         # Jupyter notebook with EDA, preprocessing, and model training
├── googleplaystore.csv     # Original dataset
├── streamlit.py            # Streamlit web app script
├── model.pkl               # Trained classification model (required for running streamlit app)
└── README.md               # Project documentation
