from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# --- FUNCTION TO BUILD DYNAMIC PROMPT ---
def build_prompt(genre=None, artist=None, mood=None):
    system_prompt = """
    You are an AI Song Suggester.
    Recommend songs in this format:
    Title - Artist (Year) - Genre
    Short Description
    """
    
    # Dynamically create user request
    user_prompt = "Suggest me a song"
    if genre:
        user_prompt += f" in the {genre} genre"
    if artist:
        user_prompt += f" by {artist}"
    if mood:
        user_prompt += f" that matches a {mood} mood"
    user_prompt += "."
    
    return system_prompt + "\nUser: " + user_prompt


# --- EXAMPLE RUNS ---
# Example 1: Genre + Artist
prompt1 = build_prompt(genre="pop", artist="Taylor Swift")

# Example 2: Genre + Mood
prompt2 = build_prompt(genre="rock", mood="energetic")

# Example 3: Only Mood
prompt3 = build_prompt(mood="relaxing")

# Call Gemini for each
for p in [prompt1, prompt2, prompt3]:
    response = client.models.generate_content(
        model="gemini-pro",
        contents=p
    )
    print("\n🎵 Suggestion:", response.text)
