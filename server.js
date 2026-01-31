const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: { origin: "*" },
  maxHttpBufferSize: 1e7
});

const PORT = 3000;

app.use(express.static(__dirname));

io.on("connection", (socket) => {
  console.log("🌐 Dashboard connected");

  socket.on("pi_frame", (frame) => {
    socket.broadcast.emit("camera_frame", frame);
  });
});

server.listen(PORT, "0.0.0.0", () =>
  console.log(`🚀 Dashboard running at http://localhost:${PORT}`)
);
