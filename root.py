from flask import Flask
from flask import request, jsonify, make_response, render_template, send_file
import json
import pathlib

app = Flask(__name__)


class Recipe():
    def __init__(self, dic, filepath):
        self.time = dic['time']
        self.score = dic['score']
        self.name = dic['name']
        self.running_time = dic['running_time']
        self.training_rate = dic['training_rate']
        self.features = dic['features']
        self.categorical_features = dic.get('categorical_features')
        self.random_state = dic.get('random_state')
        self.submit_score = dic.get('submit_score')
        self.param = dic
        self.filepath = filepath

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return f"<Recipe: {self.name}>"


@app.route('/')
def home():
    path = pathlib.Path('recipe')
    recipes = []
    for recipe in path.glob('**/*.json'):
        with open(recipe, 'r') as f:
            j = json.load(f)
            recipes.append(Recipe(j, recipe.name))
    print(recipes)
    return render_template('index.html',
                           recipes=sorted(recipes, reverse=True))


@app.route('/job/<name>')
def job(name):
    path = pathlib.Path('recipe')
    with open(path / name.split('.')[0] / name, 'r') as f:
        j = json.load(f)

    return render_template('job.html',
                           recipe=Recipe(j, path))


@app.route('/static/importance/<name>')
def importance(name):
    path = pathlib.Path('result') / name.split('.')[0] / 'importance.png'
    return send_file(str(path), mimetype='image/gif')


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
