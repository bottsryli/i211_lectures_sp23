from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

DINO_PATH = app.root_path + '/dinosaurs.csv'
FAQ_PATH = app.root_path + '/faq.csv'
DINO_KEYS = ['slug', 'name', 'description', 'image', 'image-credit', 'source-url', 'source-credit']


def get_dinos():
    try:
        with open(DINO_PATH, 'r') as csvfile:
            data = csv.DictReader(csvfile)
            dinosaurs = {}
            for dino in data:
                dinosaurs[dino['slug']] = dino
    except Exception as e:
        print(e)
    return dinosaurs
# with open('dinosaurs.csv', 'r') as csvfile:
#     data = csv.DictReader(csvfile)
#     dinosaurs = {row['slug']:{'name':row['name'], 'description':row['description'], 
# 'image':row['image'], 'image-credit':row['image-credit'], 'source-url':row['source-url'], 
# 'source-credit':row['source-credit']} for row in data}

def set_dinos(dinosaurs):
    try:
        with open(DINO_PATH, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=DINO_KEYS)
            writer.writeheader()
            for dino in dinosaurs.values():
                writer.writerow(dino)
    except Exception as err:
        print(err)


# @app.route('/')
# def index():
#     return render_template('index.html', name="Ryli", dinosaurs=dinosaurs)
def get_faq():
    with open(FAQ_PATH, 'r') as csvfile:
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
 
@app.route('/add-dino', methods = ['GET', 'POST'])
def add_dino():
    if request.method == 'POST':
    #grab te user data from POST
        in_slug = request.form['slug']
        in_description = request.form['description']
        in_name = request.form['name']
        in_image = request.form['image']
        in_image_credit= request.form['image-credit']
        in_source_url = request.form['source-url']
        in_source_credit = request.form['source-credit']
    #process the data 
    #create a new directory with the new dinosaur data in it
        new_dino = {'slug':in_slug, 'name':in_name, 'description':in_description, 'image':in_image, 'image-credit':in_image_credit, 'source-url':in_source_url, 'source-credit':in_source_credit}

        #grab the existing dinosaur data and add new dino
        dinosaurs=get_dinos()
        dinosaurs[in_slug] = new_dino

        set_dinos(dinosaurs)
 
        # return redirect(url_for('index'))
    else:
        return render_template('add-dino.html')




@app.route('/dino-quiz', methods = ['GET', 'POST'])
def dino_quiz():
    #do we have post data coming in?
    if request.method == 'POST':
        #process the data
        responses={}
        responses['Question1'] = request.form['Question1']
        responses['Question2'] = " and ".join(request.form.getlist('Question2'))
        responses['Question3'] = request.form.get('Question3', 'false')
        responses['Question4'] = request.form['Question4']
        print(responses)
        #redirect to index
        quiz_answers={'Question1': 'North America', 'Question2': 'Triceratops and Stegosaurus', 'Question3': 'True', 'Question4': '66'}
        quiz_results={}
        score=0
        for question in responses:
            if responses[question] == quiz_answers[question]:
                quiz_results[question] = "Correct! The answer is " + str(quiz_answers[question])
                score+=1
            else:
                quiz_results[question] = "Incorrect! The answer was " + str(quiz_answers[question])

        return render_template('dino-quiz-results.html', quiz_results=quiz_results, score=score)
    else:
        return render_template('dino-quiz.html')