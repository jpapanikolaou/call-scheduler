from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This list will store the physicians (in-memory storage, you may want to use a database)
physicians_list = []

@app.route('/')
def home():
    print("Hit the homepage")
    return "Hello, this is homepage"

@app.route('/add-physician', methods=['POST', 'OPTIONS'])
def add_physician():
    if request.method == 'OPTIONS':
        # Respond to preflight request
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Accept')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    else:
        # Process actual request
        try:
            physician = request.get_json()
            # Add the physician data to the list
            physicians_list.append(physician)
            # Optionally, you can perform additional processing or validation here
            # Return a response (modify this based on your needs)
            print("WOW this")
            return jsonify({'status': 'success', 'message': 'Physician added successfully'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    print("Running")
    app.run(debug=True)
