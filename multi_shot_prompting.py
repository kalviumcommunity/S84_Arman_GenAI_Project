from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY")  # Replace with your Gemini API key

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Song Suggester.
Always recommend songs in this format:
Title - Artist (Year) - Genre
Short Description
"""

# --- MULTI-SHOT EXAMPLES ---
examples = """
Example 1:
User: Suggest me a pop song about love.
AI: Shape of You - Ed Sheeran (2017) - Pop
A catchy love-themed pop track with upbeat rhythms and modern vibes.

Example 2:
User: Suggest me a classic rock song with deep meaning.
AI: Bohemian Rhapsody - Queen (1975) - Rock
An iconic masterpiece blending opera, rock, and storytelling.

Example 3:
User: Suggest me a motivational hip-hop song.
AI: Lose Yourself - Eminem (2002) - Hip-Hop
An inspiring rap anthem about seizing opportunities and overcoming fear.
"""

# --- USER PROMPT ---
user_prompt = "Suggest me a sad song about heartbreak."

# --- FINAL PROMPT ---
full_prompt = system_prompt + "\n" + examples + "\nUser: " + user_prompt

# Call Gemini
response = client.models.generate_content(
    model="gemini-pro",
    contents=full_prompt
)

print("🎵 Multi-Shot Suggestion:", response.text)
