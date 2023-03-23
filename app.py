import os
from flask import Flask, jsonify
from services import get_film_characters, get_sorted_films

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

@app.route("/films/<int:film_id>/characters", methods=['GET'])
def list_characters(film_id):
    character_names = get_film_characters(film_id)
    return jsonify({"characters": character_names})

@app.route("/", methods=['GET'])
@app.route("/films", methods=['GET'])
def list_movies():
    sorted_films = get_sorted_films()
    return jsonify(sorted_films)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
