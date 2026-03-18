chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'analyze_product') {
    // URL of the backend API (using local for development, would be https://... in production)
    const api_url = 'http://localhost:8000/analyze';

    fetch(api_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request.product),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      sendResponse(data);
    })
    .catch(error => {
      console.error('Error:', error);
      sendResponse({
        recommendation: "Analysis unavailable",
        market_insight: "Could not connect to the AI analysis server. Make sure the API is running."
      });
    });

    return true; // Keep the message channel open for async response
  }
  return false; // No response for other actions
});
