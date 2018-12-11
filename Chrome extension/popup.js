
// Call function connect() whenever the page is loaded
document.addEventListener('DOMContentLoaded', connect);

function connect() {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
      if(xhr.readyState === 4 && xhr.status === 200) { //If POST request received sucessfully

        var result = JSON.parse(xhr.responseText);
        neutralPctString = result['Neutral'];
        libPctString = result['Liberal'];
        conPctString = result['Conservative'];
        changeContent('neutral', "Neutral: " + neutralPctString);
        changeContent('liberal', "Liberal: " + libPctString);
        changeContent('conservative', "Conservative: " + conPctString);
        showHideContent("loading");
        maxIdeology(neutralPctString, libPctString, conPctString);
      }
    };

    xhr.open("POST", "http://localhost:5000/classify", true); //set the POST request and the receiving URL
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"url": tabs[0].url})); //Send url of current tab as a JSON object

  

  })
};

// Helper function to change the content of HTML elements
function changeContent(elementId, content) {
  document.getElementById(elementId).textContent = content;
}

// Helper function to show/hide HTML elements
function showHideContent(elementId) {
  showState = document.getElementById(elementId).style.display
  if (showState == "none") {
    document.getElementById(elementId).style.display = "initial"
  } else {
    document.getElementById(elementId).style.display = "none"
  }
}

// Helper function to parse the percentage 
function convertPercentage(percentageString) {
  return parseFloat(percentageString.replace('%', ''));
}

// Helper function that return the dominant political ideology of the article
function maxIdeology(neutralPctString, libPctString, conPctString){
  neutralPct = convertPercentage(neutralPctString);
  libPct = convertPercentage(libPctString);
  conPct = convertPercentage(conPctString);
  maxId = Math.max(neutralPct, libPct, conPct);
  console.log(maxId)
  if (maxId == neutralPct) {
    document.getElementById("neutralPic").style.display = "block";
  } else if (maxId == libPct) {
    document.getElementById("donkey").style.display = "block";
  } else {
    document.getElementById("elephant").style.display = "block";
  }
}

