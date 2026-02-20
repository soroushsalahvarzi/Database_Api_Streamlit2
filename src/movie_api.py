import requests

def get_movie_by_id(movie_id):
    url = 'https://moviesapi.ir/api/v1/movies'

    parameter = {
        'page': movie_id
    }
    response = requests.get(url, params=parameter)

    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        data = response['data'][0]
        title = data['title']
        year = data['year']
        country = data['country']
        imdb_rate = data['imdb_rating']
        genres = data['genres']
        return {
            "title": title,
            "year": year,
            "country": country,
            "imdb_rate": imdb_rate,
            "genres": genres
        }        
    