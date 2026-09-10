import sys


# Streamlit may inherit a legacy Windows console encoding (for example cp1252).
# LLM responses can contain Unicode punctuation that those encodings cannot
# represent, so configure the console before importing the application.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.langgraphagenticai.main import load_langgraph_agenticai_app

if __name__ == "__main__":
    load_langgraph_agenticai_app()
