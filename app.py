from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)

with open('dinosaurs.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)
    dinosaurs = {row['slug']:{'name':row['name'], 'description':row['description'], 
'image':row['image'], 'image-credit':row['image-credit'], 'source-url':row['source-url'], 
'source-credit':row['source-credit']} for row in data}

# @app.route('/')
# def index():
#     return render_template('index.html', name="Ryli", dinosaurs=dinosaurs)

@app.route('/')
@app.route('/dino')
@app.route('/dino/<dino>')
def index(dino=None):
    dinosaurs=get_dinos()
    if dino in dinosaurs.keys():
        print(dino)
        return render_template('dino.html', dinosaur=dinosaurs[dino])
    else:
        return render_template('index.html', dinosaurs=dinosaurs)

@app.route('/about')
def about():
    return render_template('about.html')