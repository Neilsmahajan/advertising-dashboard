from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(filename='backend.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Google Analytics credentials
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'  # Replace with actual path


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

@app.route('/api/google-analytics', methods=['POST'])
def google_analytics():
    try:
        credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        analytics = build('analyticsreporting', 'v4', credentials=credentials)

        # Example request to fetch session data
        body = {
            'reportRequests': [{
                'viewId': 'VIEW_ID',  # Replace with actual View ID
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}]
            }]
        }
        response = analytics.reports().batchGet(body=body).execute()
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/screenshot', methods=['POST'])
def take_screenshot():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        screenshot_path = f"{url.split('//')[-1].split('/')[0]}.png"
        driver.save_screenshot(screenshot_path)
        return jsonify({'message': 'Screenshot taken', 'path': screenshot_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()
    
if __name__ == '__main__':
    app.run(debug=True)