from fastapi import FastAPI

app = FastAPI()

_count = 0

@app.get("/count")
def count():
    global _count
    return {"count": _count}


