chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'extract_product') {
    // Better extraction for common e-commerce sites
    let title = document.title;
    let price = 'Unknown';
    let url = window.location.href;

    // Try to find price more robustly
    const priceSelectors = [
      '.a-price .a-offscreen', // Amazon
      '.product-price-value', // AliExpress
      '[data-price-container]', // Some Shopify sites
      '.price-wrapper', // Some Magento/WooCommerce sites
      '.price',
      '#price'
    ];

    for (const selector of priceSelectors) {
      const element = document.querySelector(selector);
      if (element) {
        price = element.innerText.trim();
        break;
      }
    }

    // Fallback regex search in the whole body if price not found by selector
    if (price === 'Unknown') {
      const priceRegex = /\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?/;
      const match = document.body.innerText.match(priceRegex);
      if (match) {
        price = match[0];
      }
    }

    const product = { title, price, url };
    sendResponse({ product });
  }
  return true;
});
