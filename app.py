from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/')
def main():
    data = {
        "status": "Server Up"
    }
    return jsonify(data), 200

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test_page():
    if request.method == 'GET':
        return "Usando metodo GET"
    elif request.method == 'POST':
        return "Usando metodo POST"
    if request.method == 'PUT':
        return "Usando metodo PUT"
    if request.method == 'DELETE':
        return "Usando metodo DELETE"


if __name__ == "__main__":
    app.run()