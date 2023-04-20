"""Precisa ter rota /api/create_item [tipo post]
Precisa ter rota /api/read_item [tipo get]
Precisa ter rota /api/update_item [tipo post]
Precisa ter rota /api/delete_item [tipo get]"""

from flask import Flask, request
from flask_restful import Resource, Api
import dataset

db = dataset.connect('sqlite:///mydatabase.db')
table = db['Armarios']
app = Flask(__name__)
api = Api(app)
from datetime import datetime

class Crud(Resource):
    def post(self):
        dados = request.get_json()
        nome = dados["nome"]
        data = str(datetime.now())
        table.insert(dict(name=nome, date=data))
        return {"status": "create"}
    def get(self):
        ver = []
        for row in table:
            ver.append(row)
        print(ver)
        return ver
    def put(self):
        dados = request.get_json()
        print(dados)
        id_n = dados["id"]
        print(id)
        user = table.find(id=id_n)
        print(user)
        #data = dict(id=user)
        #table.update(data, ["id"])
        return {"SATU":"ATU"}
    

api.add_resource(Crud, "/api/")

if __name__ == "__main__":
    app.run(debug=True)