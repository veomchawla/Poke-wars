import uvicorn
from fastapi import FastAPI
from data_resource.mcp_resource import router as data_router
from battle_tool.mcp_tool import router as battle_router

app = FastAPI(
    title="Pokemon MCP Server",
    description="A FastAPI-based MCP interface to simulate Pokémon battles, retrieve data, and explore strategies.",
    version="1.1.1",  # Updated version
    docs_url="/docs",  # Swagger UI endpoint
    redoc_url="/redoc",  # Optional ReDoc docs
)


# Root health check endpoint
@app.get("/", tags=["Health Check"])
async def read_root():
    """
    Basic health check for the server.
    """
    return {"message": "Welcome to the Pokemon MCP Server!", "status": "running"}


# Register routers with clean prefixes
app.include_router(data_router, prefix="/pokemon", tags=["Pokemon Data"])
app.include_router(battle_router, prefix="/battle", tags=["Battle Simulation"])


# Entry point for running locally
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )




