"""Validation functions for CrewAI configurations."""

from typing import Dict, List, Any, Tuple


def validate_agent_config(agent_config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validate agent configuration.

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    # Check required fields
    if not agent_config.get("role"):
        errors.append("Agent role is required")
    if not agent_config.get("goal"):
        errors.append("Agent goal is required")
    if not agent_config.get("backstory"):
        errors.append("Agent backstory is required")

    # Validate numeric fields
    if agent_config.get("max_iter") and agent_config["max_iter"] < 1:
        errors.append("max_iter must be at least 1")
    if agent_config.get("max_rpm") and agent_config["max_rpm"] < 1:
        errors.append("max_rpm must be at least 1")
    if agent_config.get("max_retry_limit") and agent_config["max_retry_limit"] < 0:
        errors.append("max_retry_limit must be non-negative")
    if agent_config.get("guardrail_max_retries") and agent_config["guardrail_max_retries"] < 0:
        errors.append("guardrail_max_retries must be non-negative")

    # Validate code execution mode
    if agent_config.get("code_execution_mode") and agent_config["code_execution_mode"] not in ["safe", "unsafe"]:
        errors.append("code_execution_mode must be 'safe' or 'unsafe'")

    return len(errors) == 0, errors


def validate_task_config(task_config: Dict[str, Any], available_agents: List[str]) -> Tuple[bool, List[str]]:
    """
    Validate task configuration.

    Args:
        task_config: Task configuration dictionary
        available_agents: List of available agent names

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    # Check required fields
    if not task_config.get("description"):
        errors.append("Task description is required")
    if not task_config.get("expected_output"):
        errors.append("Task expected_output is required")
    if not task_config.get("agent"):
        errors.append("Task must be assigned to an agent")
    elif task_config["agent"] not in available_agents:
        errors.append(f"Task assigned to unknown agent: {task_config['agent']}")

    # Validate context references
    if task_config.get("context"):
        for context_task in task_config["context"]:
            if not isinstance(context_task, str):
                errors.append("Context task references must be task names (strings)")

    # Validate guardrail retries
    if task_config.get("guardrail_max_retries") and task_config["guardrail_max_retries"] < 0:
        errors.append("guardrail_max_retries must be non-negative")

    return len(errors) == 0, errors


def validate_crew_config(crew_config: Dict[str, Any], has_agents: bool, has_tasks: bool) -> Tuple[bool, List[str]]:
    """
    Validate crew configuration.

    Args:
        crew_config: Crew configuration dictionary
        has_agents: Whether any agents are configured
        has_tasks: Whether any tasks are configured

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    # Check that agents and tasks exist
    if not has_agents:
        errors.append("Crew must have at least one agent")
    if not has_tasks:
        errors.append("Crew must have at least one task")

    # Validate process type
    if crew_config.get("process") not in ["sequential", "hierarchical"]:
        errors.append("Process must be 'sequential' or 'hierarchical'")

    # Check hierarchical process requirements
    if crew_config.get("process") == "hierarchical":
        if not crew_config.get("manager_llm") and not crew_config.get("manager_agent"):
            errors.append("Hierarchical process requires either manager_llm or manager_agent")

    # Validate max_rpm
    if crew_config.get("max_rpm") and crew_config["max_rpm"] < 1:
        errors.append("max_rpm must be at least 1")

    return len(errors) == 0, errors


def validate_project_name(name: str) -> Tuple[bool, str]:
    """
    Validate project name.

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return False, "Project name is required"

    if not name.replace("_", "").replace("-", "").isalnum():
        return False, "Project name can only contain letters, numbers, hyphens, and underscores"

    if name[0].isdigit():
        return False, "Project name cannot start with a number"

    if len(name) > 100:
        return False, "Project name must be 100 characters or less"

    return True, ""


def validate_tool_selection(selected_tools: List[str], all_tools: List[str]) -> Tuple[bool, List[str]]:
    """
    Validate selected tools exist in the available tools catalog.

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    for tool in selected_tools:
        if tool not in all_tools:
            errors.append(f"Unknown tool: {tool}")

    return len(errors) == 0, errors


def check_required_env_vars(agents_config: List[Dict[str, Any]], tasks_tools: List[str], enable_langsmith: bool = False) -> List[str]:
    """
    Determine which environment variables are required based on configuration.

    Args:
        agents_config: List of agent configurations
        tasks_tools: List of selected tools
        enable_langsmith: Whether LangSmith tracing is enabled

    Returns:
        List of required environment variable names
    """
    required_vars = set()

    # Check LLM requirements
    for agent in agents_config:
        llm = agent.get("llm", "")
        if "gpt" in llm or "openai" in llm:
            required_vars.add("OPENAI_API_KEY")
        elif "claude" in llm or "anthropic" in llm:
            required_vars.add("ANTHROPIC_API_KEY")
        elif "gemini" in llm or "google" in llm:
            required_vars.add("GOOGLE_API_KEY")
        elif "azure" in llm:
            required_vars.add("AZURE_OPENAI_API_KEY")
            required_vars.add("AZURE_OPENAI_ENDPOINT")

    # Check tool requirements
    from utils.constants import TOOL_ENV_REQUIREMENTS
    for tool in tasks_tools:
        if tool in TOOL_ENV_REQUIREMENTS:
            required_vars.update(TOOL_ENV_REQUIREMENTS[tool])

    # Check LangSmith requirements
    if enable_langsmith:
        required_vars.add("LANGCHAIN_API_KEY")
        required_vars.add("LANGCHAIN_PROJECT")

    return sorted(list(required_vars))


def validate_complete_configuration(
    project_name: str,
    agents: List[Dict[str, Any]],
    tasks: List[Dict[str, Any]],
    crew_config: Dict[str, Any]
) -> Tuple[bool, Dict[str, List[str]]]:
    """
    Validate entire project configuration.

    Returns:
        Tuple of (is_valid, dict_of_errors_by_category)
    """
    all_errors = {
        "project": [],
        "agents": [],
        "tasks": [],
        "crew": [],
    }

    # Validate project name
    name_valid, name_error = validate_project_name(project_name)
    if not name_valid:
        all_errors["project"].append(name_error)

    # Validate agents
    agent_names = []
    for i, agent in enumerate(agents):
        valid, errors = validate_agent_config(agent)
        if not valid:
            all_errors["agents"].extend([f"Agent {i+1}: {err}" for err in errors])
        if agent.get("role"):
            agent_names.append(agent["role"])

    # Validate tasks
    for i, task in enumerate(tasks):
        valid, errors = validate_task_config(task, agent_names)
        if not valid:
            all_errors["tasks"].extend([f"Task {i+1}: {err}" for err in errors])

    # Validate crew
    valid, errors = validate_crew_config(crew_config, len(agents) > 0, len(tasks) > 0)
    if not valid:
        all_errors["crew"].extend(errors)

    # Check if any errors exist
    has_errors = any(len(errors) > 0 for errors in all_errors.values())

    return not has_errors, all_errors
