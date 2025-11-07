"""
Gunny - a CrewAI Companion

A Streamlit application for creating complete CrewAI projects with all configuration options.
"""

import streamlit as st
from typing import Dict, List, Any
from utils.constants import (
    PROCESS_TYPES,
    DEFAULT_CREW_CONFIG,
    KNOWLEDGE_SOURCE_TYPES,
    EMBEDDER_PROVIDERS,
    ENTERPRISE_APPS,
    ENV_VARIABLES,
    TOOLS_CATALOG,
)
from utils.validators import validate_complete_configuration, check_required_env_vars
from generators.project_generator import (
    generate_project_structure,
    create_zip_file,
    generate_project_summary,
)
from generators.yaml_generator import generate_agents_yaml, generate_tasks_yaml
from generators.python_generator import generate_crew_py, generate_main_py
from ui.components import (
    agent_configuration_form,
    task_configuration_form,
    tools_selector,
    code_preview,
    validation_messages,
)
from ui.icons import get_icon, icon_inline, icon_tab, icon_button, get_favicon_svg

# Page configuration
st.set_page_config(
    page_title="Gunny - CrewAI Companion",
    page_icon=get_favicon_svg(),
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom dark mode styling
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap');

    :root {
        --background: oklch(0.1649 0.0352 281.8285);
        --foreground: oklch(0.9513 0.0074 260.7315);
        --card: oklch(0.2542 0.0611 281.1423);
        --card-foreground: oklch(0.9513 0.0074 260.7315);
        --popover: oklch(0.2542 0.0611 281.1423);
        --popover-foreground: oklch(0.9513 0.0074 260.7315);
        --primary: oklch(0.6726 0.2904 341.4084);
        --primary-foreground: oklch(1.0000 0 0);
        --secondary: oklch(0.2542 0.0611 281.1423);
        --secondary-foreground: oklch(0.9513 0.0074 260.7315);
        --muted: oklch(0.2123 0.0522 280.9917);
        --muted-foreground: oklch(0.6245 0.0500 278.1046);
        --accent: oklch(0.8903 0.1739 171.2690);
        --accent-foreground: oklch(0.1649 0.0352 281.8285);
        --destructive: oklch(0.6535 0.2348 34.0370);
        --destructive-foreground: oklch(1.0000 0 0);
        --border: oklch(0.3279 0.0832 280.7890);
        --input: oklch(0.3279 0.0832 280.7890);
        --ring: oklch(0.6726 0.2904 341.4084);
        --sidebar: oklch(0.1649 0.0352 281.8285);
        --sidebar-foreground: oklch(0.9513 0.0074 260.7315);
        --sidebar-primary: oklch(0.6726 0.2904 341.4084);
        --sidebar-accent: oklch(0.8903 0.1739 171.2690);
        --sidebar-border: oklch(0.3279 0.0832 280.7890);
        --font-sans: 'Outfit', sans-serif;
        --font-mono: 'Fira Code', monospace;
        --radius: 0.5rem;
        --shadow-sm: 0px 4px 8px -2px hsl(0 0% 0% / 0.10), 0px 1px 2px -3px hsl(0 0% 0% / 0.10);
        --shadow-md: 0px 4px 8px -2px hsl(0 0% 0% / 0.10), 0px 2px 4px -3px hsl(0 0% 0% / 0.10);
        --shadow-lg: 0px 4px 8px -2px hsl(0 0% 0% / 0.10), 0px 4px 6px -3px hsl(0 0% 0% / 0.10);
        --spacing-xs: 0.5rem;
        --spacing-sm: 0.75rem;
        --spacing-md: 1rem;
        --spacing-lg: 1.5rem;
        --spacing-xl: 2rem;
        --spacing-2xl: 3rem;
    }

    /* Global font and background */
    html, body, [class*="css"], .stApp {
        font-family: var(--font-sans) !important;
        background-color: var(--background) !important;
        color: var(--foreground) !important;
    }

    /* Headings */
    h1 {
        font-family: var(--font-sans) !important;
        color: var(--foreground) !important;
        font-weight: 600 !important;
        margin-bottom: var(--spacing-md) !important;
        padding-bottom: var(--spacing-sm) !important;
    }

    h2, h3 {
        font-family: var(--font-sans) !important;
        color: var(--foreground) !important;
        font-weight: 600 !important;
        margin-top: var(--spacing-md) !important;
        margin-bottom: var(--spacing-sm) !important;
    }

    h4, h5, h6 {
        font-family: var(--font-sans) !important;
        color: var(--foreground) !important;
        font-weight: 600 !important;
    }

    /* Main content area */
    .main .block-container {
        background-color: var(--background) !important;
        padding: var(--spacing-md) var(--spacing-sm) !important;
        max-width: 1400px !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: var(--sidebar) !important;
        border-right: 1px solid var(--sidebar-border) !important;
        padding: var(--spacing-md) var(--spacing-sm) !important;
    }

    [data-testid="stSidebar"] * {
        color: var(--sidebar-foreground) !important;
    }

    /* Cards and containers */
    [data-testid="stExpander"],
    [data-testid="stAlert"] {
        background-color: var(--card) !important;
        border-radius: var(--radius) !important;
        border: 1px solid var(--border) !important;
        box-shadow: var(--shadow-sm) !important;
        color: var(--card-foreground) !important;
        margin-bottom: var(--spacing-sm) !important;
    }

    [data-testid="stExpander"] > div {
        padding: var(--spacing-md) !important;
    }

    [data-testid="stExpanderDetails"] {
        padding: var(--spacing-sm) var(--spacing-md) !important;
    }

    .stTabs [data-baseweb="tab-panel"] {
        background-color: var(--card) !important;
        border-radius: var(--radius) !important;
        border: 1px solid var(--border) !important;
        box-shadow: var(--shadow-sm) !important;
        color: var(--card-foreground) !important;
        padding: var(--spacing-md) !important;
        margin-top: var(--spacing-md) !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background-color: transparent !important;
        border-bottom: none !important;
        width: 100% !important;
        display: flex !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: var(--muted) !important;
        color: var(--muted-foreground) !important;
        border-radius: var(--radius) !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        border: 1px solid var(--border) !important;
        flex: 1 !important;
        text-align: center !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--primary) !important;
        color: var(--primary-foreground) !important;
        border-color: var(--primary) !important;
    }

    /* Hide tab borders and underlines */
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }

    .stTabs::after,
    .stTabs::before,
    .stTabs [data-baseweb="tab-list"]::after,
    .stTabs [data-baseweb="tab-list"]::before {
        display: none !important;
    }

    /* Input fields */
    .stTextInput, .stTextArea, .stNumberInput, .stSelectbox {
        margin-bottom: var(--spacing-sm) !important;
    }

    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input,
    .stSelectbox select {
        background-color: var(--input) !important;
        color: var(--foreground) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        font-family: var(--font-sans) !important;
        padding: var(--spacing-sm) var(--spacing-md) !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus,
    .stNumberInput input:focus,
    .stSelectbox select:focus {
        border-color: var(--ring) !important;
        box-shadow: 0 0 0 2px var(--ring) !important;
        outline: none !important;
    }

    /* Buttons */
    .stButton, .stDownloadButton {
        margin: var(--spacing-xs) var(--spacing-xs) !important;
    }

    .stButton button {
        background-color: var(--primary) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem !important;
        font-weight: 700 !important;
        font-family: var(--font-sans) !important;
        box-shadow: var(--shadow-sm) !important;
        transition: all 0.2s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 2rem !important;
        min-height: 3rem !important;
        width: 100% !important;
        line-height: 1 !important;
    }

    .stButton button p {
        color: white !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .stButton button:hover {
        background-color: var(--accent) !important;
        color: var(--accent-foreground) !important;
        box-shadow: var(--shadow-md) !important;
        transform: translateY(-1px) !important;
    }

    .stDownloadButton button {
        background-color: var(--accent) !important;
        color: var(--accent-foreground) !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: var(--card) !important;
        padding: var(--spacing-sm) !important;
        border-radius: var(--radius) !important;
        border: 1px solid var(--border) !important;
        margin: var(--spacing-sm) 0 !important;
    }

    [data-testid="stMetricValue"] {
        color: var(--primary) !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted-foreground) !important;
        font-weight: 500 !important;
    }

    /* Info/Success/Warning/Error boxes */
    .stAlert {
        border-radius: var(--radius) !important;
        padding: var(--spacing-sm) var(--spacing-md) !important;
        margin: var(--spacing-sm) 0 !important;
    }

    [data-baseweb="notification"] {
        background-color: var(--card) !important;
        border-left: 4px solid var(--primary) !important;
    }

    /* Sidebar info text styling - smaller and lighter */
    [data-testid="stSidebar"] .stAlert p {
        font-size: 0.85rem !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
    }

    /* Code blocks */
    code {
        font-family: var(--font-mono) !important;
        background-color: var(--muted) !important;
        color: var(--foreground) !important;
        border-radius: calc(var(--radius) - 2px) !important;
        padding: 0.2rem 0.5rem !important;
    }

    pre {
        font-family: var(--font-mono) !important;
        background-color: var(--muted) !important;
        color: var(--foreground) !important;
        border-radius: var(--radius) !important;
        padding: var(--spacing-sm) var(--spacing-md) !important;
        margin: var(--spacing-sm) 0 !important;
        overflow-x: auto !important;
    }

    /* Checkbox and radio */
    .stCheckbox, .stRadio {
        padding: var(--spacing-xs) 0 !important;
        margin: var(--spacing-xs) 0 !important;
    }

    .stCheckbox label,
    .stRadio label {
        color: var(--foreground) !important;
        font-family: var(--font-sans) !important;
    }

    /* Radio button custom styling - brand pink */
    .stRadio [role="radio"][aria-checked="true"]::before {
        background-color: var(--primary) !important;
    }

    .stRadio [role="radio"]::before {
        border-color: var(--primary) !important;
    }

    /* Remove white center dot from selected radio buttons */
    .stRadio [role="radio"][aria-checked="true"]::after {
        display: none !important;
    }

    /* Ensure transparent background for all radio inner elements */
    .stRadio [role="radio"]::after {
        background-color: transparent !important;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border-radius: var(--radius) !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-sm) !important;
    }

    /* Multiselect */
    .stMultiSelect [data-baseweb="tag"] {
        background-color: var(--primary) !important;
        color: var(--primary-foreground) !important;
        border-radius: calc(var(--radius) - 2px) !important;
        padding: var(--spacing-xs) var(--spacing-sm) !important;
        margin: var(--spacing-xs) !important;
    }

    /* Columns */
    [data-testid="column"] {
        padding: 0 var(--spacing-xs) !important;
    }

    /* Slider */
    .stSlider [data-baseweb="slider"] {
        background-color: var(--muted) !important;
    }

    .stSlider [role="slider"] {
        background-color: var(--primary) !important;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: var(--background);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--muted);
        border-radius: var(--radius);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary);
    }

    /* Links */
    a {
        color: var(--primary) !important;
        text-decoration: none !important;
    }

    a:hover {
        color: var(--accent) !important;
        text-decoration: underline !important;
    }

    /* Divider */
    hr {
        border-color: var(--border) !important;
        margin: var(--spacing-md) 0 !important;
    }

    /* Remove Streamlit branding elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Spinner */
    .stSpinner > div {
        border-top-color: var(--primary) !important;
    }

    /* Section Container - Card-like styling for section groups */
    .section-container {
        background: oklch(0.28 0.065 281);
        border-radius: var(--radius);
        padding: var(--space-md);
        margin-bottom: var(--space-lg);
        border: 1px solid var(--border);
    }
