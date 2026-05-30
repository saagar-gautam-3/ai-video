"""Custom application exceptions hierarchy"""

class AppException(Exception):
    """Base exception for all custom application errors"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class DatabaseException(AppException):
    """Exception raised for database operations errors"""
    def __init__(self, message: str = "Database operation failed", status_code: int = 500):
        super().__init__(message, status_code)


class ValidationException(AppException):
    """Exception raised for input validation errors"""
    def __init__(self, message: str = "Validation error", status_code: int = 400):
        super().__init__(message, status_code)


class NotFoundException(AppException):
    """Exception raised when a resource is not found"""
    def __init__(self, message: str = "Resource not found", status_code: int = 404):
        super().__init__(message, status_code)


class AuthenticationException(AppException):
    """Exception raised for authentication failure"""
    def __init__(self, message: str = "Authentication failed", status_code: int = 401):
        super().__init__(message, status_code)


class ForbiddenException(AppException):
    """Exception raised for unauthorized access"""
    def __init__(self, message: str = "Permission denied", status_code: int = 403):
        super().__init__(message, status_code)
