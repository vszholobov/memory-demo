from fastapi import FastAPI
import uvicorn
import socket

app = FastAPI()
memory_hog = []

@app.get("/consume")
def consume_memory():
    memory_hog.append(bytearray(10 * 1024 * 1024))  # 10MB
    container_name = socket.gethostname()
    return {
        "message": f"Consumed memory chunks: {len(memory_hog)}",
        "container": container_name
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
