from flask import Flask, request, jsonify

import json


app = Flask(__name__)

def save_data(data):
    try:
        with open('datos.json', 'r') as f:
            existent_data = json.load(f)
    except FileNotFoundError:
        existent_data = []
    
    existent_data.append(data)
    with open('datos.json', 'w') as f:
        json.dump(existent_data, f, indent=4)



@app.route('/webapp-odt', methods=['POST'])
def endpoint():
    if request.method == 'POST':
        data = request.json

        save_data(data)

        return jsonify({"MSN": "Peticion POST recibida"})
    else:
        return jsonify({"Error": "NO recibido"})

if __name__ == '__main__':
    app.run(debug=True)
