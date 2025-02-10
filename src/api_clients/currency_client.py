import os
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')


class CurrencyClient:
    """
    Client for the Chronos Currency API.
    Provides methods to retrieve user balances and process currency transactions.
    """

    def __init__(self, base_url: str = None):
        """
        Initialize the CurrencyClient.

        The base_url is loaded from the environment variable CURRENCY_API_URL if not provided.
        """
        self.base_url = base_url or os.getenv("CURRENCY_API_URL", "https://chronoscurrency.example.com")
        logging.info(f"CurrencyClient configured with base URL: {self.base_url}")

    def get_balance(self, user_id: str) -> dict:
        """
        Retrieve the balance for a given user.

        Expects a JSON response in the form:
            {"balance": <numeric_balance>, "t_units": "<time_unit_representation>"}

        Returns:
            A dictionary with the user's balance and T‑Unit display.

        Raises:
            Exception: if the request fails.
        """
        try:
            url = f"{self.base_url}/balance?user_id={user_id}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            balance_data = response.json()
            logging.info(f"Fetched balance for {user_id}: {balance_data}")
            return balance_data
        except Exception as e:
            logging.error(f"Failed to get balance for user {user_id}: {e}")
            raise

    def process_transaction(self, transaction_data: dict) -> dict:
        """
        Process a currency transaction via the Chronos Currency API.

        Expects a POST endpoint that processes the transaction and returns a transaction record.

        Args:
            transaction_data: A dictionary containing transaction details.

        Returns:
            A dictionary with the transaction record and status.

        Raises:
            Exception: if the transaction processing fails.
        """
        try:
            url = f"{self.base_url}/transaction"
            response = requests.post(url, json=transaction_data, timeout=5)
            response.raise_for_status()
            tx_data = response.json()
            logging.info(f"Processed transaction: {tx_data}")
            return tx_data
        except Exception as e:
            logging.error(f"Failed to process transaction: {e}")
            raise


# Standalone demo
if __name__ == "__main__":
    client = CurrencyClient()

    # Demo: Get balance for a dummy user.
    try:
        balance = client.get_balance("user123")
        print(f"Balance for user123: {balance}")
    except Exception as e:
        print(f"Error fetching balance: {e}")

    # Demo: Process a dummy transaction.
    try:
        transaction = {
            "sender": "user123",
            "receiver": "user456",
            "amount": 50,
            "timestamp": 1234567890.0
        }
        tx_record = client.process_transaction(transaction)
        print(f"Transaction record: {tx_record}")
    except Exception as e:
        print(f"Error processing transaction: {e}")
