import os
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')


class TimeClient:
    """
    Client for the Chronos Time API.
    Provides a method to fetch the current Chronos cunix time.
    """

    def __init__(self, base_url: str = None):
        """
        Initialize the TimeClient.

        The base_url is loaded from the environment variable TIME_API_URL if not provided.
        """
        # Use provided base_url or load from environment (with a default fallback)
        self.base_url = base_url or os.getenv("TIME_API_URL", "https://chronostime.example.com/chronos/cunix")
        logging.info(f"TimeClient configured with base URL: {self.base_url}")

    def get_current_time(self) -> float:
        """
        Fetch the current Chronos cunix time from the API.
        Expects a JSON response in the form: {"chronos_unix": <timestamp>}.

        Returns:
            The current cunix time as a float.

        Raises:
            Exception: if the request fails or the response is invalid.
        """
        try:
            response = requests.get(self.base_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            # Convert the value to float
            current_time = float(data.get("chronos_unix"))
            logging.info(f"Fetched current Chronos time: {current_time}")
            return current_time
        except Exception as e:
            logging.error(f"Failed to fetch Chronos time: {e}")
            raise


# Standalone demo
if __name__ == "__main__":
    client = TimeClient()
    current_time = client.get_current_time()
    print(f"Current Chronos time: {current_time}")
