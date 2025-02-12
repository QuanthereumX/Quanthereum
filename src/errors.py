# errors.py - Custom exceptions for QuanthereumX
# Author: Przemek Buczek

class DatabaseConnectionError(Exception):
    """Raised when the database connection fails."""
    def __init__(self, message="Failed to connect to the database"):
        self.message = message
        super().__init__(self.message)

class InvalidConfigurationError(Exception):
    """Raised when an invalid configuration is detected."""
    def __init__(self, message="Invalid configuration detected"):
        self.message = message
        super().__init__(self.message)

class ServiceUnavailableError(Exception):
    """Raised when a service is unavailable."""
    def __init__(self, message="Service is currently unavailable"):
        self.message = message
        super().__init__(self.message)

# Example usage
if __name__ == "__main__":
    try:
        raise DatabaseConnectionError()
    except DatabaseConnectionError as e:
        print(f"⚠️ {e}") 
