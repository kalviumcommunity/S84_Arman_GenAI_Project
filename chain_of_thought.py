from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY_HERE")  # Replace with your API key

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Song Suggester.
When recommending a song:
1. Think step by step (analyze user request).
2. Narrow down possible songs.
3. Then give the final recommendation in this format:
   🎵 Title - Artist (Year)
   Genre: <genre>
   Short Description
"""

# --- USER PROMPT ---
user_prompt = "Suggest me a relaxing acoustic song that has meaningful lyrics for a calm evening."

# --- FULL PROMPT (explicitly ask for reasoning) ---
full_prompt = system_prompt + "\nUser: " + user_prompt + "\nShow your reasoning step by step before the final answer."

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🧠 Chain of Thought Reasoning:\n")
print(response.text)
