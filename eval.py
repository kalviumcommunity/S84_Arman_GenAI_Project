from vector_db import search_knowledge_base
from model import generate_response

eval_data = [
    {"query": "I have cough", "expected": "Tulsi"},
    {"query": "Fever symptoms", "expected": "Giloy"},
    {"query": "Head is aching", "expected": "sandalwood"}
]

correct = 0
for e in eval_data:
    docs = search_knowledge_base(e["query"], top_k=2)
    resp = generate_response(e["query"], docs)
    if any(e["expected"].lower() in r.lower() for r in resp["remedies"]):
        correct += 1

print(f"Accuracy: {correct}/{len(eval_data)}")
