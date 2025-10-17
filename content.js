// Takea-Sponsor-Away - Content Script
// Automatically removes sponsored products on Takealot.com

(function() {
  'use strict';

  // Function to remove sponsored products from the DOM
  function hideSponsoredProducts() {
    // Find all elements with text "Sponsored"
    const allElements = document.querySelectorAll('*');
    let removedCount = 0;

    allElements.forEach(element => {
      // Check if element contains "Sponsored" text
      if (element.textContent.trim() === 'Sponsored' || 
          element.textContent.includes('Sponsored')) {
        
        // Find the product card container (usually a parent element)
        // Takealot uses various container structures, so we'll traverse up
        let productCard = element.closest('[class*="card"]') || 
                         element.closest('[class*="product"]') ||
                         element.closest('article') ||
                         element.closest('[data-ref]');
        
        // Go one more div up to get the outer container
        if (productCard && productCard.parentElement) {
          productCard = productCard.parentElement;
        }
        
        // If we found a container and it hasn't been removed yet
        if (productCard && !productCard.hasAttribute('data-sponsor-removed')) {
          // Mark it first to avoid duplicate processing
          productCard.setAttribute('data-sponsor-removed', 'true');
          
          // Remove immediately
          if (productCard.parentNode) {
            productCard.remove();
          }
          
          removedCount++;
        }
      }
    });

    if (removedCount > 0) {
      console.log(`[Takea-Sponsor-Away] Removed ${removedCount} sponsored products`);
    }
  }

  // Run on initial page load
  hideSponsoredProducts();

  // Set up MutationObserver to watch for dynamically loaded content
  const observer = new MutationObserver((mutations) => {
    // Check if new nodes were added
    let shouldCheck = false;
    
    for (const mutation of mutations) {
      if (mutation.addedNodes.length > 0) {
        shouldCheck = true;
        break;
      }
    }

    if (shouldCheck) {
      hideSponsoredProducts();
    }
  });

  // Start observing the document for changes
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });

  // Also run periodically as a fallback (every 2 seconds)
  setInterval(hideSponsoredProducts, 2000);

  console.log('[Takea-Sponsor-Away] Extension loaded and monitoring for sponsored products. Products will be completely removed from the page.');
})();

