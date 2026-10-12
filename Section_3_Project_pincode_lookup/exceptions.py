from fastapi import status, Request
from fastapi.responses import JSONResponse


class PinCodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode
        self.detail = f"Pincode '{pincode}' not found"


class InvalidPinCodeError(Exception):
    def __init__(self, pincode: str, detail: str = "Invalid formate"):
        self.pincode = pincode
        self.detail = f"Invalid pincode format: '{pincode}'. Pincode must be 6 digits"



async def pincode_not_found_handler(request: Request, exc: PinCodeNotFoundError):
    return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                    "status": "error",
                    "message": exc.detail,
                    "pincode": exc.pincode
                }
    )        

async def invalid_pincode_handler(request: Request, exc: InvalidPinCodeError):
    return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "error",
                "message": exc.detail,
                "pincode": exc.pincode
            }
    )
