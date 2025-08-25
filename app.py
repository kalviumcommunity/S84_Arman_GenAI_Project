import streamlit as st
import json
from model import generate_response
from vector_db import search_knowledge_base

st.title("🌿 Ayurvedic Medicine Recommender")

query = st.text_input("Enter your symptom or condition")

if query:
    docs = search_knowledge_base(query, top_k=3)
    response = generate_response(query, docs)
    st.json(response)
