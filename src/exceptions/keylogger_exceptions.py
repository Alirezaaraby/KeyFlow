class KeyloggerException(Exception):
    """Base class for all keylogger exceptions."""
    def __init__(self, message: str) -> None:
        super().__init__(f"Keylogger Exception: {message}")


class KeyloggerPermissionException(KeyloggerException):
    """Raised when permission-related issues occur."""
    def __init__(self, message: str = "Permission denied for keylogging.") -> None:
        super().__init__(f"Keylogger Permission Exception: {message}")


class KeyloggerOSException(KeyloggerException):
    """Raised for operating system compatibility issues."""
    def __init__(self, message: str = "Operating system error for keylogging.") -> None:
        super().__init__(f"Keylogger OS Exception: {message}")


class KeyloggerQueueException(KeyloggerException):
    """Raised when there are issues with the queue."""
    def __init__(self, message: str = "Queue operation failed in keylogger.") -> None:
        super().__init__(f"Keylogger Queue Exception: {message}")


class KeyloggerUnexpectedException(KeyloggerException):
    """Raised for any unexpected errors."""
    def __init__(self, message: str = "An unexpected error occurred in keylogger.") -> None:
        super().__init__(f"Keylogger Unexpected Exception: {message}")
