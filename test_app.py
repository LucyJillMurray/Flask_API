import unittest
import json
from sentiment import app

class SentimentAnalysisTestCase(unittest.TestCase):
    
    def setUp(self):
        # Set up a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_route(self):
        """Test the home route"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to the Sentiment Analysis API!")
    
    def test_analyse_route_with_text(self):
        """Test the /analyse route with valid text"""
        sample_text = {"text": "I love this!"}
        response = self.app.post('/analyse', 
                                 data=json.dumps(sample_text),
                                 content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn("label", data[0])  # Should contain a "label" key
        self.assertIn("score", data[0])  # Should contain a "score" key
    
    def test_analyse_route_no_text(self):
        """Test the /analyse route with missing text in the JSON"""
        response = self.app.post('/analyse', 
                                 data=json.dumps({}),  # No text provided
                                 content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertEqual(data["error"], "No text provided in the JSON body")
    
    def test_analyse_route_invalid_content_type(self):
        """Test the /analyse route with invalid content type"""
        sample_text = {"text": "This is awesome!"}
        response = self.app.post('/analyse', 
                                 data=json.dumps(sample_text),
                                 content_type='text/plain')  # Invalid content type
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertEqual(data["error"], "Request content-type must be application/json")

if __name__ == '__main__':
    unittest.main()
