from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})#this isn't secure, use diff method
                                                    #when releasing

@app.route('/submit-name', methods=['POST'])
def submit_name():
    # Retrieve JSON data from request
    data = request.get_json()
    print(data)  # This will print the entire JSON body as a Python dictionary

    # Access the firstName value
    if data:
        return jsonify({'status': 'success', 'data': data}), 200
    else:
        return jsonify({'status': 'error', 'message': 'firstName is missing'}), 400

@app.route('/test-get', methods=['GET'])
def test_get():
    # This is just a simple response to confirm the GET request is working
    return jsonify({'status': 'success', 'message': 'GET request received successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True,port=5001)
