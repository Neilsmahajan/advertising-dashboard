# Advertising Dashboard

This project is a web-based advertising analytics dashboard designed for Vloe, a Montreal-based advertising agency. The dashboard analyzes and provides insights into clients' advertising and SEO efforts by simply entering a website URL.

## Features
- Analyze website SEO performance
- Integrate advertising platforms like Google Ads, Facebook Ads, and Bing Ads
- Localization support for French and English
- Exportable and visually appealing analytics reports
- Screenshot or scrape data from advertising platforms:
  - Google Analytics
  - LinkedIn
  - Pinterest
  - X (formerly Twitter)
  - Meta (Facebook and Instagram Ads)
  - Mailchimp
  - Cyberimpact
  - TikTok
  - Snapchat
  - Bing
  - Google Ads
  - Google Merchant Center
  - Google Tag Manager

## Technology Stack
- **Frontend**: React.js (with i18next for localization)
- **Backend**: Flask (Python)
- **Database**: PostgreSQL or MongoDB
- **Hosting**: AWS, Azure, or Heroku

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Neilsmahajan/advertising-dashboard.git
   ```
   cd advertising-dashboard
2. Install dependencies:
    ```bash
    npm install --legacy-peer-deps
    ```
3. Start the frontend development server:
    ```bash
    npm start
    ```
4. Install dependencies for the backend:
    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    pip install -r requirements.txt
    ```
5. Run the backend server (Python):
    ```bash
    python app.py
    ```
6. To deploy the backend for production:
    ```bash
    gunicorn -w 4 -b 0.0.0.0:5000 app:app
    ```
7. To build the frontend for production:
    ```bash
    npm run build
    ```
## Planned Enhancements
- Add the ability to scrape or take screenshots of advertising platform dashboards.
- Automate authentication and API integration for supported advertising platforms.
- Generate and download PDF reports with combined analytics and screenshots.

## Contact
  
**Neil Mahajan**<br>
Email: nsmahaj1@asu.edu<br>
Personal Email: neilsmahajan@gmail.com<br>
LinkedIn: [Neil Mahajan](https://www.linkedin.com/in/neil-mahajan/)<br>