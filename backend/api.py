"""Precisa ter rota /api/create_item [tipo post]
Precisa ter rota /api/read_item [tipo get]
Precisa ter rota /api/update_item [tipo post]
Precisa ter rota /api/delete_item [tipo get]"""

from flask import Flask, request
from flask_restful import Resource, Api
import dataset
import logging

db = dataset.connect('sqlite:///mydatabase.db')
table = db['Armarios']
app = Flask(__name__)
api = Api(app)
from datetime import datetime

class Crud(Resource):
    def post(self):
        dados = request.get_json()
        nome = dados["nome"]
        descricao = dados["dec"]
        quant = dados["quant"]
        data = str(datetime.now())
        table.insert(dict(name=nome, descricao=descricao, quantidade=quant, date=data))
        return {"status": "create"}
    
    def get(self):
        ver = []
        for row in table:
            ver.append(row)
        print(ver)
        return ver
    
    def put(self):
        dados = request.get_json()
        id_rec = dados["id"]
        nome = dados["nome"]
        descricao = dados["dec"]
        quant = dados["quant"]
        data = str(datetime.now())
        dados_dicionario = {}
        for row in table:
            row = dict(row)
            if id_rec in str(row['id']):
                dados_dicionario = dict(id=id_rec, name=nome, descricao=descricao, quantidade=quant, date=data)
                table.update(dados_dicionario, ["id"])
        return {"status":"ATUALIZADO", "dados": dados_dicionario}
    
    def delete(self):
        dados = request.get_json()
        print("#################################",dados)
        id_rec = dados["id"]
        dados_dicionario = {}
        for row in table:
            row = dict(row)
            if id_rec in str(row['id']):
                dados_dicionario = dict(id=row['id'], name=row['name'])
                table.delete(id=row['id'], name=row['name'])
        return {"status":"Deletado", "Dados": dados_dicionario}

api.add_resource(Crud, "/api/")

if __name__ == "__main__":
    app.run(debug=True)
