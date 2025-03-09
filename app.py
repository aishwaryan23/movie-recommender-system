import streamlit as st
import pickle
import pandas as pd

st.markdown(
    """
    <style>
    .stApp {
        background-color: #80CBC4;
        color: black;
    }
    .tit {
        text-align: center;
        font-size: 100px;
        font-weight: bold;
        color: black;
    }
    .custom-label {
        font-size: 20px;
        font-weight: bold;
        color: red;  /* Change this to any color */
    }
     
    
    /* Change text color */
    .stTextInput, .stSelectbox, .stButton {
        color: black !important;
    }
    

    /* Custom button styling */
    div.stButton > button {
        background-color: #B4EBE6 ;
        color: black;
        border-radius: 10px;
        padding: 10px;
        width: 100%;
        font-size: 16px;
        font-weight:bold;
    }

    /* Button hover effect */
    div.stButton > button:hover {
        background-color: white;
        color: black;
        border: 2px solid black;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.markdown('<h1 class="tit"><u>Movie Recommender System</u></h1>',unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p style="color: black; font-size: 30px; font-weight: bold;">Search your favourite movies </p>', unsafe_allow_html=True)
selected_movie_name = st.selectbox("",movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

