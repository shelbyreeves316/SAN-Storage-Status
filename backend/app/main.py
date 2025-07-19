from fastapi import FastAPI
from .routers import volumes, disks

app = FastAPI(title="Btrfs Dashboard API")

app.include_router(volumes.router, prefix="/api/volumes", tags=["volumes"])
app.include_router(disks.router, prefix="/api/disks", tags=["disks"])


@app.get("/")
async def root():
    return {"message": "Btrfs Dashboard API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
