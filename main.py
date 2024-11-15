import streamlit as st
import pandas as pd
import joblib

# Load dataset and model
final_df = pd.read_excel("netflix.xlsx")
cosine_sim = joblib.load('movie_predict.pkl')

# Recommendation function
def recommendation(title, cosine_sim=cosine_sim):
    if title not in final_df['Title'].values:
        return f"Title '{title}' not found in the dataset.😞 "
    
    idx = final_df[final_df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 5 similar movies
    movie_indices = [i[0] for i in sim_scores]
    result = final_df['Title'].iloc[movie_indices].tolist()
    return result

# Streamlit app
def main():
    st.title('Movie Recommender')
    st.write('Enter the name of a movie to get recommendations (e.g., Batman Begins)')

    txt_ip = st.text_input("Enter movie name:")
    if txt_ip:
        recommended_movies = recommendation(txt_ip)
        if isinstance(recommended_movies, list):
            st.write("### Recommended Movies:")
            # Display the recommended movies as a bullet list
            for movie in recommended_movies:
                st.write(f"- {movie}")
        else:
            st.write(recommended_movies)  # Handle error message if title not found
    else:
        st.write('Please enter a movie name to get recommendations.')

if __name__ == "__main__":
    main()
