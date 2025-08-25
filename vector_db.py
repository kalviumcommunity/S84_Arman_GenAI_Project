from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

kb = [
    {"symptom": "cough", "remedy": "Tulsi tea with honey"},
    {"symptom": "fever", "remedy": "Giloy juice"},
    {"symptom": "headache", "remedy": "Apply sandalwood paste"},
    {"symptom": "indigestion", "remedy": "Ginger and lemon tea"},
    {"symptom": "stress", "remedy": "Ashwagandha powder with milk"}
]

corpus = [item["symptom"] for item in kb]
vectorizer = TfidfVectorizer().fit(corpus)
kb_vectors = vectorizer.transform(corpus)

def search_knowledge_base(query, top_k=2):
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, kb_vectors).flatten()
    ranked = sims.argsort()[::-1][:top_k]
    return [kb[i] for i in ranked]
