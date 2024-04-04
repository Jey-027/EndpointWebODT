from flask import Flask, request, jsonify
from datetime import datetime
import json
import os
import uuid


app = Flask(__name__)

save_dir = "JSON_Files"

def save_data(data):
    try:
        with open(os.path.join(save_dir, 'datos.json'), 'r') as f:
            existent_data = json.load(f)
    except FileNotFoundError:
        existent_data = []
    
    existent_data.append(data)
    with open(os.path.join(save_dir, 'datos.json'),'w') as f:
        json.dump(existent_data, f, indent=4)


def save_individual_file(data):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{current_time}_{str(uuid.uuid4())}.json"
    with open(os.path.join(save_dir, filename), 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/datos_odt', methods=['POST'])
def endpoint():
    if request.method == 'POST':
        data = request.json

        save_data(data)
        save_individual_file(data)

        return jsonify({"MSN": "Peticion POST recibida"})
    else:
        return jsonify({"Error": "NO recibido"})

if __name__ == '__main__':
    app.run(debug=True)
