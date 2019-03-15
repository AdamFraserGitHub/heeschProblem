var socket = io('/CDC');

var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var scrWidth = canvas.width = 500;
var scrHeight = canvas.height = 500;

var colors = ['rgb(255,0,0)','rgb(255,150,0)','rgb(255,255,0)','rgb(0,255,0)', 'rgb(0,255,255)', 'rgb(0,0,255)', 'rgb(150,0,255)', 'rgb(255,0,255)'];

var center = {x:scrWidth / 2, y:scrHeight / 2}
var scale = 200;

socket.on('startShape', function(data) {
    ctx.fillStyle = 'rgb(255,255,255)'
    ctx.fillRect(0,0,scrWidth,scrHeight);
    pointNormal = [data.pointsx, data.pointsy]
    drawShape(pointNormal);
});

socket.on('newPoints', function(data) {
    pointsOther = [data.pointsx, data.pointsy]
    drawShape(pointsOther);
})

function drawShape(points) {
    ctx.beginPath()
        ctx.moveTo(center.x + scale*points[0][0], center.y + scale*points[1][0]);
        for(var i = 1; i < points[0].length; i++) {
            ctx.lineTo(center.x + scale*points[0][i], center.y + scale*points[1][i]);
            ctx.moveTo(center.x + scale*points[0][i], center.y + scale*points[1][i]);
        }
        ctx.lineTo(center.x + scale*points[0][0], center.y + scale*points[1][0]);
        
        ctx.stroke()
    ctx.closePath()

    for(var i = 0; i < points[0].length; i++) {
        ctx.beginPath()
            ctx.fillStyle = colors[i];
            ctx.arc(center.x + scale*points[0][i], center.y + scale*points[1][i], 5, 0, Math.PI * 2);
            ctx.fill();
        ctx.closePath()
    }
}
