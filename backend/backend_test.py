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
        # Connect to the test database
        self.mongo_client = MongoClient(os.getenv('MONGODB_URL'))
        self.db = self.mongo_client['data']
        self.collection = self.db['users']
        self.collection.delete_many({})  # Clear the collection before each test

    def tearDown(self):
        # Drop the test database
        self.collection.delete_many({})

    def test_valid_post_request(self):
        response = self.client.post('/submitform', json={
            "name": "John K",
            "identity_number": "1972031902990500",
            "date_of_birth": "1999-02-19",
            "email":"febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], "Data successfully inserted.")
    
    def test_duplicate_post_request(self):
        self.collection.insert_one({
            "name": "John K",
            "identity_number": "1972031902990500",
            "date_of_birth": "1999-02-19",
            "email":"febrian@ieee.org"
        })
        response = self.client.post('/submitform', json={
            "name": "John K",
            "identity_number": "1972031902990500",
            "date_of_birth": "1999-02-19",
            "email":"febrian@ieee.org"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Duplicate entry detected.")
    
    def test_invalid_identity_number_length(self):
        response = self.client.post('/submitform', json={
            "name": "John K",
            "identity_number": "12345",
            "date_of_birth": "19-02-1999"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Identity number must be 16 digits and all numerical.")
    
    def test_invalid_identity_number_non_numeric(self):
        response = self.client.post('/submitform', json={
            "name": "John K",
            "identity_number": "12345ABCDE123456",
            "date_of_birth": "19-02-1999"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Identity number must be 16 digits and all numerical.")
    
    def test_identity_number_date_of_birth_mismatch(self):
        response = self.client.post('/submitform', json={
            "name": "John K",
            "identity_number": "1972031702990511",
            "date_of_birth": "19-02-1999"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Identity number does not match the date of birth.")

if __name__ == '__main__':
    unittest.main()
