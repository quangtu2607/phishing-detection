msg = {
    "content": document.body.innerHTML,
    "url": document.URL
}

chrome.runtime.sendMessage(msg);
