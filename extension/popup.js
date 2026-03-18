document.getElementById('analyze-btn').addEventListener('click', async () => {
  const resultDiv = document.getElementById('result');
  resultDiv.textContent = 'Analyzing product...';

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab) {
    resultDiv.textContent = 'Error: No active tab found.';
    return;
  }

  chrome.tabs.sendMessage(tab.id, { action: 'extract_product' }, (response) => {
    if (chrome.runtime.lastError) {
      resultDiv.textContent = 'Error: ' + chrome.runtime.lastError.message;
      return;
    }

    if (response && response.product) {
      const product = response.product;
      chrome.runtime.sendMessage({ action: 'analyze_product', product: product }, (analysis) => {
        if (chrome.runtime.lastError) {
          resultDiv.textContent = 'Error: ' + chrome.runtime.lastError.message;
          return;
        }

        if (analysis && analysis.recommendation) {
          resultDiv.innerHTML = `<strong>Recommendation:</strong> ${analysis.recommendation}<br><br><strong>Market Insight:</strong> ${analysis.market_insight}`;
        } else {
          resultDiv.textContent = 'Analysis failed. Please try again.';
        }
      });
    } else {
      resultDiv.textContent = 'Failed to extract product info. Are you on a product page?';
    }
  });
});
