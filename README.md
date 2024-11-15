# Movie Recommendation System

## Overview

This project is a movie recommendation system that suggests movies based on content similarity. The system leverages cosine similarity to recommend movies by analyzing numerical features from a comprehensive movie dataset. The project is implemented in Python and features a web interface built using Streamlit.

## Project Features

**Data Preparation:** The movie dataset is processed with attributes converted to numerical format to facilitate cosine similarity calculations.

**Cosine Similarity:** Utilizes cosine_similarity from scikit-learn to compute the similarity between movies based on scaled features.

**Web App Interface:** Integrates with Streamlit for a user-friendly interface where users can input movie titles and receive personalized movie recommendations.

**Model Persistence:** Uses joblib to save essential components, enabling efficient reuse of data and pre-computed similarity matrices.

## How to Run the Project

**1. Environment Setup**

Ensure Python and the required libraries are installed:

```pip install pandas scikit-learn streamlit joblib```

**2. Running the Streamlit App**

Clone this repository and navigate to the project directory.

Launch the Streamlit app using:

```streamlit run app.py```

Enter a movie title in the input field to get movie recommendations.

**3. Dockerization (Optional)**

If you want to run the app in a Docker container:

*Build the Docker image:*

```docker build -t movie-recommender .```

*Run the Docker container:*

```docker run -p 8501:8501 movie-recommender```

**4. Project Files**

**app.py:** Main script containing the Streamlit app logic.

**movie_predict.pkl:** Serialized model file for cosine similarity.

**netflix.xlsx:** Dataset file containing movie attributes.

**Dockerfile:** Instructions to build the Docker image.

**Usage Instructions**

Enter the title of a movie in the input box provided by the Streamlit app.

The app will display a list of recommended movies based on content similarity.

