import streamlit as st
from movie_api import get_movie_by_id
from app_db import init_db, save_movie, get_all_movies, create_table

init_db()
create_table()

st.set_page_config(page_title="Movie Finder", layout="centered")

st.title("Movie Finder App")

movie_name = st.text_input("Enter movie name:")


if st.button("Search"):
    movie = get_movie_by_id(movie_name)
    st.session_state.movie = movie  


if "movie" in st.session_state and st.session_state.movie:

    movie = st.session_state.movie

    
    st.subheader(movie["title"])
    st.write("Year:", movie["year"])
    st.write("Genre:", movie["genres"])
    st.write("Country:", movie["country"])


    if st.button("Save to Database"):
        save_movie(movie)
        st.success("Saved successfully")

elif "movie" in st.session_state and st.session_state.movie is None:
    st.error("Movie not found ")

st.divider()

st.header(" Saved Movies")

movies = get_all_movies()

for m in movies:
    st.markdown(f"""
    {m[1]} ({m[2]})  
    {m[3]}  
    {m[6]}
    """)