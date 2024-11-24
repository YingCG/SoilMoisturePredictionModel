from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app)

def load_data_from_csv(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    rain = data['Rain(mm)'].astype(float).tolist()
    soilTemp = data['SoilTemp(c)'].astype(float).tolist()
    soilMoisture = data['SoilMoisture(%)'].astype(float).tolist()

    return rain, soilTemp, soilMoisture

rain, soilTemp, soilMoisture = load_data_from_csv('../../Data/soil data/AcrossAucklandRainfallStation/ArarimuCombined_Data_15mins_SoilProfile.csv')


@app.route('/', methods=["GET"])
def return_home():
    return jsonify({
        "message": "Lasr 3 days of weather data",
        "rain": rain[-3: ],
         "soilTemp": soilTemp[-3: ],
        'soilMoisture': soilMoisture[-3: ]
    })
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
# https://www.youtube.com/watch?v=OwxxCibSFKk