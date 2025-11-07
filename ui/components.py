"""Reusable UI components for the Gunny Streamlit app."""

import streamlit as st
from typing import Dict, List, Any, Optional
from ui.icons import icon_inline
from utils.constants import (
    TOOLS_CATALOG,
    LLM_PROVIDERS,
    EMBEDDER_PROVIDERS,
    CODE_EXECUTION_MODES,
    ENTERPRISE_APPS,
    DEFAULT_AGENT_CONFIG,
    DEFAULT_TASK_CONFIG,
)


def agent_configuration_form(agent_index: int, agent_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Render agent configuration form.

    Args:
        agent_index: Index of the agent (for unique keys)
        agent_data: Existing agent data to populate form

    Returns:
        Dictionary containing agent configuration
    """
    if agent_data is None:
        agent_data = {}

    st.subheader(f"Agent {agent_index + 1}")

    with st.expander("Basic Configuration", expanded=True):
        role = st.text_input(
            "Role *",
            value=agent_data.get("role", ""),
            key=f"agent_{agent_index}_role",
            help="The role of the agent (e.g., 'Senior Researcher', 'Content Writer')"
        )

        goal = st.text_area(
            "Goal *",
            value=agent_data.get("goal", ""),
            key=f"agent_{agent_index}_goal",
            help="The objective this agent is trying to achieve"
        )

        backstory = st.text_area(
            "Backstory *",
            value=agent_data.get("backstory", ""),
            key=f"agent_{agent_index}_backstory",
            help="Background story that gives context to the agent's expertise"
        )

    with st.expander("Execution Settings"):
        col1, col2 = st.columns(2)
        with col1:
            verbose = st.checkbox(
                "Verbose",
                value=agent_data.get("verbose", DEFAULT_AGENT_CONFIG["verbose"]),
                key=f"agent_{agent_index}_verbose",
                help="Enable detailed logging"
            )

            cache = st.checkbox(
                "Cache",
                value=agent_data.get("cache", DEFAULT_AGENT_CONFIG["cache"]),
                key=f"agent_{agent_index}_cache",
                help="Enable caching of tool results"
            )

            allow_delegation = st.checkbox(
                "Allow Delegation",
                value=agent_data.get("allow_delegation", DEFAULT_AGENT_CONFIG["allow_delegation"]),
                key=f"agent_{agent_index}_allow_delegation",
                help="Allow this agent to delegate tasks to other agents"
            )

        with col2:
            max_iter = st.number_input(
                "Max Iterations",
                min_value=1,
                value=agent_data.get("max_iter", DEFAULT_AGENT_CONFIG["max_iter"]),
                key=f"agent_{agent_index}_max_iter",
                help="Maximum number of iterations for task execution"
            )

            max_retry_limit = st.number_input(
                "Max Retry Limit",
                min_value=0,
                value=agent_data.get("max_retry_limit", DEFAULT_AGENT_CONFIG["max_retry_limit"]),
                key=f"agent_{agent_index}_max_retry_limit",
                help="Maximum number of retries on error"
            )

    with st.expander("LLM Configuration"):
        llm_provider = st.selectbox(
            "LLM Provider",
            options=list(LLM_PROVIDERS.keys()),
            key=f"agent_{agent_index}_llm_provider",
            help="Select the LLM provider for this agent"
        )

        if llm_provider in LLM_PROVIDERS:
            llm_model = st.selectbox(
                "Model",
                options=LLM_PROVIDERS[llm_provider],
                key=f"agent_{agent_index}_llm_model",
                help="Select the specific model"
            )

            if llm_model == "Enter custom model name":
                llm_model = st.text_input(
                    "Custom Model Name",
                    key=f"agent_{agent_index}_llm_custom"
                )

    with st.expander("Advanced AI Features"):
        col1, col2 = st.columns(2)
        with col1:
            reasoning = st.checkbox(
                "Enable Reasoning",
                value=agent_data.get("reasoning", DEFAULT_AGENT_CONFIG["reasoning"]),
                key=f"agent_{agent_index}_reasoning",
                help="Enable reflection and planning before execution"
            )

            multimodal = st.checkbox(
                "Enable Multimodal",
                value=agent_data.get("multimodal", DEFAULT_AGENT_CONFIG["multimodal"]),
                key=f"agent_{agent_index}_multimodal",
                help="Enable multimodal capabilities (images, etc.)"
            )

        with col2:
            allow_code_execution = st.checkbox(
                "Allow Code Execution",
                value=agent_data.get("allow_code_execution", DEFAULT_AGENT_CONFIG["allow_code_execution"]),
                key=f"agent_{agent_index}_code_exec",
                help="Allow agent to execute code"
            )

            if allow_code_execution:
                code_execution_mode = st.selectbox(
                    "Code Execution Mode",
                    options=list(CODE_EXECUTION_MODES.keys()),
                    key=f"agent_{agent_index}_code_mode",
                    help=CODE_EXECUTION_MODES.get("safe", "")
                )

    # Compile agent data
    agent_config = {
        "role": role,
        "goal": goal,
        "backstory": backstory,
        "verbose": verbose,
        "cache": cache,
        "allow_delegation": allow_delegation,
        "max_iter": max_iter,
        "max_retry_limit": max_retry_limit,
        "llm": llm_model if llm_provider != "Other" else None,
        "reasoning": reasoning,
        "multimodal": multimodal,
        "allow_code_execution": allow_code_execution,
    }

    if allow_code_execution:
        agent_config["code_execution_mode"] = code_execution_mode

    return agent_config


def task_configuration_form(
    task_index: int,
    available_agents: List[str],
    available_tasks: List[str],
    task_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Render task configuration form.

    Args:
        task_index: Index of the task (for unique keys)
        available_agents: List of available agent roles
        available_tasks: List of available task names for context
        task_data: Existing task data to populate form

    Returns:
        Dictionary containing task configuration
    """
    if task_data is None:
        task_data = {}

    st.subheader(f"Task {task_index + 1}")

    with st.expander("Basic Configuration", expanded=True):
        name = st.text_input(
            "Task Name",
            value=task_data.get("name", f"task_{task_index + 1}"),
            key=f"task_{task_index}_name",
            help="Unique identifier for this task"
        )

        description = st.text_area(
            "Description *",
            value=task_data.get("description", ""),
            key=f"task_{task_index}_description",
            height=100,
            help="Detailed description of what this task should accomplish. Use {variable} for dynamic inputs."
        )

        expected_output = st.text_area(
            "Expected Output *",
            value=task_data.get("expected_output", ""),
            key=f"task_{task_index}_expected_output",
            help="Clear definition of what the output should look like"
        )

        if available_agents:
            agent = st.selectbox(
                "Assigned Agent *",
                options=available_agents,
                key=f"task_{task_index}_agent",
                index=available_agents.index(task_data["agent"]) if task_data.get("agent") in available_agents else 0,
                help="Which agent should execute this task"
            )
        else:
            st.warning("No agents available. Please create at least one agent first.")
            agent = None

    with st.expander("Dependencies & Execution"):
        col1, col2 = st.columns(2)

        with col1:
            if len(available_tasks) > 0:
                context = st.multiselect(
                    "Context Tasks",
                    options=available_tasks,
                    default=task_data.get("context", []),
                    key=f"task_{task_index}_context",
                    help="Other tasks whose outputs should be available as context"
                )
            else:
                context = []

            async_execution = st.checkbox(
                "Async Execution",
                value=task_data.get("async_execution", DEFAULT_TASK_CONFIG["async_execution"]),
                key=f"task_{task_index}_async",
                help="Execute this task asynchronously"
            )

        with col2:
            human_input = st.checkbox(
                "Human Input",
                value=task_data.get("human_input", DEFAULT_TASK_CONFIG["human_input"]),
                key=f"task_{task_index}_human",
                help="Require human review before completing"
            )

    with st.expander("Output Settings"):
        markdown = st.checkbox(
            "Markdown Output",
            value=task_data.get("markdown", DEFAULT_TASK_CONFIG["markdown"]),
            key=f"task_{task_index}_markdown",
            help="Format output as markdown"
        )

        output_file = st.text_input(
            "Output File",
            value=task_data.get("output_file", ""),
            key=f"task_{task_index}_output_file",
            help="Path to save the output (e.g., 'output/report.md')"
        )

    # Compile task data
    task_config = {
        "name": name,
        "description": description,
        "expected_output": expected_output,
        "agent": agent,
        "context": context if context else None,
        "async_execution": async_execution,
        "human_input": human_input,
        "markdown": markdown,
        "output_file": output_file if output_file else None,
    }

    return task_config


def tools_selector(selected_tools: List[str] = None) -> List[str]:
    """
    Render tools selection interface.

    Args:
        selected_tools: List of currently selected tools

    Returns:
        List of selected tool names
    """
    if selected_tools is None:
        selected_tools = []

    st.write("### Select Tools")

    # Search functionality
    search_query = st.text_input(
        "Search tools",
        placeholder="Type to search tools...",
        key="tool_search"
    )

    selected = []

    # Display tools by category
    for category, tools in TOOLS_CATALOG.items():
        with st.expander(f"{category} ({len(tools)} tools)"):
            for tool in tools:
                # Filter by search query
                if search_query and search_query.lower() not in tool["name"].lower() and search_query.lower() not in tool["description"].lower():
                    continue

                # Create unique key by including category to avoid duplicates
                category_key = category.replace("/", "_").replace(" ", "_").lower()
                is_selected = st.checkbox(
                    f"**{tool['name']}**",
                    value=tool["name"] in selected_tools,
                    key=f"tool_{category_key}_{tool['name']}",
                    help=tool["description"]
                )

                if is_selected:
                    selected.append(tool["name"])

    return selected


def code_preview(title: str, code: str, language: str = "yaml"):
    """
    Display code preview with syntax highlighting.

    Args:
        title: Title of the code block
        code: Code content
        language: Programming language for syntax highlighting
    """
    st.write(f"### {title}")
    st.code(code, language=language)


def validation_messages(errors: Dict[str, List[str]]):
    """
    Display validation error messages.

    Args:
        errors: Dictionary of error categories to error messages
    """
    has_errors = any(len(errs) > 0 for errs in errors.values())

    if not has_errors:
        st.success("✅ Configuration is valid!")
        return

    st.error("❌ Configuration has errors:")

    for category, error_list in errors.items():
        if error_list:
            st.write(f"**{category.capitalize()} Errors:**")
            for error in error_list:
                st.write(f"- {error}")
