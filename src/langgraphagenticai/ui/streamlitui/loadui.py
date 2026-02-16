import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

        # Custom CSS for modern UI
        self._apply_custom_styles()

    def _apply_custom_styles(self):
        """Apply custom CSS styles for a modern, polished UI."""
        st.markdown("""
        <style>
        /* Main theme colors - Light Theme */
        :root {
            --primary-color: #6366f1;
            --secondary-color: #8b5cf6;
            --background: #f8fafc;
            --card-bg: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
        }

        /* Global styles */
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
        }

        /* Header styling */
        .main-header {
            text-align: center;
            padding: 2rem 0 1rem;
            background: linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .main-subtitle {
            text-align: center;
            color: #64748b;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%);
        }

        [data-testid="stSidebar"] > div:first-child {
            background: none;
        }

        /* Button styling */
        .stButton > button {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
        }

        /* Input styling */
        .stTextInput > div > div > input {
            background: #f1f5f9;
            color: #1e293b;
            border-radius: 8px;
        }

        /* Selectbox styling */
        .stSelectbox > div > div > select {
            background: #f1f5f9;
            color: #1e293b;
        }

        /* Info boxes */
        .info-box {
            background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
            border-left: 4px solid #6366f1;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }

        /* Chat messages */
        .stChatMessage {
            background: #ffffff;
            border-radius: 12px;
        }

        /* Hide default padding */
        .block-container {
            padding-top: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)

    def load_streamlit_ui(self):
        # Page config with modern settings
        st.set_page_config(
            page_title="AI News Hub",
            page_icon="📰",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # Custom header
        st.markdown("""
        <div class="main-header">
            <h1 style="font-size: 2.5rem; margin: 0; font-weight: 700;">Conversational AI Agent</h1>
        </div>
        <div class="main-subtitle">
            <p>With Real-Time Web Search & News Summarization</p>
        </div>
        """, unsafe_allow_html=True)

        # Divider line
        st.markdown("---", unsafe_allow_html=True)

        # Initialize session state
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False

        # Sidebar
        with st.sidebar:
            st.markdown("""
            <div style="text-align: center; padding: 1rem 0;">
                <h2 style="color: #6366f1; margin: 0;">⚙️ Configuration</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("---")

            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Provider Section
            st.markdown("### 🧠 LLM Provider")
            self.user_controls["selected_llm"] = st.selectbox(
                "Provider",
                llm_options,
                label_visibility="collapsed"
            )

            if self.user_controls["selected_llm"] == 'Groq':
                st.markdown("#### Model Selection")
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Model",
                    model_options,
                    label_visibility="collapsed"
                )

                st.markdown("#### 🔑 API Credentials")
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "Groq API Key",
                    type="password",
                    placeholder="gsk_...",
                    help="Get your key at: https://console.groq.com/keys"
                )

                if not self.user_controls["GROQ_API_KEY"]:
                    st.info("💡 **Tip:** Get your free API key at [console.groq.com](https://console.groq.com/keys)")

            st.markdown("---")

            # Use Case Section
            st.markdown("### 🎯 Select Use Case")
            self.user_controls["selected_usecase"] = st.selectbox(
                "Use Case",
                usecase_options,
                label_visibility="collapsed"
            )

            # Tavily API for features that need web search
            if self.user_controls["selected_usecase"] in ["Chatbot With Web", "AI News"]:
                st.markdown("---")
                st.markdown("### 🌐 Web Search API")
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = \
                    st.session_state["TAVILY_API_KEY"] = st.text_input(
                        "Tavily API Key",
                        type="password",
                        placeholder="tvly-...",
                        help="Get your key at: https://app.tavily.com/home"
                    )

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.info("💡 **Tip:** Get your free API key at [app.tavily.com](https://app.tavily.com/home)")

            # AI News specific options
            if self.user_controls['selected_usecase'] == "AI News":
                st.markdown("---")
                st.markdown("### 📰 News Settings")

                time_frame = st.selectbox(
                    "Time Period",
                    ["Daily", "Weekly", "Monthly"],
                    index=0,
                    help="Choose the time range for news aggregation"
                )

                st.markdown("")
                if st.button(
                    "🚀 Fetch Latest AI News",
                    use_container_width=True,
                    type="primary"
                ):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

            # Footer in sidebar
            st.markdown("---")
            st.markdown("""
            <div style="text-align: center; color: #64748b; font-size: 0.8rem; padding: 1rem 0;">
                <p>Built with ❤️ using LangGraph</p>
                <p>Powered by Groq & Tavily</p>
            </div>
            """, unsafe_allow_html=True)

        return self.user_controls
