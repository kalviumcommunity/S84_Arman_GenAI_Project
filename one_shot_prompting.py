from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Song Selector.
Always recommend songs in this format:
Song Title - Artist (Year)
Short Description (genre, vibe, or theme)
"""

# --- ONE EXAMPLE (few-shot learning with 1 sample) ---
example = """
Example:
User: Suggest me a sad romantic song.
AI: Someone Like You - Adele (2011)
A heartfelt piano ballad about love and heartbreak, perfect for emotional moments.
"""

# --- USER PROMPT (new request) ---
user_prompt = "Suggest me an energetic party song by David Guetta."

# --- FINAL PROMPT (system + example + user) ---
full_prompt = system_prompt + "\n" + example + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎵 One-Shot Suggestion:", response.text)
