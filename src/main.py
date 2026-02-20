'''import streamlit as st
from movie_api import get_movie_by_id
from app_db import init_db, create_table, save_movie, get_all_movies

init_db()
create_table()

st.set_page_config(page_title="Movie Finder", layout="centered")
st.title("Movie Finder App")

movie_id = st.text_input("Enter movie id: ")
if st.button("search"):
    movie = get_movie_by_id(movie_id)

    if movie is None:
        st.error("Movie not found")
    else:
        st.subheader(movie["title"])
        st.write("Year:", movie["year"])
        st.write("Genres:", movie["genres"])
        st.write("Country:", movie["country"])
        st.write("imdb_rate:", movie["imdb_rate"])

        if st.button("Save to database"):
            save_movie(movie)
            st.success("Saved")

st.divider()
st.header("Save Movies")

movies = get_all_movies()

for m in movies:
    st.markdown(f'''

{m[1]}

''')
'''