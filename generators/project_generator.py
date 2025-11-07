"""Complete project generation for CrewAI projects."""

import os
import io
import zipfile
from typing import Dict, List, Any
from generators.yaml_generator import (
    generate_agents_yaml,
    generate_tasks_yaml,
    generate_env_file,
    generate_pyproject_toml,
    generate_readme,
    generate_gitignore,
)
from generators.python_generator import (
    generate_crew_py,
    generate_main_py,
    generate_init_py,
)


def extract_input_variables(agents: List[Dict[str, Any]], tasks: List[Dict[str, Any]]) -> List[str]:
    """
    Extract placeholder variables from agent and task descriptions.

    Args:
        agents: List of agent configurations
        tasks: List of task configurations

    Returns:
        List of unique variable names found in {variable} format
    """
    variables = set()

    # Check agent descriptions
    for agent in agents:
        for field in ["role", "goal", "backstory"]:
            text = agent.get(field, "")
            # Simple regex-like extraction
            parts = text.split("{")
            for part in parts[1:]:
                if "}" in part:
                    var = part.split("}")[0]
                    variables.add(var)

    # Check task descriptions
    for task in tasks:
        for field in ["description", "expected_output"]:
            text = task.get(field, "")
            parts = text.split("{")
            for part in parts[1:]:
                if "}" in part:
                    var = part.split("}")[0]
                    variables.add(var)

    return sorted(list(variables))


def generate_project_structure(
    project_name: str,
    description: str,
    agents: List[Dict[str, Any]],
    tasks: List[Dict[str, Any]],
    crew_config: Dict[str, Any],
    tools_by_agent: Dict[str, List[str]],
    env_vars: Dict[str, str],
    python_version: str = "3.10",
    generation_mode: str = "complete_project"
) -> Dict[str, str]:
    """
    Generate complete project structure as a dictionary of file paths to contents.

    Args:
        project_name: Name of the project
        description: Project description
        agents: List of agent configurations
        tasks: List of task configurations
        crew_config: Crew configuration
        tools_by_agent: Dictionary mapping agent roles to their tools
        env_vars: Environment variables to include
        python_version: Minimum Python version
        generation_mode: "core_files" or "complete_project" (default: "complete_project")

    Returns:
        Dictionary mapping file paths to their contents
    """
    files = {}

    # Extract input variables
    input_vars = extract_input_variables(agents, tasks)

    # Source directory files
    src_dir = f"src/{project_name}"

    # Core files (always included)
    files[f"{src_dir}/crew.py"] = generate_crew_py(
        project_name, agents, tasks, crew_config, tools_by_agent
    )
    files[f"{src_dir}/main.py"] = generate_main_py(project_name, input_vars)

    # Config files (always included)
    files[f"{src_dir}/config/agents.yaml"] = generate_agents_yaml(agents)
    files[f"{src_dir}/config/tasks.yaml"] = generate_tasks_yaml(tasks)

    # Additional files only for complete project mode
    if generation_mode == "complete_project":
        # Root level files
        files[".gitignore"] = generate_gitignore()
        files["README.md"] = generate_readme(project_name, description)
        files["pyproject.toml"] = generate_pyproject_toml(project_name, python_version)
        files[".env"] = generate_env_file(env_vars)

        # Source directory __init__.py
        files[f"{src_dir}/__init__.py"] = generate_init_py(project_name)

        # Tools directory
        files[f"{src_dir}/tools/__init__.py"] = '"""\nCustom tools for the crew.\n"""\n'
        files[f"{src_dir}/tools/custom_tool.py"] = '''"""
Example custom tool.

You can create your own custom tools here.
"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the input argument")


class MyCustomTool(BaseTool):
    name: str = "My Custom Tool"
    description: str = "Description of what this tool does"
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        """Execute the tool."""
        # Implement your custom logic here
        return f"Processed: {argument}"
'''

        # Knowledge directory
        files[f"{src_dir}/knowledge/.gitkeep"] = ""
        files[f"{src_dir}/knowledge/README.md"] = """# Knowledge Base

Place your knowledge base files here:
- PDF documents
- Text files
- CSV files
- JSON files
- Excel files

These files can be used by agents to access domain-specific information.
"""

    return files


def create_zip_file(files: Dict[str, str], project_name: str) -> bytes:
    """
    Create a ZIP file containing all project files.

    Args:
        files: Dictionary mapping file paths to their contents
        project_name: Name of the project (used as root directory in ZIP)

    Returns:
        Bytes of the ZIP file
    """
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path, content in files.items():
            # Add project name as root directory
            full_path = os.path.join(project_name, file_path)
            zip_file.writestr(full_path, content)

    zip_buffer.seek(0)
    return zip_buffer.getvalue()


def save_project_to_disk(files: Dict[str, str], base_path: str):
    """
    Save project files to disk.

    Args:
        files: Dictionary mapping file paths to their contents
        base_path: Base directory where to save the project
    """
    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Write file
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)


def generate_project_summary(
    project_name: str,
    agents: List[Dict[str, Any]],
    tasks: List[Dict[str, Any]],
    crew_config: Dict[str, Any]
) -> str:
    """
    Generate a summary of the project configuration.

    Args:
        project_name: Name of the project
        agents: List of agent configurations
        tasks: List of task configurations
        crew_config: Crew configuration

    Returns:
        Formatted summary string
    """
    summary = f"""# Project Summary: {project_name}

## Configuration Overview

**Agents:** {len(agents)}
**Tasks:** {len(tasks)}
**Process:** {crew_config.get('process', 'sequential').capitalize()}

## Agents
"""

    for i, agent in enumerate(agents, 1):
        summary += f"\n### {i}. {agent['role']}\n"
        summary += f"- **Goal:** {agent['goal']}\n"
        summary += f"- **Backstory:** {agent['backstory'][:100]}...\n"

    summary += "\n## Tasks\n"

    for i, task in enumerate(tasks, 1):
        task_name = task.get('name', f'Task {i}')
        summary += f"\n### {i}. {task_name}\n"
        summary += f"- **Agent:** {task['agent']}\n"
        summary += f"- **Description:** {task['description'][:100]}...\n"
        if task.get('output_file'):
            summary += f"- **Output File:** {task['output_file']}\n"

    summary += "\n## Crew Configuration\n"
    summary += f"- **Process Type:** {crew_config.get('process', 'sequential').capitalize()}\n"
    summary += f"- **Memory:** {'Enabled' if crew_config.get('memory') else 'Disabled'}\n"
    summary += f"- **Planning:** {'Enabled' if crew_config.get('planning') else 'Disabled'}\n"
    summary += f"- **Verbose:** {'Enabled' if crew_config.get('verbose') else 'Disabled'}\n"

    return summary
