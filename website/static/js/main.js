function get_by_order (){
    url_params = function (){
        var query = window.location.search.substring(1);
        var vars = query.split('&');
        var params = {};
        for (var i in vars){
            var pair = vars[i].split('=');
            params[pair[0]] = decodeURIComponent(pair[1]);
        }
        return params
    }();

    console.log("url params:", url_params);
    console.log("l:", url_params['l'])

    var order = document.getElementById("order_dropdown").value;
    
    req_url = 'members?' + 't=' + Math.random() + '&' + 'order=' + order
    console.log(req_url)

    var xhttp;
    if (window.XMLHttpRequest) {
        xhttp = new XMLHttpRequest();
    } else {
        //code for IE 5 and 6
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var parser = new DOMParser()
            , doc = parser.parseFromString(xhttp.responseText, "text/html");
            var newTable = doc.getElementsByClassName("members_table")[0];
            var oldTable = document.getElementsByClassName("members_table")[0];
            oldTable.parentNode.replaceChild(newTable, oldTable)
            console.log(newTable);
        }
    }


    xhttp.open('GET', req_url, true);
    xhttp.send();

    return true;
}
