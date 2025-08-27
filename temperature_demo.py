from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY")  # Replace with your API key

# --- SYSTEM PROMPT ---
system_prompt = """
You are an AI Song Suggester.
Always recommend songs in this format:
Title - Artist (Year) - Genre
Short Description
"""

# --- USER PROMPT ---
user_prompt = "Suggest me a relaxing acoustic song."

# --- TRY DIFFERENT TEMPERATURES ---
for temp in [0.0, 0.7, 1.0]:
    print(f"\n--- Temperature: {temp} ---")
    response = client.models.generate_content(
        model="gemini-pro",
        contents=system_prompt + "\nUser: " + user_prompt,
        generation_config={"temperature": temp}
    )
    print(response.text)
