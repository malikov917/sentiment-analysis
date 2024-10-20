from flask import Flask, request, jsonify

from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the sentiment-analysis pipeline with mBERT
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json  # Get JSON data from the request
    text = data.get('text', '')  # Extract the text from the JSON
    if text:
        # Run sentiment analysis
        result = sentiment_pipeline(text)
        return jsonify(result), 200  # Return the result as JSON
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013)  # Run the app on port 5000
