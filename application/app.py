from flask import Flask, render_template, request
import json
import joblib
import numpy as np


app = Flask(__name__)
@app.route('/')
def index():
    data = read_from_json_file('../train_model/data.json')
    return render_template('index.html',company=data['Company'],name=data['Names'],engine_type=data['Engine Type'],transmission=data['Transmission'],
                                        registered_city=data['Registered City'],body_type=data['Body Type'],assembley=data['Assembly'],
                                        color=data['Color'])

@app.route('/predict', methods=['POST'])
def predict():
    data = read_from_json_file('../train_model/data.json')
    company = request.form['company']
    company = data['Company'][company]
    name = request.form['name']
    name = data['Names'][name]
    engine_type = request.form['engine_type']
    engine_type = data['Engine Type'][engine_type]
    transmission = request.form['transmission']
    transmission = data['Transmission'][transmission]
    registered_city = request.form['registered_city']
    registered_city = data['Registered City'][registered_city]
    body_type = request.form['body_type']
    body_type = data['Body Type'][body_type]
    assembley = request.form['assembley']
    assembley = data['Assembly'][assembley]
    color = request.form['color']
    color = data['Color'][color]
    year = request.form['model_year']
    mileage = request.form['mileage']
    capacity = request.form['engine_capacity']
    model = joblib.load('../train_model/trained_model.pkl')
    prediction = model.predict((np.array([[year,mileage,engine_type,transmission,registered_city,color,assembley,body_type,capacity,company,name]])))
    prediction = int(prediction)
    percentage = prediction*2/100
    prediction = str(int(prediction-percentage))+' PKR - '+str(int(prediction+percentage))+' PKR'
    return render_template('index.html',company=data['Company'],name=data['Names'],engine_type=data['Engine Type'],transmission=data['Transmission'],
                                        registered_city=data['Registered City'],body_type=data['Body Type'],assembley=data['Assembly'],
                                        color=data['Color'], prediction=prediction)


"""

Helper functions

"""

def read_from_json_file(file):
    with open(file, 'r') as fp:
        data = json.load(fp)
    return data

if __name__ == '__main__':
    app.run()