import time
import json
import logging

# Configure logging for the helper module.
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')


def format_timestamp(ts: float) -> str:
    """
    Convert a UNIX timestamp to a human-readable string.

    Args:
        ts (float): A UNIX timestamp (seconds since epoch).

    Returns:
        str: The timestamp formatted as "YYYY-MM-DD HH:MM:SS".
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


def json_response(success: bool, data=None, message: str = "") -> dict:
    """
    Generate a standardized JSON response.

    Args:
        success (bool): Indicates whether the operation was successful.
        data: The data to include in the response (if any).
        message (str): A message to include (for errors or additional info).

    Returns:
        dict: A dictionary formatted with keys "success", "data", "message", and "timestamp".
    """
    return {
        "success": success,
        "data": data,
        "message": message,
        "timestamp": format_timestamp(time.time())
    }


# Example usage for quick testing.
if __name__ == "__main__":
    now = time.time()
    formatted_now = format_timestamp(now)
    logging.info(f"Formatted timestamp: {formatted_now}")

    sample_response = json_response(True, data={"sample": "value"}, message="Operation successful")
    logging.info(f"Sample JSON response: {json.dumps(sample_response, indent=2)}")
