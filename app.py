"""
Gunny - CrewAI Project Generator

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

# Page configuration
st.set_page_config(
    page_title="Gunny - CrewAI Project Generator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
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

# Header
st.title("🎯 Gunny - CrewAI Project Generator")
st.markdown("### Build complete CrewAI projects with all configuration options")

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
        "Gunny is a comprehensive tool for generating CrewAI projects. "
        "Configure agents, tasks, and crews with all available options, "
        "then download your complete project ready to run."
    )

# Main tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📋 Project Info",
    "🤖 Agents",
    "📝 Tasks",
    "⚙️ Crew Config",
    "🔧 Tools",
    "📚 Knowledge",
    "🚀 Advanced",
    "👁️ Preview & Generate"
])

# Tab 1: Project Information
with tab1:
    st.header("Project Information")

    col1, col2 = st.columns(2)

    with col1:
        project_name = st.text_input(
            "Project Name *",
            value=st.session_state.get("project_name", ""),
            help="Name of your CrewAI project (use underscores for spaces)",
            placeholder="my_awesome_crew"
        )
        st.session_state.project_name = project_name

        python_version = st.selectbox(
            "Python Version",
            options=["3.10", "3.11", "3.12"],
            index=0,
            help="Minimum Python version for your project"
        )
        st.session_state.python_version = python_version

    with col2:
        project_description = st.text_area(
            "Project Description",
            value=st.session_state.get("project_description", ""),
            help="Brief description of what your crew does",
            placeholder="A crew of AI agents that..."
        )
        st.session_state.project_description = project_description

    st.markdown("---")
    st.markdown("### Project Structure Preview")
    st.code(f"""
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
""", language="text")

# Tab 2: Agents Configuration
with tab2:
    st.header("Agent Configuration")
    st.markdown("Configure your AI agents with roles, goals, and capabilities.")

    # Agent management buttons
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("➕ Add Agent"):
            st.session_state.agents.append({})
            st.rerun()

    with col2:
        if st.button("➖ Remove Last Agent") and len(st.session_state.agents) > 0:
            st.session_state.agents.pop()
            st.rerun()

    st.markdown("---")

    # Display agent forms
    if len(st.session_state.agents) == 0:
        st.info("👆 Click 'Add Agent' to create your first agent")
    else:
        for i in range(len(st.session_state.agents)):
            agent_config = agent_configuration_form(i, st.session_state.agents[i])
            st.session_state.agents[i] = agent_config

            # Tools for this agent
            with st.expander(f"🔧 Tools for Agent {i + 1}"):
                agent_role = agent_config.get("role", f"Agent {i+1}")
                current_tools = st.session_state.tools_by_agent.get(agent_role, [])

                st.write("Select tools for this agent (or configure all tools in the Tools tab)")

                # Quick tool selection
                selected = []
                cols = st.columns(3)
                common_tools = ["SerperDevTool", "FileReadTool", "WebsiteSearchTool"]

                for idx, tool_name in enumerate(common_tools):
                    with cols[idx % 3]:
                        if st.checkbox(
                            tool_name,
                            value=tool_name in current_tools,
                            key=f"agent_{i}_tool_{tool_name}"
                        ):
                            selected.append(tool_name)

                st.session_state.tools_by_agent[agent_role] = selected

            st.markdown("---")

# Tab 3: Tasks Configuration
with tab3:
    st.header("Task Configuration")
    st.markdown("Define tasks and assign them to agents.")

    # Get available agent roles
    available_agents = [agent.get("role", f"Agent {i+1}") for i, agent in enumerate(st.session_state.agents) if agent.get("role")]
    available_task_names = [task.get("name", f"task_{i+1}") for i, task in enumerate(st.session_state.tasks)]

    # Task management buttons
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("➕ Add Task"):
            st.session_state.tasks.append({})
            st.rerun()

    with col2:
        if st.button("➖ Remove Last Task") and len(st.session_state.tasks) > 0:
            st.session_state.tasks.pop()
            st.rerun()

    st.markdown("---")

    # Check if agents exist
    if len(available_agents) == 0:
        st.warning("⚠️ Please create at least one agent first in the Agents tab")
    elif len(st.session_state.tasks) == 0:
        st.info("👆 Click 'Add Task' to create your first task")
    else:
        for i in range(len(st.session_state.tasks)):
            # Get available tasks for context (excluding current task)
            context_tasks = [name for j, name in enumerate(available_task_names) if j != i]

            task_config = task_configuration_form(
                i,
                available_agents,
                context_tasks,
                st.session_state.tasks[i]
            )
            st.session_state.tasks[i] = task_config
            st.markdown("---")

# Tab 4: Crew Configuration
with tab4:
    st.header("Crew Configuration")
    st.markdown("Configure how your crew operates.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Basic Settings")

        crew_name = st.text_input(
            "Crew Name",
            value=st.session_state.crew_config.get("name", "crew"),
            help="Name for your crew instance"
        )
        st.session_state.crew_config["name"] = crew_name

        process = st.selectbox(
            "Process Type",
            options=list(PROCESS_TYPES.keys()),
            format_func=lambda x: f"{x.capitalize()} - {PROCESS_TYPES[x]}",
            help="How tasks are executed"
        )
        st.session_state.crew_config["process"] = process

        verbose = st.checkbox(
            "Verbose Mode",
            value=st.session_state.crew_config.get("verbose", False),
            help="Enable detailed logging"
        )
        st.session_state.crew_config["verbose"] = verbose

        cache = st.checkbox(
            "Enable Cache",
            value=st.session_state.crew_config.get("cache", True),
            help="Cache results for efficiency"
        )
        st.session_state.crew_config["cache"] = cache

    with col2:
        st.subheader("Advanced Settings")

        memory = st.checkbox(
            "Enable Memory",
            value=st.session_state.crew_config.get("memory", False),
            help="Enable short and long-term memory"
        )
        st.session_state.crew_config["memory"] = memory

        planning = st.checkbox(
            "Enable Planning",
            value=st.session_state.crew_config.get("planning", False),
            help="Enable autonomous planning"
        )
        st.session_state.crew_config["planning"] = planning

        max_rpm = st.number_input(
            "Max RPM",
            min_value=0,
            value=st.session_state.crew_config.get("max_rpm") or 0,
            help="Maximum requests per minute (0 = unlimited)"
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
            placeholder="gpt-4"
        )
        st.session_state.crew_config["manager_llm"] = manager_llm

# Tab 5: Tools Configuration
with tab5:
    st.header("Tools Configuration")
    st.markdown("Select tools available to your agents.")

    st.info(f"💡 Total tools available: {sum(len(tools) for tools in TOOLS_CATALOG.values())}")

    selected_tools = tools_selector(st.session_state.selected_tools)
    st.session_state.selected_tools = selected_tools

    if selected_tools:
        st.success(f"✅ {len(selected_tools)} tools selected")

        with st.expander("View Selected Tools"):
            for tool in selected_tools:
                st.write(f"- {tool}")

# Tab 6: Knowledge Configuration
with tab6:
    st.header("Knowledge Base Configuration")
    st.markdown("Add knowledge sources for your agents.")

    st.subheader("Knowledge Sources")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("➕ Add Knowledge Source"):
            st.session_state.knowledge_sources.append({"type": "String", "config": {}})
            st.rerun()

    st.markdown("---")

    if len(st.session_state.knowledge_sources) == 0:
        st.info("👆 Click 'Add Knowledge Source' to add knowledge to your crew")
    else:
        for i, source in enumerate(st.session_state.knowledge_sources):
            with st.expander(f"Knowledge Source {i + 1}", expanded=True):
                source_type = st.selectbox(
                    "Source Type",
                    options=KNOWLEDGE_SOURCE_TYPES,
                    index=KNOWLEDGE_SOURCE_TYPES.index(source.get("type", "String")),
                    key=f"knowledge_{i}_type"
                )
                source["type"] = source_type

                if source_type == "String":
                    content = st.text_area(
                        "Content",
                        value=source.get("config", {}).get("content", ""),
                        key=f"knowledge_{i}_content",
                        help="Direct text content"
                    )
                    source["config"] = {"content": content}
                else:
                    file_path = st.text_input(
                        "File Path",
                        value=source.get("config", {}).get("path", ""),
                        key=f"knowledge_{i}_path",
                        help=f"Path to {source_type} file in knowledge/ directory",
                        placeholder=f"knowledge/document.{source_type.lower()}"
                    )
                    source["config"] = {"path": file_path}

                if st.button("🗑️ Remove", key=f"knowledge_{i}_remove"):
                    st.session_state.knowledge_sources.pop(i)
                    st.rerun()

    st.markdown("---")
    st.subheader("Embedder Configuration")

    use_embedder = st.checkbox(
        "Configure Custom Embedder",
        value=st.session_state.get("use_embedder", False)
    )
    st.session_state.use_embedder = use_embedder

    if use_embedder:
        embedder_provider = st.selectbox(
            "Embedder Provider",
            options=EMBEDDER_PROVIDERS,
            help="Vector embedding provider"
        )
        st.session_state.embedder_provider = embedder_provider

# Tab 7: Advanced Configuration
with tab7:
    st.header("Advanced Configuration")

    st.subheader("Environment Variables")
    st.markdown("Configure API keys and environment variables")

    # Determine required env vars
    if st.session_state.agents:
        required_vars = check_required_env_vars(st.session_state.agents, st.session_state.selected_tools)

        if required_vars:
            st.info(f"Based on your configuration, you'll need: {', '.join(required_vars)}")

            for var in required_vars:
                placeholder = "your_api_key_here"
                current_value = st.session_state.env_vars.get(var, placeholder)

                env_value = st.text_input(
                    var,
                    value=current_value,
                    type="password",
                    help=f"API key for {var}",
                    key=f"env_{var}"
                )
                st.session_state.env_vars[var] = env_value
        else:
            st.info("No specific API keys detected. You can add custom environment variables below.")

    st.markdown("---")
    st.subheader("Custom Environment Variables")

    custom_var_name = st.text_input("Variable Name", key="custom_env_name")
    custom_var_value = st.text_input("Variable Value", type="password", key="custom_env_value")

    if st.button("Add Custom Variable"):
        if custom_var_name and custom_var_value:
            st.session_state.env_vars[custom_var_name] = custom_var_value
            st.success(f"Added {custom_var_name}")
        else:
            st.error("Please provide both name and value")

    st.markdown("---")
    st.subheader("Enterprise Features")

    enterprise_apps = st.multiselect(
        "Enterprise App Integrations",
        options=ENTERPRISE_APPS,
        help="Select enterprise applications to integrate"
    )
    st.session_state.enterprise_apps = enterprise_apps

    if enterprise_apps:
        st.info(f"Selected: {', '.join(enterprise_apps)}")

# Tab 8: Preview & Generate
with tab8:
    st.header("Preview & Generate Project")

    # Validation
    project_name = st.session_state.get("project_name", "")

    if not project_name:
        st.error("⚠️ Please provide a project name in the Project Info tab")
    elif len(st.session_state.agents) == 0:
        st.error("⚠️ Please create at least one agent")
    elif len(st.session_state.tasks) == 0:
        st.error("⚠️ Please create at least one task")
    else:
        # Validate configuration
        is_valid, errors = validate_complete_configuration(
            project_name,
            st.session_state.agents,
            st.session_state.tasks,
            st.session_state.crew_config
        )

        validation_messages(errors)

        if is_valid:
            st.markdown("---")

            # Generate preview
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📄 agents.yaml")
                agents_yaml = generate_agents_yaml(st.session_state.agents)
                st.code(agents_yaml, language="yaml")

            with col2:
                st.subheader("📄 tasks.yaml")
                tasks_yaml = generate_tasks_yaml(st.session_state.tasks)
                st.code(tasks_yaml, language="yaml")

            st.markdown("---")

            col3, col4 = st.columns(2)

            with col3:
                st.subheader("🐍 crew.py")
                crew_py = generate_crew_py(
                    project_name,
                    st.session_state.agents,
                    st.session_state.tasks,
                    st.session_state.crew_config,
                    st.session_state.tools_by_agent
                )
                st.code(crew_py, language="python")

            with col4:
                st.subheader("🐍 main.py")
                input_vars = []  # Extract from descriptions
                main_py = generate_main_py(project_name, input_vars)
                st.code(main_py, language="python")

            st.markdown("---")

            # Generate and download
            st.subheader("🎉 Generate Project")

            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                st.markdown("Your project is ready to be generated!")

            with col2:
                if st.button("📊 View Summary", use_container_width=True):
                    summary = generate_project_summary(
                        project_name,
                        st.session_state.agents,
                        st.session_state.tasks,
                        st.session_state.crew_config
                    )
                    st.markdown(summary)

            with col3:
                # Generate project files
                project_files = generate_project_structure(
                    project_name,
                    st.session_state.project_description,
                    st.session_state.agents,
                    st.session_state.tasks,
                    st.session_state.crew_config,
                    st.session_state.tools_by_agent,
                    st.session_state.env_vars,
                    st.session_state.get("python_version", "3.10")
                )

                # Create ZIP file
                zip_data = create_zip_file(project_files, project_name)

                st.download_button(
                    label="⬇️ Download ZIP",
                    data=zip_data,
                    file_name=f"{project_name}.zip",
                    mime="application/zip",
                    use_container_width=True
                )

            st.success("✅ Project generated successfully! Download the ZIP file and extract it to get started.")

            st.markdown("---")
            st.subheader("🚀 Next Steps")
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

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center'>Made with ❤️ using Streamlit | "
    "Powered by CrewAI | <a href='https://github.com/yourusername/gunny'>GitHub</a></div>",
    unsafe_allow_html=True
)
