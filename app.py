from flask import Flask, request
from smartphonedb import SmartphoneDB
from cartdb import CartDB
import json

app = Flask(__name__)
db = SmartphoneDB()
cartdb = CartDB()
url = 'http://127.0.0.1:5000/'

@app.route('/', methods=['GET'])
def homepage():
    html = f"""
    <h1>Grocery list by</h1>
    <ul>
        <li><a href="{url}smartphone">Statuscode</a></li>
        <li><a href="{url}smartphone/brands">All tables</a></li>
        <li><a href="{url}smartphone/Apple">Get by brand [in table]<a/>
        <li><a href="{url}smartphone/name/Apple iPhone Xs Max">Get by name<a/>
        <li><a href="{url}smartphone/price/1123.5">Get by price</a>
        <li><a href="{url}smartphone/add">Add with POST method</a>
        <li><a href="{url}smartphone/delete/<doc_id>">Delete smartphone with doc id</a>
        <li><a href="{url}cart/cart">Check the cart</a>
        <li><a href="{url}cart/add">Add to cart</a>
        <li><a href="{url}cart/delete/tablename/<doc_id>">Delete from cart with doc id</a>
    </ul>"""
    return html

@app.route('/smartphone')
def smartphone():
    return {'status':'200'}

@app.route('/smartphone/brands')
def brands():
    return json.dumps(db.brands())

@app.route('/smartphone/<brand>', methods=['POST', 'GET'])
def by_brand(brand):
    return db.get_phone_list(brand)

@app.route('/smartphone/<brand>/<int:idx>')
def getphone(brand, idx):
    return db.getPhone(brand, idx)

# @app.route('/smartphone/<name>')
# def by_name(name):
#     return db.get_smartphone_by_name(name)

# @app.route('/smartphone/<price>')
# def by_price(price):
#     return db.get_smartphone_by_price(price)

# @app.route('/smartphone/delete/<brand>/<doc_id>')
# def del_by_doc_id(brand, doc_id):
#     db.delete_smartphone(brand, doc_id)

@app.route('/cart/<tablename>')
def cart(tablename):
    return json.dumps(cartdb.get_all(tablename))

@app.route('/cart/add/', methods=['POST'])
def add_cart():
    data = request.get_json()
    cartdb.add(data)
    return {'status':200}

@app.route('/cart/delete/<tablename>/<int:doc_id>')
def delcart(tablename, idx):
    cartdb.remove_cart(tablename, idx)
    return {'status':200}

if __name__ == '__main__':
    app.run(debug=True)
