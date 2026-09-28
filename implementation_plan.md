# 1. Project Title
AI Marketing Campaign Content Generator
# 2. Project Summary
This application helps people create the first draft of marketing content. The user fills in a short form: the product or service, the target audience, the campaign goal, the marketing channel(ex: email or social media post), and the desired tone. The app combines those answers into a carefully written prompt, sends it to an open-source large language model running locally on the users computer, and displays a structured draft the user can copy, download, and edit.
# 3. Problem Statement
Problem: Starting marketing content is slow. Small business owners, students, and nonprofit staff often struggle with creating marketing materials, and their drafts can be inconsistent in tone or missing a clear call to action.
Why it matters: Consistent marketing helps small organizations reach customers, but many cannot afford agencies or paid AI subscriptions. A free, local tool lowers that barrier nad keeps business details on the user's own machine.
Intended Users: Small business owners, student organizations, freelancers, and marketing beginners that are looking to create their first draft.
# 4. Capstone Requirement Alignment
# 5. Project Scope
MVP features:
* A form that collects: product/service, target audience, goal, channel, tone.
* Input validation.
* A prompt builder with a template for multiple channels.
* One LLM call through Ollama
* Response and display in the browser
* Friendly error messages
* A label that the output is an AI-generated draft.
# 6. Recommended Technology Stack
* Llama 3.2
* Ollama
* Steamlit
* Pytest
* UV
* VSCode
* Github
# 7. Application Workflow
* User opens the Streamlit page and fills the form.
* User clicks generate.
* Validation checks the inputs.
* The prompts builder turns the inputs into a system prompt.
* The LLM client sends the prompt to the local Ollama server.
* Ollama runs the model and returns text.
* The formatter cleans the text.
* Steamlit displays the draft, a disclaimer, options.
* If any step fails, an error message is displayed.
# 8. Application Architecture
# 9. Proposed Project Structure
# 10. Step-by-Step Development Milestones