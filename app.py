from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

stores = [
    {
        "name" : "My Wonderful Store",
        "items":[
            {
                "name" : "My Item",
                "price" : 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_by_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'Store not found'})
    

@app.route('/store')
def get_store():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_store = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_store['name'],
                'price' : request_store['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})
    

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message' : 'Store not found'}) 

@app.route('/')
def home():
    return render_template('index.html')
    
    


app.run(port=8080)
