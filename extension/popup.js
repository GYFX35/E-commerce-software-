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
          // Clear previous content
          resultDiv.textContent = '';

          // Create elements for Recommendation
          const recTitle = document.createElement('strong');
          recTitle.textContent = 'Recommendation: ';
          const recText = document.createTextNode(analysis.recommendation);

          const br1 = document.createElement('br');
          const br2 = document.createElement('br');

          // Create elements for Market Insight
          const insightTitle = document.createElement('strong');
          insightTitle.textContent = 'Market Insight: ';
          const insightText = document.createTextNode(analysis.market_insight);

          // Append everything
          resultDiv.appendChild(recTitle);
          resultDiv.appendChild(recText);
          resultDiv.appendChild(br1);
          resultDiv.appendChild(br2);
          resultDiv.appendChild(insightTitle);
          resultDiv.appendChild(insightText);
        } else {
          resultDiv.textContent = 'Analysis failed. Please try again.';
        }
      });
    } else {
      resultDiv.textContent = 'Failed to extract product info. Are you on a product page?';
    }
  });
});