</style>
""",
    unsafe_allow_html=True,
)

# Initialize session state
if "agents" not in st.session_state:
    st.session_state.agents = []
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "crew_config" not in st.session_state:
    st.session_state.crew_config = DEFAULT_CREW_CONFIG.copy()
if "selected_tools" not in st.session_state:
    st.session_state.selected_tools = []
if "tools_by_agent" not in st.session_state:
    st.session_state.tools_by_agent = {}
if "knowledge_sources" not in st.session_state:
    st.session_state.knowledge_sources = []
if "env_vars" not in st.session_state:
    st.session_state.env_vars = {}
if "generation_mode" not in st.session_state:
    st.session_state.generation_mode = "core_files"

# Header - Brand box matching tabs width
st.markdown(
    """
<div style='
    background: linear-gradient(135deg, oklch(0.65 0.15 195) 0%, oklch(0.60 0.12 210) 100%);
    padding: 3rem 1.5rem 2rem 1.5rem;
    border-radius: var(--radius);
    margin-top: 2rem;
    margin-bottom: 0.5rem;
    width: 100%;
    box-sizing: border-box;
'>
    <div style='display: inline-block; background: #ec4899; padding: 0.75rem 2rem; border-radius: 50px; margin-bottom: 0.75rem; box-shadow: none; border: none;'>
        <h1 style='margin: 0; font-size: 5rem; color: white;'>Gunny</h1>
    </div>
    <p style='margin: 0.5rem 0 0 0; font-size: 1.5rem; color: rgba(255, 255, 255, 0.95); font-weight: 500;'>CrewAI Companion</p>
