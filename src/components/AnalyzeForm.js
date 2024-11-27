import React, { useState } from 'react';
import axios from 'axios';

const AnalyzeForm = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    try {
      setError(null);  // Clear previous errors
      const response = await axios.post('http://127.0.0.1:5000/api/analyze', { url });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    }
  };

  return (
    <div>
      <h1>Advertising Analytics Dashboard</h1>
      <input
        type="text"
        placeholder="Enter website URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button onClick={handleAnalyze}>Analyze</button>

      {error && <p style={{ color: 'red' }}>{error}</p>}
      {result && (
        <div>
          <h2>Analysis Results:</h2>
          <p><strong>URL:</strong> {result.url}</p>
          <p><strong>SEO Score:</strong> {result.seo_score}</p>
          <p><strong>Advertising Platforms:</strong> {result.ads_platforms.join(', ')}</p>
          <p><strong>Issues:</strong> {result.issues.join(', ')}</p>
        </div>
      )}
    </div>
  );
};

export default AnalyzeForm;