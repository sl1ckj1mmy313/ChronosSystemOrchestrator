import os
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')


class NetworkClient:
    """
    Client for the Chronos Network API.
    Provides methods to access network-related endpoints such as peer discovery,
    network status, metrics, and resynchronization.
    """

    def __init__(self, base_url: str = None):
        """
        Initialize the NetworkClient.
        The base_url is loaded from the environment variable NETWORK_API_URL if not provided.
        """
        self.base_url = base_url or os.getenv("NETWORK_API_URL", "https://chronosnetwork.example.com")
        logging.info(f"NetworkClient configured with base URL: {self.base_url}")

    def get_peers(self) -> dict:
        """
        Retrieve the list of currently discovered peers.
        Expects a JSON response like: {"peers": [<peer_info>, ...]}
        """
        try:
            url = f"{self.base_url}/network/peers"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched peers: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to get peers: {e}")
            raise

    def get_status(self) -> dict:
        """
        Retrieve the network status, including node information and peer count.
        """
        try:
            url = f"{self.base_url}/network/status"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched network status: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to get network status: {e}")
            raise

    def get_metrics(self) -> dict:
        """
        Retrieve real-time network performance metrics.
        """
        try:
            url = f"{self.base_url}/network/metrics"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched network metrics: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to get network metrics: {e}")
            raise

    def resync_network(self) -> dict:
        """
        Trigger a resynchronization of the network.
        """
        try:
            url = f"{self.base_url}/network/resync"
            response = requests.post(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Network resync initiated: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to resync network: {e}")
            raise


# Standalone demo:
if __name__ == "__main__":
    client = NetworkClient()
    try:
        peers = client.get_peers()
        print("Peers:", peers)
    except Exception as e:
        print("Error fetching peers:", e)
