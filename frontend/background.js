//for listening any message which comes from runtime
chrome.runtime.onMessage.addListener(messageReceived);

function messageReceived(msg) {
   // Do your work here
   console.log(msg);
   const url = 'http://127.0.0.1:8000/phishing/get_url';
   const options = {
   method: 'POST',
   headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=UTF-8'
   },
   body: JSON.stringify({
      url: msg,
   })
   };

   fetch(url, options)
   .then(response => {
      console.log(response.status);
   });
}