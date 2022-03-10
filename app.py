import flask
from flask import request, jsonify
import sqlite3
from db import session, Cliente

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>ACADEMIA POTENAY</h1>
<p>Sejam Bem vindos</p>'''


@app.route('/clientes/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('academia.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cliente = cur.execute('SELECT * FROM cliente;').fetchall()

    return jsonify(all_cliente)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/clientes', methods=['GET'])
def api_filter():
    query_parameters = request.args

    cdCliente = query_parameters.get('cdCliente')
    nomeCliente = query_parameters.get('nomeCliente')
    telefone = query_parameters.get('telefone')
    email = query_parameters.get('email')

    query = "SELECT * FROM cliente WHERE"
    to_filter = []

    if cdCliente:
        query += ' cdCliente=? AND'
        to_filter.append(cdCliente)
    if nomeCliente:
        query += ' nomeCliente=? AND'
        to_filter.append(nomeCliente)
    if telefone:
        query += ' telefone=? AND'
        to_filter.append(telefone)
    if email:
        query += ' email=? AND'
        to_filter.append(email)
    if not (id or cdCliente or nomeCliente or telefone or email):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('academia.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()
