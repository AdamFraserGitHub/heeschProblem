var express = require('express');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);
var bodyParser = require('body-parser')
var path = require('path');

// var seedShape = {
//     name: "square",
//     points: [[-0.5, 0.5, 0.5, -0.5],[-0.5, -0.5, 0.5, 0.5]],
// }

var clientDataChannel = io.of('/CDC');

clientDataChannel.on('connection', function(socket) {
    console.log("client connected!");
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use('/', express.static('public'))

app.post('/baseShape', function(req, res) {
    console.log("base shape recieved")
    clientDataChannel.emit('startShape', {pointsx: req.body.x, pointsy: req.body.y});
    res.send("ok");
});

app.post('/processRotation', function(req, res) {
    console.log("rotated shape recieved")
    clientDataChannel.emit('newPoints', {pointsx: req.body.x, pointsy: req.body.y});
    res.send("ok");
});

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, 'public', 'rotSqRend.html'))
});

server.listen(80,'0.0.0.0', function(err) {
    if(err) {
        console.log("you broke the server! GRRR!! (ノಠ益ಠ)ノ彡┻━┻ \n");
    } else {
        console.log("server online!\n... well it might be\nwho knows really?")
    }
});

