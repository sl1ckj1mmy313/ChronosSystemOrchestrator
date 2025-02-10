from pydantic import BaseModel
from typing import Optional, List, Dict

class TimeResponse(BaseModel):
    """
    Represents a response from the Chronos Time API.
    """
    chronos_time: float  # The current Chronos cunix time
    timestamp: float     # Local timestamp when the time was fetched

class BalanceResponse(BaseModel):
    """
    Represents a user's balance along with its display in Chronos Time Units.
    """
    balance: float       # Raw Chronos Currency (C₡) balance
    t_units: str         # Display value in T‑Units (e.g., "T⦀24" for one month)

class Transaction(BaseModel):
    """
    Represents a currency transaction request.
    """
    sender: str
    receiver: str
    amount: float
    timestamp: float     # The time when the transaction was initiated

class TransactionRecord(BaseModel):
    """
    Represents the record returned by the blockchain after processing a transaction.
    """
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    timestamp: float
    status: str          # e.g., "success", "failed"

class PeerInfo(BaseModel):
    """
    Represents information about a discovered peer.
    """
    ip: str
    port: int
    supports_mtls: bool

class NetworkStatus(BaseModel):
    """
    Represents the status of the network as provided by the Chronos Network API.
    """
    node: Dict[str, str]     # e.g., {"hostname": "dummy_server", "ip": "7f000001", "port": "8443"}
    peer_count: int
    peers: List[PeerInfo]

class AIMetrics(BaseModel):
    """
    Represents AI-generated insights or metrics.
    """
    insights: Dict[str, float]
    timestamp: float
