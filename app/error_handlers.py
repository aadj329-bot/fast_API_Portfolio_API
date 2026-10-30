from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import(ResourceNotFoundError, DuplicateResourceError)


async def resource_not_found_handler(request: Request, exc: ResourceNotFoundError):
    return JSONResponse(status_code=404, content={"message": str(exc)})


async def duplicate_resource_handler(request: Request, exc: DuplicateResourceError):
    return JSONResponse(status_code=409, content={'message': str(exc)})

