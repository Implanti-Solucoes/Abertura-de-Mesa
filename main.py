import socket

from bson import Int64
from lxml import objectify
from flask import render_template, Flask, request
from datetime import date, datetime
from bson.tz_util import FixedOffset
from datetime import datetime
from pymongo import MongoClient
app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def index_post():
    today = str(date.today())
    mesa = int(request.form['mesa'])
    hora_abertura = request.form['horaAbertura']
    hora_fechamento = request.form['horaFechamento']

    datime_abertura = datetime.strptime("{} {}:00.000000".format(today, hora_abertura), "%Y-%m-%d %H:%M:%S.%f")
    datime_fechamento = datetime.strptime("{} {}:59.999000".format(today, hora_fechamento), "%Y-%m-%d %H:%M:%S.%f")

    query = {
        "DataHora": {
            u"$gte": datime_abertura.replace(tzinfo=FixedOffset(-180, "-0300"))
        },
        "DataHoraFechamento": {
            u"$lte": datime_fechamento.replace(tzinfo=FixedOffset(-180, "-0300"))
        },
        "Situacao": 3,
        "$or": [
            {
                u"NumeroMesaConta": Int64(mesa)
            },
            {
                u"NumeroMesa": Int64(mesa)
            }
        ]
    }

    client = conexao()
    database = client["DigisatServer"]
    collection = database["ItensMesaConta"]
    if 'reabrir' not in request.form:
        cursor = collection.find(query)
        return render_template('lista_mesas.html', itens=cursor, form=request.form)
    else:
        cursor = collection.update_many(query, {"$set": {"Situacao": 2}})
        return render_template('index.html')


def conexao():
    f = open(r'C:\DigiSat\SuiteG6\Sistema\ConfiguracaoClient.xml', 'r')
    data = f.read()
    f.close()
    data = data.replace('<?xml version="1.0" encoding="utf-8"?>\n', '')
    data = data.replace('ï»¿', '')
    xml = objectify.fromstring(data)
    host = str(xml.Ip) if hasattr(xml, 'Ip') else '127.0.0.1'
    try:
        socket.inet_aton(host)
    except socket.error:
        try:
            host = socket.gethostbyname(host)
        except:
            host = '127.0.0.1'

    client = MongoClient(
        host=host, username='root', password='|cSFu@5rFv#h8*=',
        authSource='admin', port=12220, serverSelectionTimeoutMS=5000,
        connectTimeoutMS=10000, authMechanism='SCRAM-SHA-1'
    )
    return client
