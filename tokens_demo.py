import tiktoken  # pip install tiktoken

# Initialize tokenizer (GPT-3.5/GPT-4 tokenizer works similarly for demo)
tokenizer = tiktoken.get_encoding("cl100k_base")

# Example prompts (Song Suggester)
prompt1 = "Suggest me a relaxing acoustic song."
prompt2 = "Suggest me a romantic pop song by Taylor Swift with heartfelt lyrics and a soothing melody."

# Tokenize
tokens1 = tokenizer.encode(prompt1)
tokens2 = tokenizer.encode(prompt2)

print("Prompt 1:", prompt1)
print("Tokens:", tokens1)
print("Token count:", len(tokens1))

print("\nPrompt 2:", prompt2)
print("Tokens:", tokens2)
print("Token count:", len(tokens2))
