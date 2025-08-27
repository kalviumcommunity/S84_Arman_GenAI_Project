🎵 AI Song Suggester with RAG + Gemini LLM
📌 Project Idea

The AI Song Suggester is an intelligent system that recommends songs based on user preferences such as genre, artist, mood, or theme.
It uses RAG (Retrieval-Augmented Generation) to fetch relevant information from a song dataset and Google Gemini LLM to generate natural language recommendations.

For example:

User: "Suggest me a relaxing lo-fi song for studying."

AI: "I recommend 'Weightless' by Marconi Union — it’s a calming track often used for deep focus and relaxation."

⚙️ Implementation

Dataset: Song metadata (genres, artists, albums, release year, lyrics/themes).

RAG Pipeline:

Retrieve relevant songs from dataset based on user query.

Use Gemini LLM to refine and generate human-like recommendations.

LLM Features:

Zero-shot, one-shot, and few-shot prompting.

Dynamic prompting (based on user context).

Custom temperature & token control for creativity vs. accuracy.

🛠️ Tech Stack

Google Gemini API (LLM for natural language recommendations).

LangChain (for RAG + prompt orchestration).

Custom Song Dataset (for retrieval).

Python (backend).

📚 Assignments Covered

This project includes the following AI/LLM concepts:

System & User Prompts

Zero-Shot Prompting

One-Shot Prompting

Multi-Shot Prompting

Dynamic Prompting

Chain of Thought Prompting

Tokens & Tokenization

Temperature

Top P Sampling

Create Project Readme

🎥 Video Explanation

In the video:

I’ll explain the project idea.

Show how RAG + Gemini is used.

Walk through each assignment implementation.

🚀 Future Work

Add embeddings & vector database (Pinecone / FAISS).

Implement cosine similarity & L2 similarity.

Build a frontend UI for users to interact.