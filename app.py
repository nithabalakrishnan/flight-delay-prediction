import os
import model
import pandas as pd
import numpy as np

from flask import Flask, request, render_template, jsonify

import sys, os
import pprint
dep_delay_data = pd.read_csv('CleanData/flight_prediction_dummies.csv')
airport_ids  = pd.read_csv('CleanData/airport_id.csv',header=None)
#print(dep_delay_data.head(1))
#print(airport_ids.iloc[:,0].tolist())
app = Flask(__name__, template_folder="templates", static_folder="static")

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(dep_delay_data.drop('DEP_DELAY', axis=1),dep_delay_data['DEP_DELAY'], test_size=0.1, random_state=42)
print("--------------")
#print(train_x)


# model.ontime()

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/getPredictions/<sample>")
def getPredictions(sample):
    # departureAirport = request.args.get('departureAirport')
    # arrivalAirport = request.args.get('arrivalAirport')
    # departureDate = request.args.get('departureDate')
    # departureAirport = request.form.get('departureAirport')
    # arrivalAirport = request.form.get('arrivalAirport')
    # departureDate = request.form.get('departureDate')

    print("Got data")
    data = {
        "departureDate": 'departureDate',
        "arrivalAirport": 'arrivalAirport',
        "departureDate": 'departureDate',
    }
    return jsonify(data)


@app.route("/airportIDs")
def airportIds():
    return jsonify(airport_ids.iloc[:,0].tolist())


if __name__ == '__main__':
    app.run(port=5001,debug=True) 
