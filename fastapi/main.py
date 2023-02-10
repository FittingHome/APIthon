from fastapi import FastAPI, Body, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from celery_worker import create_task



app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/example", status_code=202)
def run_task(data=Body(...)):
    amount = int(data["amount"])
    x, y = data["x"], data["y"]
    task = create_task.delay(amount, x, y)

    return JSONResponse({"Task": task.id})

@app.websocket("/taskstatus")
async def websocket_endpoint(websocket: WebSocket, id):
    await websocket.accept()
    # await manager.connect(websocket)
    try:
        while True:
            json_content = {
                "status" : AsyncResult(id).state
            }
        
            await manager.send_personal_message(json_content, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)