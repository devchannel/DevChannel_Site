function get_by_order (){
    url_params = function (){
        var query = window.location.search.substring(1);
        var vars = query.split('&');
        var params = {};
        for (var i in vars){
            var pair = vars[i].split('=');
            params[pair[0]] = decodeURIComponent(pair[1]);
        }
    }();

    document.getElementById("order_dropdown");
    
    req_url = 'members?' + 't=' + Math.random()

    var xhttp;
    if (window.XMLHttpRequest) {
        xhttp = new XMLHttpRequest();
    } else {
        //code for IE 5 and 6
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log(xhttp.responseText.getElementById("order_dropdown"));
        }
    }


    xhttp.open('GET', req_url, true);
    xhttp.send();

    return true;
}
