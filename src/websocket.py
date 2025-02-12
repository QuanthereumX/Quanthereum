# websocket.py - Real-time WebSocket server for QuanthereumX
# Author: Przemek Buczek

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import logging

app = FastAPI()

# WebSocket connection manager
class ConnectionManager:
    """Manages WebSocket connections."""
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        """Accept a new WebSocket connection."""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Remove a disconnected WebSocket connection."""
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """Send a message to all connected clients."""
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Handles real-time WebSocket connections."""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"📡 New message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/")
async def get():
    """Returns a simple HTML page for WebSocket testing."""
    return HTMLResponse("""
    <html>
        <head>
            <script>
                var ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) {
                    var log = document.getElementById("log");
                    log.innerHTML += event.data + "<br>";
                };
                function sendMessage() {
                    var input = document.getElementById("message");
                    ws.send(input.value);
                    input.value = "";
                }
            </script>
        </head>
        <body>
            <h1>QuanthereumX WebSocket</h1>
            <input type="text" id="message" placeholder="Type a message">
            <button onclick="sendMessage()">Send</button>
            <div id="log"></div>
        </body>
    </html>
    """)

# Run WebSocket server with: uvicorn src.websocket:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
