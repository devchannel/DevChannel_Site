var express = require('express');
var bodyParser = require('body-parser');
var spawn = require('child_process').spawn;

var app = express();

app.use(bodyParser());

app.get('/', function(req, res){
	console.log('Request');
	res.sendFile(__dirname + '/static/index.html');
	app.use('/', express.static(__dirname + '/static/'));
});


app.post('/join', function(req, res){
	console.log('Post')
	var country = req.body.country;
	var email = req.body.email;
	var p_langs = req.body.p_langs;
	console.log("Email: " + email);
	console.log("Country: " + country);
	console.log("Programing langs: " + p_langs);

	// pass to python script
	var foo = spawn('python3', ['main.py', email, country, p_langs]);
	var str = '';
	foo.stdout.on('data', function(data){ str += data.toString();});
	foo.stdout.on('end', function() {
		console.log(str);
		res.send(str);
	});
})

server = app.listen(3000);
console.log('Server running at port 3000')
