import functools
import logging
import traceback
from typing import Callable, Any

def log_and_handle_exception(func: Callable) -> Callable:
    """
    Decorator to log and handle exceptions in async functions.
    
    Args:
        func (Callable): Function to wrap
    
    Returns:
        Callable: Wrapped function with exception handling
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            logger.error(traceback.format_exc())
            raise
    return wrapper

def retry(max_attempts: int = 3, delay: int = 1):
    """
    Decorator to retry a function with exponential backoff.
    
    Args:
        max_attempts (int): Maximum number of retry attempts
        delay (int): Initial delay between retries
    
    Returns:
        Callable: Wrapped function with retry mechanism
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            import asyncio
            
            logger = logging.getLogger(func.__module__)
            attempts = 0
            
            while attempts < max_attempts:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Function {func.__name__} failed after {max_attempts} attempts")
                        raise
                    
                    wait_time = delay * (2 ** attempts)
                    logger.warning(
                        f"Attempt {attempts} failed: {e}. "
                        f"Retrying in {wait_time} seconds..."
                    )
                    await asyncio.sleep(wait_time)
        
        return wrapper
    return decorator

class CustomException(Exception):
    """
    Base custom exception for the RAG project.
    """
    def __init__(self, message: str, error_code: int = 500):
        """
        Initialize custom exception.
        
        Args:
            message (str): Error message
            error_code (int, optional): HTTP-like error code
        """
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self):
        return f"Error {self.error_code}: {self.message}"
