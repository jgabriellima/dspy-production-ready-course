"""
Helper module for setting up observability and environment configuration.
This module provides a single function to initialize all observability tools.
"""

from dotenv import load_dotenv
from langfuse import get_client
from openinference.instrumentation.dspy import DSPyInstrumentor


def setup_observability():
    """
    Initialize environment variables, Langfuse client, and DSPy instrumentation.
    
    This function:
    1. Loads environment variables from .env file
    2. Initializes and verifies Langfuse client
    3. Instruments DSPy for OpenInference tracing
    
    Returns:
        langfuse: The initialized Langfuse client
    """
    # Load environment variables
    load_dotenv()
    
    # Initialize Langfuse client
    langfuse = get_client()
    
    # Verify connection
    if langfuse.auth_check():
        print("Langfuse client is authenticated and ready!")
    else:
        print("Authentication failed. Please check your credentials and host.")
    
    # Enable Tracing for DSPy
    DSPyInstrumentor().instrument()
    
    return langfuse

