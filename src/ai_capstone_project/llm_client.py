import ollama

MODEL_NAME = "llama3.2"

def generate(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content":" You are a marketing copywriter who writes short, clear ad copy."},
            {"role": "user", "content":prompt},
        ],
    )
    return response["message"]["content"]
if __name__ == "__main__":
    print(generate("Write a two sentence ad for a coffee shop named Bloom and Brunch."))