from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Placeholder logic for URL analysis
    result = {
        "url": url,
        "seo_score": 85,
        "ads_platforms": ["Google Ads", "Facebook Ads"],
        "issues": ["Missing meta description", "No Google Tag Manager"]
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)