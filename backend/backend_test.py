import unittest
from flask_testing import TestCase
from pymongo import MongoClient
from backend import run_app
from dotenv import load_dotenv
import os

load_dotenv()

class TestFlaskApp(TestCase):
    
    def create_app(self):
        app = run_app()
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        # Connect to database
        self.mongo_client = MongoClient(os.getenv('MONGODB_URL'))
        self.db = self.mongo_client['data']
        self.collection = self.db['users']
        self.collection.delete_many({})  # Clear the collection before each test

    def tearDown(self):
        # Drop the test database
        self.collection.delete_many({})

    def test_valid_post_request(self):
        response = self.client.post('/submitform', json={
            "name": "John",
            "identity_number": "1872031902995998",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], "Data successfully inserted.")
    
    def test_duplicate_post_request(self):
        self.collection.insert_one({
            "name": "John",
            "identity_number": "1872031902995998",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        response = self.client.post('/submitform', json={
            "name": "John",
            "identity_number": "1872031902995998",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Duplicate entry detected.")
    
    def test_invalid_identity_number_length(self):
        response = self.client.post('/submitform', json={
            "name": "John",
            "identity_number": "12345",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Identity number must be 16 digits and all numerical.")
    
    def test_invalid_identity_number_non_numeric(self):
        response = self.client.post('/submitform', json={
            "name": "John",
            "identity_number": "12345ABCDE123456",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Identity number must be 16 digits and all numerical.")
    
    def test_identity_number_date_of_birth_mismatch(self):
        response = self.client.post('/submitform', json={
            "name": "John",
            "identity_number": "1999021700123456",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Identity number does not match the date of birth.")
    
    def test_empty_fields(self):
        response = self.client.post('/submitform', json={
            "name": "",
            "identity_number": "",
            "date_of_birth": "",
            "email": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "All fields must be provided.")
    
    def test_invalid_name(self):
        response = self.client.post('/submitform', json={
            "name": "John123",
            "identity_number": "1999021900123456",
            "date_of_birth": "1999-02-19",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Name must contain only alphabets.")
    
    def test_invalid_date_of_birth_format(self):
        response = self.client.post('/submitform', json={
            "name": "John",
            "identity_number": "1999021900123456",
            "date_of_birth": "19-02-1999",
            "email": "febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Date of birth must be in the format YYYY-MM-DD.")

if __name__ == '__main__':
    unittest.main()
