import os
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')


class BlockchainClient:
    """
    Client for the Chronos Blockchain API.
    Provides methods to fetch the blockchain state and submit transactions.
    """

    def __init__(self, base_url: str = None):
        """
        Initialize the BlockchainClient.
        The base_url is loaded from the environment variable BLOCKCHAIN_API_URL if not provided.
        """
        self.base_url = base_url or os.getenv("BLOCKCHAIN_API_URL", "https://chronosblockchain.example.com")
        logging.info(f"BlockchainClient configured with base URL: {self.base_url}")

    def get_chain(self) -> dict:
        """
        Retrieve the current blockchain ledger.
        Expects a JSON response, for example: {"chain": [...], "length": <int>}
        """
        try:
            url = f"{self.base_url}/blockchain/chain"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched blockchain data: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to fetch blockchain data: {e}")
            raise

    def submit_transaction(self, transaction_data: dict) -> dict:
        """
        Submit a transaction to the blockchain.
        Expects a POST endpoint that processes the transaction and returns a transaction record.
        """
        try:
            url = f"{self.base_url}/blockchain/transaction"
            response = requests.post(url, json=transaction_data, timeout=5)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Transaction submitted: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to submit transaction: {e}")
            raise


# Standalone demo:
if __name__ == "__main__":
    client = BlockchainClient()
    try:
        chain = client.get_chain()
        print("Blockchain:", chain)
    except Exception as e:
        print("Error fetching blockchain:", e)

    # Dummy transaction demo
    transaction = {
        "sender": "Alice",
        "receiver": "Bob",
        "amount": 50,
        "timestamp": 1234567890.0
    }
    try:
        tx_record = client.submit_transaction(transaction)
        print("Transaction record:", tx_record)
    except Exception as e:
        print("Error submitting transaction:", e)
