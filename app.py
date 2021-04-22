import pandas as pd
import flask
import csv
import json
from flask import request, jsonify
#from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Abrimos la cartera limpia posibilidades en formato JSON

with open('cartera_lim_jsonize.json') as f:
  cartera_posibiliades = json.load(f)

#print(cartera_posibiliades)


@app.route('/', methods=['GET'])
def dominio_api():
    return 'Este es mi local host.. la pagina principal es decir el dominio'

#http://127.0.0.1:5000


@app.route('/all/cartera-posibilidades/entera', methods=['GET'])
def cartera_api():
    return jsonify(cartera_posibiliades)

#http://127.0.0.1:5000/all/cartera-posibilidades/entera


@app.route('/all/cartera-posibilidades', methods=['GET'])
def strike_api():

    if "Strike" in request.args:
        Strike = str(request.args["Strike"])
    else:
        return "Error: Por favor indique el nivel de Strike para visualizar las opciones con ese nivel."


    results = []

   
    for cartera in cartera_posibiliades:
        if cartera['Strike'] == Strike:
            results.append(cartera)

    
    return jsonify(results)
#http://127.0.0.1:5000/all/cartera-posibilidades?Strike=700
# Cambiar 700 por el numero deseado




@app.route('/all/cartera-posibilidades/entera/new',methods =["POST"])

def opcion_nueva_api():
    cartera ={
    "": "21517", 
    "Ask": "296,47", 
    "Bid": "283,93", 
    "Comprada": "0", 
    "Contratos": "0", 
    "DEX_CONTRATO": "MC1 90000O2", 
    "Divisa": "EUR", 
    "Multiplicador": "100", 
    "Px_ejecucion": "0", 
    "Sentido": "0", 
    "Spot_Price": "3800", 
    "Strike": "900", 
    "Tipo": "Put", 
    "Underlying Code": "MC1", 
    "Underlying_name": "renta4", 
    "Vencimiento": "2022-03-18", 
    "am_eu_type": "Europea", 
    "todays_date": "2021-04-16"
  }
    return jsonify(cartera)





app.run()



