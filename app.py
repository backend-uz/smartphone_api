# simple flask app
from flask import Flask, request, jsonify
from smartphonedb import DB
import json
db = DB('db.json')

app = Flask(__name__)

@app.route('/smartphone')
def getBrads() -> dict:
    """
    Return list of brands
    """
    return jsonify({"brands":db.get_tables()})

@app.route('/smartphone/<brand>')
def getPhones(brand) -> dict:
    """
    Return list of phones by brand
    """
    return jsonify({"phones":db.get_phone_list(brand)})

@app.route('/smartphone/<brand>/<int:idx>')
def getPhone(brand,idx) -> dict:
    """
    Return phone data by brand
    """
    return db.getPhone(brand,idx)

@app.route('/smartphone/<brand>',methods=['POST'])
def addPhone(brand) -> dict:
    """
    Add new phone to the database
    """
    all_table = db.get_tables()
    if brand in all_table:
        data = request.get_json()
        table = db.db.table(brand)
        table.insert(data)
        return {"status":"success"}
    else:
        return {"status":"failed","message":"Brand not found"}

if __name__ == '__main__':
    app.run(debug=True)