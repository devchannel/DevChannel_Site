function search_lang (){

    var order = document.getElementById("order_dropdown").value;
    var query = document.getElementById("member_search_box").value;

    var req_url = 'members?order=' + order + '&lang=' + encodeURIComponent(query);

    var xhttp;
    if (window.XMLHttpRequest) {
        xhttp = new XMLHttpRequest();
    } else {
        //code for IE 5 and 6
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhttp.onreadystatechange = function() {
        console.log(xhttp.readyState)
        if (xhttp.readyState == 1) {
            var newSpan = document.createElement("span");
            newSpan.id = "load_text";
            newSpan.innerHTML = "Loading...";
            var oldTable = document.getElementsByClassName("members_table")[0];
            oldTable.parentNode.replaceChild(newSpan, oldTable);//this function makes the page scroll to top and I want to stop that, halp pls!
        } else if (xhttp.readyState == 4 && xhttp.status == 200) {
            var parser = new DOMParser()
            , doc = parser.parseFromString(xhttp.responseText, "text/html");
            var newTable = doc.getElementsByClassName("members_table")[0];
            var load_text = document.getElementById("load_text");
            load_text.parentNode.replaceChild(newTable, load_text);
        }
    }

    xhttp.open('GET', req_url, true);
    xhttp.send();

    return true;
}
