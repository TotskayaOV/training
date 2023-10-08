const grabBtn = document.getElementById("grabBtn");
grabBtn.addEventListener("click",() => {    
    chrome.tabs.query({active: true}, (tabs) => {
        const tab = tabs[0];
        if (tab) {
            chrome.scripting.executeScript(
                {
                    target:{tabId: tab.id, allFrames: true},
                    func:grabImages
                }
            )
        } else {
            alert("There are no active tabs")
        }
    })
})


function grabImages() {
  let i = 0;
  const intervalId = setInterval(() => {
    const element = document.querySelector("#root > div > div > div > section > section > main > div > div > div > div.ant-row.ant-row-space-between.partners-actions > div:nth-child(1) > button:nth-child(2)",
      document,
      null,
      XPathResult.FIRST_ORDERED_NODE_TYPE,
      null
    ).singleNodeValue;
    
    if (element) {
      element.click();
      i++;
      if (i >= 1000) {
        clearInterval(intervalId); 
      }
    }
  }, 1000); 
}