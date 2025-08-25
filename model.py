import json
import random

def generate_response(query, docs):
    # Mocked LLM response (replace with real OpenAI call if needed)
    remedies = [d["remedy"] for d in docs]
    return {
        "query": query,
        "remedies": remedies,
        "notes": "Consult an Ayurvedic practitioner before use."
    }
