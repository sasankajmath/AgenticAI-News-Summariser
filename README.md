# LangGraph: Agentic AI News Summarizer

An intelligent AI agent application built with LangGraph that fetches, summarizes, and presents the latest AI news. Features a Streamlit web interface with multiple use cases including web-enhanced chatbot capabilities.

## Features

- **AI News Summarizer**
  - Fetches latest AI news from the web using Tavily API
  - Supports multiple timeframes: Daily, Weekly, and Monthly summaries
  - LLM-powered summarization with structured markdown output
  - Saves summaries to persistent markdown files organized by date

- **Chatbot with Web Search**
  - Conversational AI powered by Groq models
  - Real-time web search integration for up-to-date information
  - Context-aware responses using search results

- **Basic Chatbot**
  - Simple conversational AI interface
  - Fast responses using Groq's optimized inference

## Project Structure

```
AI_News_Summerize/
├── app.py                              # Main entry point
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── AINews/                             # Output directory for news summaries
│   ├── daily_summary.md
│   ├── weekly_summary.md
│   └── monthly_summary.md
└── src/langgraphagenticai/             # Main source code
    ├── __init__.py
    ├── main.py                         # Main application logic
    ├── graph/                          # LangGraph workflow definitions
    │   ├── __init__.py
    │   └── graph_builder.py            # Builds use case graphs
    ├── LLMS/                           # LLM configuration
    │   ├── __init__.py
    │   └── groqllm.py                  # Groq LLM integration
    ├── nodes/                          # Graph processing nodes
    │   ├── __init__.py
    │   ├── ai_news_node.py             # AI news fetch & summarization
    │   ├── basic_chatbot_node.py       # Basic chatbot node
    │   └── chatbot_with_Tool_node.py   # Chatbot with tools
    ├── state/                          # State management
    │   ├── __init__.py
    │   └── state.py                    # TypedDict for graph state
    ├── tools/                          # Tool integrations
    │   ├── __init__.py
    │   └── search_tool.py              # Tavily search integration
    └── ui/                             # Streamlit UI components
        ├── __init__.py
        ├── uiconfigfile.ini            # UI configuration
        ├── uiconfigfile.py             # Configuration loader
        └── streamlitui/
            ├── __init__.py
            ├── loadui.py               # UI component loader
            └── display_result.py       # Result display handler
```

## Installation

### Prerequisites

- Python 3.9 or higher
- Groq API key ([Get one here](https://groq.com/))
- Tavily API key ([Get one here](https://tavily.com/))

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_News_Summerize
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
streamlit run app.py
```

### Configuration

In the Streamlit sidebar:
1. Enter your Groq API key
2. Enter your Tavily API key
3. Select a Groq model (options include):
   - `openai/gpt-oss-20b`
   - `openai/gpt-oss-120b`
   - `qwen/qwen3.6-27b`
   - `qwen/qwen3.8-27b`
4. Choose a use case:
   - **Basic Chatbot** - Simple conversation
   - **Chatbot With Web** - Chat with web search
   - **AI News** - Generate AI news summaries

### AI News Summarizer

When using the AI News feature:
1. Select a frequency (Daily, Weekly, or Monthly)
2. Click "Generate Summary"
3. The agent will:
   - Fetch the latest AI news from the web
   - Summarize the content using the selected LLM
   - Save the summary to a markdown file
   - Display the formatted results

## Architecture

### LangGraph Workflow

The application uses LangGraph for building stateful, multi-actor applications with LLMs:

- **State Management**: Uses TypedDict for maintaining conversation state
- **Node-based Processing**: Each operation (fetch, summarize, save) is a separate node
- **Graph Builder**: Dynamically builds workflows based on selected use case

### Components

| Component | Description |
|-----------|-------------|
| `graph_builder.py` | Creates LangGraph workflows for different use cases |
| `ai_news_node.py` | Handles news fetching, summarization, and saving |
| `search_tool.py` | Tavily API integration for web search |
| `groqllm.py` | Groq LLM configuration and initialization |

## Dependencies

- `langchain` - LLM framework
- `langgraph` - Workflow orchestration
- `langchain_community` - Community integrations
- `langchain_core` - Core LangChain components
- `langchain_groq` - Groq integration
- `langchain_openai` - OpenAI integration
- `faiss-cpu` - Vector database for embeddings
- `streamlit` - Web app framework
- `tavily-python` - Search API client

## Output

News summaries are saved in the `AINews/` directory:
- `daily_summary.md` - Daily AI news summary
- `weekly_summary.md` - Weekly AI news summary
- `monthly_summary.md` - Monthly AI news summary

Each summary includes:
- Date of generation
- Source links
- Structured news items with summaries
- Proper citations

## License

MIT License
