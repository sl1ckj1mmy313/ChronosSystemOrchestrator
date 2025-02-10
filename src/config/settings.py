import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    # API endpoint URLs for external Chronos modules
    TIME_API_URL: str = os.getenv("TIME_API_URL", "https://chronostime.example.com/chronos/cunix")
    CURRENCY_API_URL: str = os.getenv("CURRENCY_API_URL", "https://chronoscurrency.example.com")
    BLOCKCHAIN_API_URL: str = os.getenv("BLOCKCHAIN_API_URL", "https://chronosblockchain.example.com")
    NETWORK_API_URL: str = os.getenv("NETWORK_API_URL", "https://chronosnetwork.example.com")
    AI_API_URL: str = os.getenv("AI_API_URL", "https://chronosai.example.com")

    # Orchestrator and network configuration
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8443"))
    SERVICE_NAME: str = os.getenv("SERVICE_NAME", "_chronos._tcp.local.")
    USE_TLS: bool = os.getenv("USE_TLS", "false").lower() == "true"
    SOCKET_TIMEOUT: float = float(os.getenv("SOCKET_TIMEOUT", "5.0"))

    # TLS settings (for secure communications)
    CERTFILE: str = os.getenv("CERTFILE", "server.crt")
    KEYFILE: str = os.getenv("KEYFILE", "server.key")
    CA_FILE: str = os.getenv("CA_FILE", "ca_cert.pem")

    # Optional encryption key (should be Base64-encoded if provided)
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY", None)


# Create a settings instance for use in the application
settings = Settings()

if __name__ == "__main__":
    # For quick testing: print out the settings
    print("ChronosSystemOrchestrator Settings:")
    print(f"TIME_API_URL: {settings.TIME_API_URL}")
    print(f"CURRENCY_API_URL: {settings.CURRENCY_API_URL}")
    print(f"BLOCKCHAIN_API_URL: {settings.BLOCKCHAIN_API_URL}")
    print(f"NETWORK_API_URL: {settings.NETWORK_API_URL}")
    print(f"AI_API_URL: {settings.AI_API_URL}")
    print(f"HOST: {settings.HOST}")
    print(f"PORT: {settings.PORT}")
    print(f"SERVICE_NAME: {settings.SERVICE_NAME}")
    print(f"USE_TLS: {settings.USE_TLS}")
    print(f"SOCKET_TIMEOUT: {settings.SOCKET_TIMEOUT}")
    print(f"CERTFILE: {settings.CERTFILE}")
    print(f"KEYFILE: {settings.KEYFILE}")
    print(f"CA_FILE: {settings.CA_FILE}")
    print(f"ENCRYPTION_KEY: {settings.ENCRYPTION_KEY}")
