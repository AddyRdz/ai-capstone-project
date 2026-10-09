REQUIRED_FIELDS = ["product", "audience", "goal", "channel", "tone"]
MARKETING_CHANNELS = ["Email", "Social Post", "Ad Copy"]

def validate_inputs(data):
    problems = []
    for field in REQUIRED_FIELDS:
        value = data.get(field, "").strip()
        if not value:
            problems.append(f"'{field}' is required.")
    if data.get("channel") not in  MARKETING_CHANNELS:
        problems.append(f"'channel' must be one of: {MARKETING_CHANNELS}")
    return problems

if __name__ == "__main__":
    good = {"product": "Coffee shop", "audience": "Locals", "goal": "More visits", "channel": "email", "tone": "friendly"}
    bad = {"product": "", "audience": "Locals", "goal": "", "channel": "tiktok", "tone": "friendly"}
    print("Good:", validate_inputs(good))
    print("Bad:", validate_inputs(bad))