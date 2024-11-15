# Movie Recommendation System

## Overview
This project is a **movie recommendation system** based on content similarity using cosine similarity and numerical features from a comprehensive movie dataset. The system is designed to recommend movies based on user input and is implemented in Python with the option to create a web interface using **Streamlit**.

## Project Features
- **Data Preparation**: Utilizes a movie dataset with attributes converted to numerical format for cosine similarity calculations.
- **Cosine Similarity**: Employs `cosine_similarity` from `scikit-learn` to compute similarity between movies based on feature scaling.
- **Web App**: Includes integration with **Streamlit** for a user-friendly interface to input movie titles and receive recommendations.
- **Model Persistence**: Saves necessary components for reuse, ensuring that data preprocessing and calculations do not need to be repeated.

## How to Run the Project

### 1. Environment Setup
Ensure that Python and necessary libraries are installed:
```bash
pip install pandas scikit-learn streamlit joblib
```
