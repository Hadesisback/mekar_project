import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin 
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()

def run_app():
    app = Flask(__name__)
    CORS(app, support_credentials=True)

    mongodb_url = os.getenv('MONGODB_URL')
    
    client = MongoClient(mongodb_url)
   
    db = client['data']
    collection = db['users']

    @app.route('/submitform', methods=['POST'])
    @cross_origin(supports_credentials=True)
    def pushtoDB():
        data = request.json
        name = data.get('name')
        identity_number = data.get('identity_number')
        date_of_birth = data.get('date_of_birth')
        email = data.get('email')

        
        if not identity_number.isdigit() or len(identity_number) != 16:
            return jsonify({"error": "Identity number must be 16 digits and all numerical."}), 400
        
        # Check if the 7th to 12th digits of identity number match the date of birth
        id_date_part = identity_number[6:12]
        dob_parts = date_of_birth.split('-')
        dob_format = dob_parts[2][-2:] + dob_parts[1] + dob_parts[0][-3:-1]
        
        if id_date_part != dob_format:
            return jsonify({"error": "Identity number does not match the date of birth."}), 400
        
        # Check for duplicate entries in the database
        existing_entry = collection.find_one({
            "name": name,
            "identity_number": identity_number,
            "date_of_birth": date_of_birth,
            "email": email
        })
        
        if existing_entry:
            return jsonify({"message": "Duplicate entry detected."}), 200
        
        # Insert data into the database
        collection.insert_one({
            "name": name,
            "identity_number": identity_number,
            "date_of_birth": date_of_birth,
            "email": email
        })
        
        return jsonify({"message": "Data successfully inserted."}), 201

    

    @app.route('/getdata', methods=['GET'])
    @cross_origin(supports_credentials=True)
    def get_data():
        data = list(collection.find({}, {"_id": 0}))  
        if not data:
            return jsonify({"message": "No data found in the database."}), 200
        
        # Convert the data to a list of lists for tabulate
        table_data = [list(item.values()) for item in data]
        headers = ["Name", "Identity Number", "Date of Birth", "Email"]
        table = tabulate(table_data, headers, tablefmt="plain")

        return f"<pre>{table}</pre>"
    

    return app
if __name__ == '__main__':
    app = run_app()
    listen_host = os.getenv('LISTEN_HOST', '0.0.0.0')
    listen_port = int(os.getenv('LISTEN_PORT', 5000))
    app.run(host=listen_host, port=listen_port)