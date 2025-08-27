from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY_HERE")  # Replace with your API key

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Song Suggester.
- Your job is to recommend songs based on user preferences.
- Always include the song title, artist, release year, genre, and a short description.
- Keep the tone friendly and concise.
"""

# --- USER PROMPT ---
user_prompt = "Suggest me an energetic pop song by Taylor Swift."

# --- FULL PROMPT (system + user) ---
full_prompt = system_prompt + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎵 Song Suggestion:", response.text)
