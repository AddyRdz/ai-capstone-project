from ai_capstone_project.validation import validate_inputs
from ai_capstone_project.prompts import build_prompt
from ai_capstone_project.llm_client import ask_model

def main():
    data = {
        "product" : "Coffee shop",
        "audience" : "Locals",
        "goal" : "More Visits",
        "channel" : "email",
        "tone" : "friendly",
    }

    problems = validate_inputs(data)
    if problems:
        print("Fix this error: ", problems)
        return
    prompt = build_prompt(data)
    draft = ask_model(prompt)
    print(draft)
