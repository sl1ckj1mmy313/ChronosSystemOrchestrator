from fastapi import APIRouter, HTTPException, Request
import time
import logging

# Import the orchestrator (assumed to be implemented in src/orchestrator/orchestrator.py)
from src.orchestrator.orchestrator import ChronosSystemOrchestrator

# Configure logging for the API layer
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')

router = APIRouter()

# Instantiate the orchestrator
orchestrator = ChronosSystemOrchestrator()

@router.get("/system/time")
def get_time():
    """
    Endpoint to get the current Chronos time.
    """
    try:
        current_time = orchestrator.sync_time()
        return {"chronos_time": current_time, "timestamp": time.time()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/system/balance")
def get_balance(user_id: str):
    """
    Endpoint to retrieve the balance for a given user.
    """
    try:
        balance = orchestrator.get_balance(user_id)
        return balance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/system/transaction")
def process_transaction(transaction: dict):
    """
    Endpoint to process a currency transaction.
    """
    try:
        tx_record = orchestrator.process_transaction(transaction)
        return {"transaction_record": tx_record, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/system/status")
def get_status():
    """
    Endpoint to get the network status.
    """
    try:
        status = orchestrator.get_network_status()
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/system/ai-insights")
def get_ai_insights():
    """
    Endpoint to retrieve AI insights (placeholder until AI module is implemented).
    """
    try:
        insights = orchestrator.get_ai_insights()
        return insights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
