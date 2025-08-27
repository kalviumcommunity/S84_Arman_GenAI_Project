from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY")

# --- SYSTEM PROMPT (role of AI) ---
system_prompt = """
You are an AI Song Suggester.
Recommend songs based only on the user query.
Always provide song title, artist, release year, and a short explanation.
"""

# --- USER PROMPT (zero-shot: no examples given) ---
user_prompt = "Suggest me a fantasy-themed song with powerful vocals."

# Combine prompts
full_prompt = system_prompt + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎵 Zero-Shot Suggestion:", response.text)
