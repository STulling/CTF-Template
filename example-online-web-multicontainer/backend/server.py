from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/flag")
def get_flag():
    return {"flag": os.getenv("FLAG", "FLAG{default_flag}")}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)