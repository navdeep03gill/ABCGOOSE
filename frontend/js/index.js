const express = require('express');
const app = express();
const http = require('http');
const { SocketAddress } = require('net');
const server = http.createServer(app);
const {Server} = require("socket.io");
const io = new Server(server);

let messages =[]

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

server.listen(3000, () => {
    console.log("Listening on *:3000");
});

io.on('connection', (socket) => {
    console.log("User connected");

    socket.on('send message', (msg) => {
        console.log("Recieved message:" + msg);
        io.emit('send message', msg);
    });
});
