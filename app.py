from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)

def get_dinos():
    with open('dinosaurs.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile)
        dinosaurs = {row['slug']:{'name':row['name'], 'description':row['description'], 'image':row['image'], 'image-credit':row['image-credit'], 'source-url':row['source-url'], 'source-credit':row['source-credit']} for row in data}
    
    return dinosaurs
# with open('dinosaurs.csv', 'r') as csvfile:
#     data = csv.DictReader(csvfile)
#     dinosaurs = {row['slug']:{'name':row['name'], 'description':row['description'], 
# 'image':row['image'], 'image-credit':row['image-credit'], 'source-url':row['source-url'], 
# 'source-credit':row['source-credit']} for row in data}

# @app.route('/')
# def index():
#     return render_template('index.html', name="Ryli", dinosaurs=dinosaurs)
def get_faq():
    with open('faq.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        faq_list = []
        for faq in data:
            faq_list.append([faq[0], faq[1]])
    return faq_list

@app.route('/')
@app.route('/dino')
@app.route('/dino/<dino>')
def index(dino=None):
    dinosaurs=get_dinos()
    if dino in dinosaurs.keys():
        # print(dino)
        return render_template('dino.html', dinosaur=dinosaurs[dino])
    else:
        return render_template('index.html', dinosaurs=dinosaurs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    faq = get_faq()
    return render_template('faq.html', faq_list=faq)
 