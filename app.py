from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

def load_movies():
    with open("movies.json", "r", encoding='utf-8') as file:
        return json.load(file)

def save_movies(movies_list):
    with open("movies.json", "w", encoding='utf-8') as file:
        json.dump(movies_list, file)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/movies')
def movies_list():
    movies = load_movies()
    return render_template('movies.html', items=movies, title="Movies")

@app.route('/random')
def random_movie():
    movies = load_movies()
    selected_movie = random.choice(movies)
    return render_template('movies.html', items=[selected_movie], title="Your movie")

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        new_movie = {
            "title": request.form.get('title'),
            "genre": request.form.get('genre'),
            "year": int(request.form.get('year')),
            "desc": request.form.get('desc')
        }

        movies = load_movies()
        movies.append(new_movie)
        save_movies(movies)

    return render_template('add.html')


if __name__ == '__main__':
    app.run()