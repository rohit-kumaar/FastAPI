from fastapi import FastAPI, Request

app = FastAPI(
    title="Fast Api Foundation",
    description="Foundation Description",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

@app.get("/")
def read_root():
    """Root endpoint - Default"""
    return {
        "message" : "Welcome to FastAPI Foundation",
        "status" : "healty"
    }

@app.get("/debug/request-info")
async def request_info(request : Request):
    """Inspect the raw request object"""
    return {
        "method" : request.method,
        "url" : str(request.url),
        "headers" : dict(request.headers),
        "path_params" : request.path_params,
        "query_params" : dict(request.query_params)
    }

@app.get(
    "/orders/active",
    summary="Get Active Orders",
    description="Retrieve a list of currently active and processing orders.",
    tags=["Orders"],
    response_description="List of active orders with their current status",
    deprecated=False
)
def get_active_orders():
    """Endpoint to retrieve all active orders (deprecated in favor of /orders/v2/active)."""
    return {
        "orders": [
            {"order_id": 101, "item": "Laptop", "status": "processing"},
            {"order_id": 102, "item": "Headphones", "status": "shipped"}
        ],
        "count": 2
    }

