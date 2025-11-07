"""YAML generation for CrewAI configuration files."""

import yaml
from typing import Dict, List, Any


def generate_agents_yaml(agents: List[Dict[str, Any]]) -> str:
    """
    Generate agents.yaml content from agent configurations.

    Args:
        agents: List of agent configuration dictionaries

    Returns:
        YAML string for agents.yaml
    """
    agents_dict = {}

    for agent in agents:
        # Use role as the key (sanitized)
        agent_key = agent["role"].lower().replace(" ", "_")

        agent_config = {
            "role": agent["role"],
            "goal": agent["goal"],
            "backstory": agent["backstory"],
        }

        # Add optional fields if they differ from defaults or are explicitly set
        optional_fields = [
            "verbose", "allow_delegation", "max_iter", "max_rpm", "cache",
            "llm", "reasoning", "max_reasoning_attempts", "multimodal",
            "allow_code_execution", "code_execution_mode", "inject_date",
            "date_format", "max_tokens", "max_execution_time", "max_retry_limit",
            "respect_context_window", "use_system_prompt", "system_template",
            "prompt_template", "response_template", "function_calling_llm",
            "guardrail_max_retries",
        ]

        for field in optional_fields:
            if field in agent and agent[field] is not None:
                agent_config[field] = agent[field]

        agents_dict[agent_key] = agent_config

    # Convert to YAML with proper formatting
    yaml_content = yaml.dump(
        agents_dict,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )

    return yaml_content


def generate_tasks_yaml(tasks: List[Dict[str, Any]]) -> str:
    """
    Generate tasks.yaml content from task configurations.

    Args:
        tasks: List of task configuration dictionaries

    Returns:
        YAML string for tasks.yaml
    """
    tasks_dict = {}

    for i, task in enumerate(tasks):
        # Use name if provided, otherwise generate from index
        task_key = task.get("name", f"task_{i+1}")
        task_key = task_key.lower().replace(" ", "_")

        task_config = {
            "description": task["description"],
            "expected_output": task["expected_output"],
            "agent": task["agent"].lower().replace(" ", "_"),
        }

        # Add optional fields
        optional_fields = [
            "name", "context", "async_execution", "human_input", "markdown",
            "output_file", "create_directory", "guardrail_max_retries",
            "allow_crewai_trigger_context",
        ]

        for field in optional_fields:
            if field in task and task[field] is not None:
                # For context, convert agent names to keys
                if field == "context" and task[field]:
                    task_config[field] = [
                        ctx.lower().replace(" ", "_") for ctx in task[field]
                    ]
                else:
                    task_config[field] = task[field]

        tasks_dict[task_key] = task_config

    # Convert to YAML with proper formatting
    yaml_content = yaml.dump(
        tasks_dict,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    )

    return yaml_content


def generate_env_file(env_vars: Dict[str, str], enable_langsmith: bool = False, langsmith_project: str = "my-crew-project") -> str:
    """
    Generate .env file content.

    Args:
        env_vars: Dictionary of environment variable names and their placeholder values
        enable_langsmith: Whether to include LangSmith configuration
        langsmith_project: LangSmith project name

    Returns:
        String content for .env file
    """
    lines = [
        "# Environment Variables for CrewAI Project",
        "# Replace the placeholder values with your actual API keys",
        "",
    ]

    # Group by provider
    grouped_vars = {}
    for var, value in env_vars.items():
        provider = var.split("_")[0]
        if provider not in grouped_vars:
            grouped_vars[provider] = []
        grouped_vars[provider].append((var, value))

    for provider, vars_list in grouped_vars.items():
        lines.append(f"# {provider.capitalize()} Configuration")
        for var, value in vars_list:
            lines.append(f"{var}={value}")
        lines.append("")

    # Add LangSmith configuration if enabled
    if enable_langsmith:
        lines.extend([
            "# LangSmith Configuration (Observability)",
            "# Get your free API key at: https://smith.langchain.com",
            "LANGCHAIN_API_KEY=your_langsmith_api_key_here",
            f"LANGCHAIN_PROJECT={langsmith_project}",
            "LANGCHAIN_ENDPOINT=https://api.smith.langchain.com",
            "LANGCHAIN_TRACING_V2=true",
            ""
        ])

    return "\n".join(lines)


def generate_pyproject_toml(project_name: str, python_version: str = "3.10", enable_langsmith: bool = False) -> str:
    """
    Generate pyproject.toml for the project.

    Args:
        project_name: Name of the project
        python_version: Minimum Python version
        enable_langsmith: Whether to include LangSmith dependency

    Returns:
        String content for pyproject.toml
    """
    # Base dependencies
    dependencies = f'''python = "^{python_version}"
crewai = {{version = "^1.3.0", extras = ["tools"]}}
crewai-tools = "^1.3.0"'''

    # Add langsmith if enabled
    if enable_langsmith:
        dependencies += '\nlangsmith = "^0.1.0"'

    toml_content = f'''[tool.poetry]
name = "{project_name}"
version = "0.1.0"
description = "A CrewAI project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
{dependencies}

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
'''
    return toml_content


def generate_readme(project_name: str, description: str, enable_langsmith: bool = False) -> str:
    """
    Generate README.md for the project.

    Args:
        project_name: Name of the project
        description: Project description
        enable_langsmith: Whether to include LangSmith setup instructions

    Returns:
        String content for README.md
    """
    # LangSmith section (if enabled)
    langsmith_section = ""
    if enable_langsmith:
        langsmith_section = '''
## LangSmith Observability

This project includes LangSmith tracing for debugging and monitoring your AI agents.

### Setup

1. Get a free API key at [https://smith.langchain.com](https://smith.langchain.com) (5,000 traces/month free)
2. Edit `.env` and add your `LANGCHAIN_API_KEY`
3. Run your crew - traces will appear in your LangSmith dashboard

### View Traces

- Visit [https://smith.langchain.com](https://smith.langchain.com) to view execution traces
- Debug agent decisions, LLM calls, and token usage
- Compare runs and track performance over time

'''

    readme_content = f'''# {project_name}

{description}

## Installation

```bash
crewai install
```

## Configuration

1. Copy `.env.example` to `.env`
2. Add your API keys to the `.env` file
{langsmith_section}
## Usage

Run the crew:

```bash
crewai run
```

Train the crew:

```bash
crewai train <n_iterations> <training_data.pkl>
```

Replay a task:

```bash
crewai replay <task_id>
```

Test the crew:

```bash
crewai test <n_iterations> <eval_llm>
```

## Project Structure

- `src/{project_name}/`: Main project directory
  - `crew.py`: Crew configuration and orchestration
  - `main.py`: Entry point for running the crew
  - `config/`:
    - `agents.yaml`: Agent definitions
    - `tasks.yaml`: Task definitions
  - `tools/`: Custom tools directory
  - `knowledge/`: Knowledge base files

## Generated with Gunny

This project was generated using [Gunny](https://github.com/yourusername/gunny), a Streamlit app for creating CrewAI projects.
'''
    return readme_content


def generate_gitignore() -> str:
    """Generate .gitignore content."""
    return '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# CrewAI
.crewai/
training_data.pkl
*.log

# OS
.DS_Store
Thumbs.db
'''
