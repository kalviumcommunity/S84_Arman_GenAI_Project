from google import genai

# Initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY")

system_prompt = """
You are an AI Song Suggester.
Always recommend songs in this format:
Title - Artist (Year) - Genre
Short Description
"""

user_prompt = "Suggest me a fantasy-themed song."

# Try different top_p values
for top_p in [0.1, 0.5, 0.9]:
    print(f"\n--- Top P: {top_p} ---")
    response = client.models.generate_content(
        model="gemini-pro",
        contents=system_prompt + "\nUser: " + user_prompt,
        generation_config={"top_p": top_p}
    )
    print(response.text)
