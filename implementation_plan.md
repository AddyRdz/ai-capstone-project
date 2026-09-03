# 1. Project Title
- Sports Movement AI
# 2. Project Summary
- Small application that accepts 10-15 second basketball or sports video containing one visible athlete. A pre-trained computer-vision model detects and tracks the person, Python converts the track into a few transparent observations- such as movement, total-screen space distance, and a locally run open-source large language model (LLM) converts only those observations into a short, readable summary. The project uses existing models without training them. It does not claim to understand plays, techniques, intent, identity, or performance quality.
# 3. Problem Statement
- Raw sports video is easy to watch but harder to describe consistently. A beginner developed also needs a manageable way to learn how computer video, ordinary Python logic, prompt engineering and an open-source LLM can form one end-to-end AI workflow.
# 4. Capstone Requirement Alignment
# 5. Project Scope
- Upload one MP4, MOV, or AVI video, limited to approximately 10–15 seconds and a documented size limit.
- Validate the file type, readability, duration, and presence of video frames.
- Use a pre-trained YOLO person detector/tracker; do not train a model.
- Select one primary track using a documented rule, such as the person track that appears in the most frames, with largest average bounding-box area as a tie-breaker.
- Extract the bounding-box center for that track over time.
- Calculate simple **screen-space** observations: visible-frame percentage, horizontal/vertical displacement, approximate path distance, predominant direction, and moving/still frame ratio.
- Show a basic result useful for debugging, such as selected track ID, observation table, or optional annotated preview.
- Send the structured observations—not the full video—to one local open-source LLM.
- Display a short grounded summary plus a limitations notice.
- Handle invalid videos, no-person cases, tracking failure, and unavailable LLM gracefully.
# 6. Recommended Technology Stack
* Python
* Streamlit
* Ultralytics YOLO
* NumPy
* qwen2
# 7. Application Workflow
- The user reads the privacy/limitations notice and uploads one short video.
- The UI checks extension, byte limit, duration, and whether OpenCV can decode frames.
- A temporary local file is created because video/model libraries commonly expect a path.
- The pre-trained vision model detects people and maintains track IDs across frames.
- A deterministic rule selects one primary athlete track. If selection is ambiguous, the MVP stops with an honest message instead of guessing.
- Python converts the selected bounding boxes into center points and simple observations.
- The program creates a compact structured record containing measurements, confidence/coverage information, and limitations.
- **The open-source LLM is used here:** the record and prompt instructions are sent to Ollama. The LLM verbalizes existing observations; it does not inspect the video or invent new measurements.
- The response is checked for emptiness and required headings, then displayed with the raw observations and disclaimer.
- Temporary video/derived files are deleted whether processing succeeds or fails.
# 9. Application Architecture
# 10. Step-by-Step Development Milestones