</div>
""",
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.markdown("---")
    st.markdown("**Project Status**")
    st.metric("Agents", len(st.session_state.agents))
    st.metric("Tasks", len(st.session_state.tasks))
    st.markdown("---")
    st.markdown("### About Gunny")
    st.info(
        "Configure CrewAI agents, tasks, and crews. "
        "Generate core files for existing projects or complete project structures."
    )

# Main tabs
tool_count = sum(len(tools) for tools in TOOLS_CATALOG.values())
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
    [
        "Project Info",
        "Agents",
        "Tasks",
        "Crew Config",
        f"Tools ({tool_count})",
        "Knowledge",
        "ENV",
        "Preview & Generate",
    ]
)

# Tab 1: Project Information
with tab1:
    st.header("Project Information")

    project_name = st.text_input(
        "Project Name *",
        value=st.session_state.get("project_name", ""),
        help="Name of your CrewAI project (use underscores for spaces)",
        placeholder="my_awesome_crew",
    )
    st.session_state.project_name = project_name

    project_description = st.text_area(
        "Project Description",
        value=st.session_state.get("project_description", ""),
        help="Brief description of what your crew does",
        placeholder="A crew of AI agents that...",
    )
    st.session_state.project_description = project_description

    python_version = st.selectbox(
        "Python Version",
        options=["3.10", "3.11", "3.12"],
        index=0,
        help="Minimum Python version for your project",
    )
    st.session_state.python_version = python_version

    st.markdown("---")

    # Generation mode selector
    st.subheader("Generation Mode")
    generation_mode = st.radio(
        "What would you like to generate?",
        options=["core_files", "complete_project"],
        format_func=lambda x: "Core Files Only"
        if x == "core_files"
        else "Complete Project",
        index=0 if st.session_state.generation_mode == "core_files" else 1,
        help="Core Files: generates only agents.yaml, tasks.yaml, crew.py, main.py for existing projects. Complete Project: generates full project structure with all boilerplate.",
        horizontal=True,
    )
    st.session_state.generation_mode = generation_mode

    st.markdown("---")
    st.markdown("### Project Structure Preview")

    if st.session_state.generation_mode == "core_files":
        st.code(
            f"""
{project_name}/
└── src/{project_name}/
    ├── main.py
    ├── crew.py
    └── config/
        ├── agents.yaml
        └── tasks.yaml
