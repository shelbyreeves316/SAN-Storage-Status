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
    # Run the FastAPI application directly instead of relying on module
    # string resolution. This avoids import errors when executing the script
    # with `python backend/app/main.py`.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8100, reload=True)