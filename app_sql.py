import pandas as pd
import flask
import csv
import json
from flask import request, jsonify
import sqlite3


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

"""
 ESta routa devuele todo el BBDD Scripts
"""
@app.route('/monthypython/all', methods=['GET'])

def api_all():
    conn = sqlite3.connect('archive/database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_database = cur.execute('SELECT * FROM scripts;').fetchall()

    return jsonify(all_database)
#http://127.0.0.1:5000/monthypython/all


# QUE aparece si se encunetra un 404

@app.errorhandler(404)
def page_404(e):

    return "<h1>404</h1><p>LA Base de DAtos no lo hemos encontrado: Mire el URL y asegurese de que esta bien escrito</p>", 404



@app.route('/monthypython/all/filters', methods=['GET'])
def api_filter():


    query_parameters = request.args

    episode = query_parameters.get('episode')
    tipo = query_parameters.get('type')
    character = query_parameters.get('character')

    query = "SELECT * FROM scripts WHERE"

    to_filter = []

    if episode:
        query += ' episode=? AND'
        to_filter.append(episode)
    if character:
        query += ' character=? AND'
        to_filter.append(character)
    if tipo:
        query += ' type=? AND'
        to_filter.append(tipo)

    if not (episode or tipo or character):
        return page_404(404)

    
    query = query[:-4] + ';'

    conn = sqlite3.connect('archive/database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


"""
Se visualizaran todos los episodios numero 10, puedes cambiar 10 por el numero de episodio que quieras. Si el Num de episodio no existe devuelve un dicionario vacio
"""
#http://127.0.0.1:5000/monthypython/all/filters?episode=10

"""
Visualizar los episodios numeros 10 que el character sea "Man" , otras opciones : ""It's Man" , ""Voice Over", "Wife" , "Robber", "Assistant" , "Mr Vercotti", etc.. 
"""

#http://127.0.0.1:5000/monthypython/all/filters?episode=10&character=Man

"""
Visualizar episodios 10, character Wife y tipo dialogo , otras opciones : "Direction"
"""

#http://127.0.0.1:5000/monthypython/all/filters?episode=10&character=Wife&type=Dialogue



app.run()




















app.run()