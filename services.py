import requests

def get_film_characters(film_id):
    url = f'https://swapi.dev/api/films/{film_id}/'
    response = requests.get(url)
    data = response.json()

    character_urls = data['characters']
    character_names = []
    for character_url in character_urls:
        character_response = requests.get(character_url)
        character_data = character_response.json()
        character_names.append(character_data['name'])
    
    return character_names

def get_sorted_films():
    url = "https://swapi.dev/api/films/"
    response = requests.get(url)
    data = response.json()
    films = data['results']
    sorted_films = sorted(films, key=lambda x: x['episode_id'])
    filtered_films = [{"id": film["episode_id"], "name": film["title"]} for film in sorted_films]

    return filtered_films