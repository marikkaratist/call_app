from fastapi import FastAPI
from call_api.router import router as router_call

app = FastAPI(
    title="Calling App"
)

app.include_router(router_call)

