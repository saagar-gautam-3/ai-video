"""Request logging middleware for monitoring API performance"""
import logging
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger("app.middleware.logging")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log details of every incoming HTTP request and response time"""

    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.time()
        
        # Process the request
        try:
            response = await call_next(request)
        except Exception as e:
            # Exceptions will be caught by global handlers, but log failure here too
            process_time = (time.time() - start_time) * 1000
            logger.error(
                f"Request Failed: {request.method} {request.url.path} - "
                f"Error: {str(e)} - Duration: {process_time:.2f}ms"
            )
            raise e
            
        process_time = (time.time() - start_time) * 1000
        
        # Log standard info format
        logger.info(
            f"{request.method} {request.url.path} - "
            f"Status: {response.status_code} - "
            f"Duration: {process_time:.2f}ms"
        )
        
        # Append duration to response header for debugging if desired
        response.headers["X-Process-Time-Ms"] = f"{process_time:.2f}"
        
        return response
