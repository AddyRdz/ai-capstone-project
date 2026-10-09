
CHANNEL_INSTRUCTIONS = {
    "Email" : "Write a marketing email with a subject line, a short body, and a call to action. Aim for under 50 characters.",
    "Social post" : "Write a short social media post (2-3 sentences). A clear hook in the first line and a call to action, with 3-5 relevant hashtags",
    "Ad Copy" : "Write a short ad with a headline and a one-sentence description."
}

def build_prompt(data):
    rules = CHANNEL_INSTRUCTIONS[data["channel"]]
    return(
        f"Product or service: {data['product']}\n"
        f"Target audience: {data['audience']}\n"
        f"Goal: {data['goal']}\n"
        f"Tone: {data['tone']}\n"
        f"Instructions: {rules}\n"
        f"Do not invent facts, prices, or statistics not provided above."
    )

if __name__ == "__main__":
    data = {"product": "Coffee shop", "audience": "Locals", "goal": "More visits", "channel": "email", "tone": "friendly"}
    print(build_prompt(data))       