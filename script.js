//skillsThis project

function getPage(uri) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //respObj = HTML.parse(xhttp.responseText);
            respObj = xhttp.response;
            return respObj;
        } else {
            return "error";
        }
    };
    xhttp.open("GET", uri, true);
    xhttp.setRequestHeader("Content-type", "text/html");
    xhttp.send();   
}

function runSearch(terms, loc) {
    //echo the search terms
    document.getElementById("results").innerHTML = terms + " - " + loc; 

    /*
    //grab the jobs
    var jobs = document.querySelectorAll('[data-tn-component="organicJob"]');
    for (var i = 0; i < jobs.length; i++) {
        alert(jobs[i].outerHTML);
        //Do something
    }
    
    //next page stuff
    var nextSpan = document.getElementsByClassName("np");
    var nextSpanParent = nextSpan[0].parentNode.parentNode;
    var nextPageLink = nextSpanParent.href;
    */
    //populate the results on the page
    //document.getElementById("results").innerHTML = terms + " - " + loc;     
}

var terms = "Devops Engineer";
var loc = "San Rafael, CA";
var jobIndexUri = encodeURI("https://www.indeed.com/jobs?q=" + terms + "&l=" + loc);
var firstPage = getPage(jobIndexUri)
/*const proxyurl = "https://cors-anywhere.herokuapp.com/";
const url = jobIndexUri; // site that doesn’t send Access-Control-*
fetch(proxyurl + url) // https://cors-anywhere.herokuapp.com/https://example.com
.then(response => response.text())
.then(contents => console.log(contents))
.catch(console.log("Can’t access " + url + " response. Blocked by browser?"))
*/