""",
            language="text",
        )
    else:
        st.code(
            f"""
{project_name}/
├── .gitignore
├── .env
├── README.md
├── pyproject.toml
└── src/{project_name}/
    ├── __init__.py
    ├── main.py
    ├── crew.py
    ├── config/
    │   ├── agents.yaml
    │   └── tasks.yaml
    ├── tools/
    │   ├── __init__.py
    │   └── custom_tool.py
    └── knowledge/
        └── README.md
""",
            language="text",
        )

# Tab 2: Agents Configuration
with tab2:
    st.header("Agent Configuration")
    st.markdown("Configure your AI agents with roles, goals, and capabilities.")

    # Agent management buttons
    st.markdown(
        """<style>
        button[key="add_agent_btn"], button[key="remove_agent_btn"] {
            height: 3rem !important;
            min-height: 3rem !important;
            max-height: 3rem !important;
            padding: 0.75rem !important;
        }
        button[key="add_agent_btn"] p, button[key="remove_agent_btn"] p {
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: white !important;
            line-height: 1 !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        </style>""",
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([0.3, 0.3, 4.4])
    with col1:
        if st.button("➕", key="add_agent_btn", help="Add Agent", use_container_width=True):
            st.session_state.agents.append({})
            st.rerun()
    with col2:
        if st.button("➖", key="remove_agent_btn", help="Remove Last Agent", use_container_width=True) and len(st.session_state.agents) > 0:
            st.session_state.agents.pop()
            st.rerun()

    st.markdown("---")

    # Display agent forms
    if len(st.session_state.agents) > 0:
        for i in range(len(st.session_state.agents)):
            agent_config = agent_configuration_form(i, st.session_state.agents[i])
            st.session_state.agents[i] = agent_config

            # Tools for this agent
            with st.expander(f"Tools for Agent {i + 1}", expanded=False):
                agent_role = agent_config.get("role", f"Agent {i + 1}")
                current_tools = st.session_state.tools_by_agent.get(agent_role, [])

                st.write(
                    "Select tools for this agent (or configure all tools in the Tools tab)"
                )

                # Quick tool selection
                selected = []
                cols = st.columns(3)
                common_tools = ["SerperDevTool", "FileReadTool", "WebsiteSearchTool"]

                for idx, tool_name in enumerate(common_tools):
                    with cols[idx % 3]:
                        if st.checkbox(
                            tool_name,
                            value=tool_name in current_tools,
                            key=f"agent_{i}_tool_{tool_name}",
                        ):
                            selected.append(tool_name)

                st.session_state.tools_by_agent[agent_role] = selected

# Tab 3: Tasks Configuration
with tab3:
    st.header("Task Configuration")
    st.markdown("Define tasks and assign them to agents.")

    # Get available agent roles
    available_agents = [
        agent.get("role", f"Agent {i + 1}")
        for i, agent in enumerate(st.session_state.agents)
        if agent.get("role")
    ]
    available_task_names = [
        task.get("name", f"task_{i + 1}")
        for i, task in enumerate(st.session_state.tasks)
    ]

    # Task management buttons
    st.markdown(
        """<style>
        button[key="add_task_btn"], button[key="remove_task_btn"] {
            height: 3rem !important;
            min-height: 3rem !important;
            max-height: 3rem !important;
            padding: 0.75rem !important;
        }
        button[key="add_task_btn"] p, button[key="remove_task_btn"] p {
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: white !important;
            line-height: 1 !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        </style>""",
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([0.3, 0.3, 4.4])
    with col1:
        if st.button("➕", key="add_task_btn", help="Add Task", use_container_width=True):
            st.session_state.tasks.append({})
            st.rerun()
    with col2:
        if st.button("➖", key="remove_task_btn", help="Remove Last Task", use_container_width=True) and len(st.session_state.tasks) > 0:
            st.session_state.tasks.pop()
            st.rerun()

    st.markdown("---")

    # Check if agents exist
    if len(available_agents) == 0:
        pass
    elif len(st.session_state.tasks) > 0:
        for i in range(len(st.session_state.tasks)):
            # Get available tasks for context (excluding current task)
            context_tasks = [
                name for j, name in enumerate(available_task_names) if j != i
            ]

            task_config = task_configuration_form(
                i, available_agents, context_tasks, st.session_state.tasks[i]
            )
            st.session_state.tasks[i] = task_config

# Tab 4: Crew Configuration
with tab4:
    st.header("Crew Configuration")
    st.markdown("Configure how your crew operates.")
    st.markdown("---")

    st.subheader("Basic Settings")

    crew_name = st.text_input(
        "Crew Name",
        value=st.session_state.crew_config.get("name", "crew"),
        help="Name for your crew instance",
    )
    st.session_state.crew_config["name"] = crew_name

    process = st.selectbox(
        "Process Type",
        options=list(PROCESS_TYPES.keys()),
        format_func=lambda x: f"{x.capitalize()} - {PROCESS_TYPES[x]}",
        help="How tasks are executed",
    )
    st.session_state.crew_config["process"] = process

    verbose = st.checkbox(
        "Verbose Mode",
        value=st.session_state.crew_config.get("verbose", False),
        help="Enable detailed logging",
    )
    st.session_state.crew_config["verbose"] = verbose

    cache = st.checkbox(
        "Enable Cache",
        value=st.session_state.crew_config.get("cache", True),
        help="Cache results for efficiency",
    )
    st.session_state.crew_config["cache"] = cache

    st.markdown("---")

    st.subheader("Observability & Tracing")

    enable_langsmith = st.checkbox(
        "Enable LangSmith Tracing",
        value=st.session_state.get("enable_langsmith", False),
        help="Enable LLM observability and debugging with LangSmith (free tier: 5k traces/month)",
    )
    st.session_state.enable_langsmith = enable_langsmith

    if enable_langsmith:
        langsmith_project = st.text_input(
            "LangSmith Project Name",
            value=st.session_state.get(
                "langsmith_project",
                st.session_state.get("project_name", "my-crew-project"),
            ),
            placeholder="my-crew-project",
            help="Project name for organizing traces in LangSmith dashboard",
        )
        st.session_state.langsmith_project = langsmith_project

        # Show mode-specific guidance
        generation_mode = st.session_state.get("generation_mode", "core_files")
        if generation_mode == "core_files":
            st.warning(
                "📋 **Core Files Mode**: Manual integration required. See instructions in the Preview & Generate tab."
            )
        else:
            st.success(
                "✅ **Complete Project Mode**: LangSmith will be auto-configured in .env and pyproject.toml"
            )

        st.info("Get your free API key at: https://smith.langchain.com")

    st.markdown("---")

    st.subheader("Advanced Settings")

    memory = st.checkbox(
        "Enable Memory",
        value=st.session_state.crew_config.get("memory", False),
        help="Enable short and long-term memory",
    )
    st.session_state.crew_config["memory"] = memory

    planning = st.checkbox(
        "Enable Planning",
        value=st.session_state.crew_config.get("planning", False),
        help="Enable autonomous planning",
    )
    st.session_state.crew_config["planning"] = planning

    max_rpm = st.number_input(
        "Max RPM",
        min_value=0,
        value=st.session_state.crew_config.get("max_rpm") or 0,
        help="Maximum requests per minute (0 = unlimited)",
    )
    if max_rpm > 0:
        st.session_state.crew_config["max_rpm"] = max_rpm
    else:
        st.session_state.crew_config["max_rpm"] = None

    st.markdown("---")

    # Hierarchical Process Settings
    if process == "hierarchical":
        st.subheader("Hierarchical Process Settings")
        st.info("Hierarchical process requires a manager LLM or manager agent")

        manager_llm = st.text_input(
            "Manager LLM",
            value=st.session_state.crew_config.get("manager_llm", ""),
            help="LLM to use for the manager agent (e.g., 'gpt-4')",
            placeholder="gpt-4",
        )
        st.session_state.crew_config["manager_llm"] = manager_llm

# Tab 5: Tools Configuration
with tab5:
    st.header("Tools Configuration")
    st.markdown("Select tools available to your agents.")
    st.markdown("---")

    selected_tools = tools_selector(st.session_state.selected_tools)
    st.session_state.selected_tools = selected_tools

    if selected_tools:
        st.success(f"{len(selected_tools)} tools selected")

        with st.expander("View Selected Tools"):
            for tool in selected_tools:
                st.write(f"- {tool}")

# Tab 6: Knowledge Configuration
with tab6:
    st.header("Knowledge Base Configuration")
    st.markdown("Add knowledge sources for your agents.")
    st.markdown("---")

    st.subheader("Knowledge Sources")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(
            f"<div>{icon_button('plus', 'Add Knowledge Source')}</div>",
            unsafe_allow_html=True,
        )
        if st.button("Add Knowledge Source", key="add_knowledge_btn"):
            st.session_state.knowledge_sources.append({"type": "String", "config": {}})
            st.rerun()

    if len(st.session_state.knowledge_sources) > 0:
        for i, source in enumerate(st.session_state.knowledge_sources):
            with st.expander(f"Knowledge Source {i + 1}", expanded=True):
                source_type = st.selectbox(
                    "Source Type",
                    options=KNOWLEDGE_SOURCE_TYPES,
                    index=KNOWLEDGE_SOURCE_TYPES.index(source.get("type", "String")),
                    key=f"knowledge_{i}_type",
                )
                source["type"] = source_type

                if source_type == "String":
                    content = st.text_area(
                        "Content",
                        value=source.get("config", {}).get("content", ""),
                        key=f"knowledge_{i}_content",
                        help="Direct text content",
                    )
                    source["config"] = {"content": content}
                else:
                    file_path = st.text_input(
                        "File Path",
                        value=source.get("config", {}).get("path", ""),
                        key=f"knowledge_{i}_path",
                        help=f"Path to {source_type} file in knowledge/ directory",
                        placeholder=f"knowledge/document.{source_type.lower()}",
                    )
                    source["config"] = {"path": file_path}

                st.markdown(
                    f"<div>{icon_button('trash-2', 'Remove')}</div>",
                    unsafe_allow_html=True,
                )
                if st.button("Remove", key=f"knowledge_{i}_remove_btn"):
                    st.session_state.knowledge_sources.pop(i)
                    st.rerun()

    st.markdown("---")
    st.subheader("Embedder Configuration")

    use_embedder = st.checkbox(
        "Configure Custom Embedder", value=st.session_state.get("use_embedder", False)
    )
    st.session_state.use_embedder = use_embedder

    if use_embedder:
        embedder_provider = st.selectbox(
            "Embedder Provider",
            options=EMBEDDER_PROVIDERS,
            help="Vector embedding provider",
        )
        st.session_state.embedder_provider = embedder_provider

# Tab 7: ENV Configuration
with tab7:
    st.header("Environment Variables")

    # Section 1: Auto-Detected Environment Variables
    st.markdown('<div class="section-container">', unsafe_allow_html=True)

    # Determine required env vars
    if st.session_state.agents:
        required_vars = check_required_env_vars(
            st.session_state.agents,
            st.session_state.selected_tools,
            st.session_state.get("enable_langsmith", False),
        )

        if required_vars:
            st.info(
                f"Based on your configuration, you'll need: {', '.join(required_vars)}"
            )

            for var in required_vars:
                placeholder = "your_api_key_here"
                current_value = st.session_state.env_vars.get(var, placeholder)

                env_value = st.text_input(
                    var,
                    value=current_value,
                    type="password",
                    help=f"API key for {var}",
                    key=f"env_{var}",
                )
                st.session_state.env_vars[var] = env_value
        else:
            st.info(
                "No specific API keys detected. You can add custom environment variables below."
            )
    st.markdown("</div>", unsafe_allow_html=True)

    # Section 2: Custom Environment Variables
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("Custom Environment Variables")

    custom_var_name = st.text_input("Variable Name", key="custom_env_name")
    custom_var_value = st.text_input(
        "Variable Value", type="password", key="custom_env_value"
    )

    if st.button("Add Custom Variable"):
        if custom_var_name and custom_var_value:
            st.session_state.env_vars[custom_var_name] = custom_var_value
            st.success(f"Added {custom_var_name}")
        else:
            st.error("Please provide both name and value")
    st.markdown("</div>", unsafe_allow_html=True)

    # Section 3: Enterprise Features
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("Enterprise Features")

    enterprise_apps = st.multiselect(
        "Enterprise App Integrations",
        options=ENTERPRISE_APPS,
        help="Select enterprise applications to integrate",
    )
    st.session_state.enterprise_apps = enterprise_apps

    if enterprise_apps:
        st.info(f"Selected: {', '.join(enterprise_apps)}")
    st.markdown("</div>", unsafe_allow_html=True)

# Tab 8: Preview & Generate
with tab8:
    st.header("Preview & Generate Project")

    # Validation
    project_name = st.session_state.get("project_name", "")

    if not project_name:
        st.error("Please provide a project name in the Project Info tab")
    elif len(st.session_state.agents) == 0:
        st.error("Please create at least one agent")
    elif len(st.session_state.tasks) == 0:
        st.error("Please create at least one task")
    else:
        # Validate configuration
        is_valid, errors = validate_complete_configuration(
            project_name,
            st.session_state.agents,
            st.session_state.tasks,
            st.session_state.crew_config,
        )

        validation_messages(errors)

        if is_valid:
            # Generate project files for download button
            project_files = generate_project_structure(
                project_name,
                st.session_state.project_description,
                st.session_state.agents,
                st.session_state.tasks,
                st.session_state.crew_config,
                st.session_state.tools_by_agent,
                st.session_state.env_vars,
                st.session_state.get("python_version", "3.10"),
                st.session_state.generation_mode,
                st.session_state.get("enable_langsmith", False),
                st.session_state.get("langsmith_project", "my-crew-project"),
            )

            # Create ZIP file
            zip_data = create_zip_file(project_files, project_name)

            # Customize filename based on mode
            if st.session_state.generation_mode == "core_files":
                zip_filename = f"{project_name}_core.zip"
            else:
                zip_filename = f"{project_name}.zip"

            # Download button at top
            st.download_button(
                label="Download ZIP",
                data=zip_data,
                file_name=zip_filename,
                mime="application/zip",
                use_container_width=True,
                type="primary",
            )

            # Customize success message based on mode
            if st.session_state.generation_mode == "core_files":
                st.success(
                    "Core files generated successfully! Download includes: agents.yaml, tasks.yaml, crew.py, main.py"
                )
            else:
                st.success(
                    "Project generated successfully! Download the ZIP file and extract it to get started."
                )

            st.markdown("---")

            # View Summary - toggleable
            if "show_summary" not in st.session_state:
                st.session_state.show_summary = False

            if st.button(
                "View Summary" if not st.session_state.show_summary else "Hide Summary",
                use_container_width=False,
            ):
                st.session_state.show_summary = not st.session_state.show_summary

            if st.session_state.show_summary:
                summary = generate_project_summary(
                    project_name,
                    st.session_state.agents,
                    st.session_state.tasks,
                    st.session_state.crew_config,
                )
                st.markdown(summary)

            st.markdown("---")

            # Generate preview
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(
                    f"<h3>{icon_inline('file', 20)} agents.yaml</h3>",
                    unsafe_allow_html=True,
                )
                agents_yaml = generate_agents_yaml(st.session_state.agents)
                st.code(agents_yaml, language="yaml")

            with col2:
                st.markdown(
                    f"<h3>{icon_inline('file', 20)} tasks.yaml</h3>",
                    unsafe_allow_html=True,
                )
                tasks_yaml = generate_tasks_yaml(st.session_state.tasks)
                st.code(tasks_yaml, language="yaml")

            st.markdown("---")

            col3, col4 = st.columns(2)

            with col3:
                st.markdown(
                    f"<h3>{icon_inline('code', 20)} crew.py</h3>",
                    unsafe_allow_html=True,
                )
                crew_py = generate_crew_py(
                    project_name,
                    st.session_state.agents,
                    st.session_state.tasks,
                    st.session_state.crew_config,
                    st.session_state.tools_by_agent,
                )
                st.code(crew_py, language="python")

            with col4:
                st.markdown(
                    f"<h3>{icon_inline('code', 20)} main.py</h3>",
                    unsafe_allow_html=True,
                )
                input_vars = []  # Extract from descriptions
                main_py = generate_main_py(project_name, input_vars)
                st.code(main_py, language="python")

            st.markdown("---")

            # LangSmith Integration Instructions (Core Files mode only)
            if (
                st.session_state.get("enable_langsmith", False)
                and st.session_state.generation_mode == "core_files"
            ):
                st.markdown(
                    f"<h3>{icon_inline('activity', 20)} LangSmith Integration</h3>",
                    unsafe_allow_html=True,
                )
                st.info(
                    "**Core Files Mode**: LangSmith tracing requires manual setup in your existing project."
                )

                langsmith_project = st.session_state.get(
                    "langsmith_project", "my-crew-project"
                )

                st.markdown(f"""
**Follow these steps to enable LangSmith tracing:**

1. **Install the LangSmith package:**
   ```bash
   pip install langsmith
   ```

2. **Add environment variables to your `.env` file:**
   ```bash
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   LANGCHAIN_PROJECT={langsmith_project}
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_TRACING_V2=true
   ```

3. **Get your free API key:**
   - Visit [https://smith.langchain.com](https://smith.langchain.com)
   - Sign up (5,000 traces/month free)
   - Copy your API key and add it to `.env`

4. **Run your crew** - tracing will work automatically!

Traces will appear in your LangSmith dashboard for debugging and monitoring.
                """)
                st.markdown("---")
            st.markdown(
                f"<h3>{icon_inline('rocket', 20)} Next Steps</h3>",
                unsafe_allow_html=True,
            )

            if st.session_state.generation_mode == "core_files":
                st.markdown(f"""
1. **Extract the ZIP file** to your existing CrewAI project
2. **Copy the files** to your project structure:
   - Place `agents.yaml` and `tasks.yaml` in your `config/` directory
   - Place `crew.py` and `main.py` in your source directory
3. **Update imports** in your code if needed
4. **Configure your `.env`** file with required API keys
5. **Run your crew:**
   ```bash
   crewai run
   ```
                """)
            else:
                st.markdown(f"""
1. **Extract the ZIP file**
2. **Navigate to the project directory:**
   ```bash
   cd {project_name}
   ```
3. **Install dependencies:**
   ```bash
   crewai install
   ```
4. **Configure environment variables:**
   - Edit the `.env` file with your API keys
5. **Run your crew:**
   ```bash
   crewai run
   ```
                """)
