from flask import Flask
from flask import request
import flask
import json
app = Flask(__name__)
# suppose you have some information in a json variable
todos = [
        { "label": "My first task", "done": False },
        { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = flask.jsonify(todos)
    # and then you can return it on the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    print("Incoming request with the following body", decoded_object)
    todos.append(decoded_object)
    # you can convert that variable into a json string like this
    json_text = flask.jsonify(todos)
    # and then you can return it on the response body like this
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    return_value = todos.pop(position)
    print("Incoming request with the following body", return_value)
    # you can convert that variable into a json string like this
    json_text = flask.jsonify(todos)
    # and then you can return it on the response body like this
    return json_text
     
# These two lines should always be at the end of your app.py file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
