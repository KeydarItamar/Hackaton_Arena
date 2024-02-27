from fastapi import FastAPI
from client import getLocNum  # Import the getLocNum function

app = FastAPI()

@app.get("/getUbiByNum/{num}")
async def read_root(num: str):
    try:
        location = await getLocNum(num)
        return location
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
