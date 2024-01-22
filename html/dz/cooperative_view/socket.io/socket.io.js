const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

app.use(express.static('public'));

io.on('connection', (socket) => {
    socket.on('pause', () => {
        io.emit('pause');
    });

    socket.on('play', () => {
        io.emit('play');
    });

    socket.on('seeked', (time) => {
        io.emit('seeked', time);
    });
});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

server.listen(3000);
