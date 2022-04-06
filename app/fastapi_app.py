from typing import Awaitable, Callable, Union

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.v1.router import api_router
from app.exceptions import BusinessException

app = FastAPI(
    title="Well API",
    openapi_url="/v1/openapi.json",
)

app.include_router(api_router, prefix="/v1")


@app.middleware("http")
async def errors_handling(
    request: Request, call_next: Callable
) -> Union[Awaitable, JSONResponse]:
    try:
        return await call_next(request)
    except BusinessException as e:
        return JSONResponse(status_code=422, content={"msg": str(e)})
