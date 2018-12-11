// When the extension is installed or upgraded ...
chrome.runtime.onInstalled.addListener(function() {
  // Replace all rules ...
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    // With a new rule ...
    chrome.declarativeContent.onPageChanged.addRules([
      {
        // That fires when a page's URL contains a 'g' ...
        conditions: [
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'huffingtonpost.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'theguardian.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'slate.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'npr.org' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'economist.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'nytimes.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'cnn.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'foxnews.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'breitbart.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'theblaze.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'wsj.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'bbc.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'bloomberg.com' },
          }), 
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: 'medium.com' },
          }), 

        ],
        // And shows the extension's page action.
        actions: [ new chrome.declarativeContent.ShowPageAction() ]
      }
    ]);
  });
});
