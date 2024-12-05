from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import logging

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure logging
logging.basicConfig(filename='backend.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    logging.info(f"Received request for URL: {url}")
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'error': f'Failed to fetch URL. Status code: {response.status_code}'}), 400

        soup = BeautifulSoup(response.text, 'html.parser')

        # SEO Analysis (Example)
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_description = meta_description['content'] if meta_description else 'Missing meta description'

        h1_tags = soup.find_all('h1')
        h1_count = len(h1_tags)

        seo_score = 85  # Placeholder score; refine this with more detailed analysis.

        # Advertising platforms (Placeholder logic)
        ads_platforms = ["Google Ads", "Facebook Ads"]

        result = {
            "url": url,
            "seo_score": seo_score,
            "ads_platforms": ads_platforms,
            "issues": [meta_description, f"{h1_count} H1 tags found"]
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)