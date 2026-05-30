"""Reusable API response format utility helpers"""
from typing import Any, Optional
from fastapi.responses import JSONResponse


def success_response(data: Any = None, status_code: int = 200) -> JSONResponse:
    """Format and return standard success envelope"""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "data": data if data is not None else {}
        }
    )


def error_response(message: str, status_code: int = 400) -> JSONResponse:
    """Format and return standard error envelope"""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message
        }
    )
