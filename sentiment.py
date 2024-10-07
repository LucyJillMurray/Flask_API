from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API!"

@app.route('/analyse', methods=['POST'])
def analyse():
    if request.is_json:
        data = request.get_json()
        text = data.get('text')
        if text:
            # Preprocess the text (remove leading/trailing spaces and convert to lowercase)
            preprocessed_text = text.strip().lower()
            
            # Perform sentiment analysis using the transformers pipeline
            result = sentiment_pipeline([preprocessed_text])
            
            # Return the result as a JSON response
            return jsonify(result), 200
        else:
            return jsonify({"error": "No text provided in the JSON body"}), 400
    else:
        return jsonify({"error": "Request content-type must be application/json"}), 400

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000
    app.run(host='0.0.0.0', port=5000)
