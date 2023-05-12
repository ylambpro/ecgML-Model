import os
from flask import Flask, flash, render_template, request, redirect, url_for
import sklearn, csv, pickle, numpy as np, pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static\\uploads'
ALLOWED_EXTENSIONS = {'csv', 'CSV'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
model = pickle.load(open('model/modelRandomForest.pkl', 'rb'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = None
    if request.method == 'POST':
        if ('file' not in request.files):
            flash('Aucun fichier sélectionner !')
        csvfile = request.files['file']
        if csvfile.filename == '':
            flash('Aucun fichier sélectionné !')
        if csvfile and allowed_file(csvfile.filename):
            filename = secure_filename(csvfile.filename)
            csvfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = UPLOAD_FOLDER+"\\"+filename
            df = pd.read_csv(filepath, header=None)
            array = df.values
            X = array[:,0:140]
            number_of_rows = X.shape[0]
            results = []
            if number_of_rows > 10:
                for ligne in range(10):
                    pred = model.predict(X[ligne].reshape(1,-1))
                    if pred == 1.0:
                        results.append(('1',str(ligne + 1),'ECG - '+ str(ligne + 1),'Normal'))
                    else:
                        results.append(('0',str(ligne + 1),'ECG - '+ str(ligne + 1),'Anormal'))
            else:
                for ligne in range(number_of_rows):
                    pred = model.predict(X[ligne].reshape(1,-1))
                    if pred == 1.0:
                        results.append(('1',str(ligne + 1),'ECG - '+ str(ligne + 1),'Normal'))
                    else:
                        results.append(('0',str(ligne + 1),'ECG - '+ str(ligne + 1),'Anormal'))
            predictions = results
    return render_template('index.html', interpretations = predictions)

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)