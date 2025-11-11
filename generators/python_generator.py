"""Python code generation for CrewAI project files."""

from typing import Dict, List, Any, Tuple


def generate_crew_py(
    project_name: str,
    agents: List[Dict[str, Any]],
    tasks: List[Dict[str, Any]],
    crew_config: Dict[str, Any],
    tools_by_agent: Dict[str, List[str]]
) -> str:
    """
    Generate crew.py file content.

    Args:
        project_name: Name of the project
        agents: List of agent configurations
        tasks: List of task configurations
        crew_config: Crew configuration dictionary
        tools_by_agent: Dictionary mapping agent roles to their tools

    Returns:
        String content for crew.py
    """
    class_name = "".join(word.capitalize() for word in project_name.split("_"))

    # Collect all unique tools needed
    all_tools = set()
    for tools_list in tools_by_agent.values():
        all_tools.update(tools_list)

    # Generate tool imports
    tool_imports = []
    if all_tools:
        tool_imports.append("from crewai_tools import (")
        for tool in sorted(all_tools):
            tool_imports.append(f"    {tool},")
        tool_imports.append(")")

    imports_section = "\n".join(tool_imports) if tool_imports else ""

    # Generate agent methods
    agent_methods = []
    for agent in agents:
        agent_key = agent["role"].lower().replace(" ", "_")
        agent_method = f'''    @agent
    def {agent_key}(self) -> Agent:
        """Create {agent['role']} agent."""
        return Agent(
            config=self.agents_config['{agent_key}'],'''

        # Add tools if any
        agent_tools = tools_by_agent.get(agent["role"], [])
        if agent_tools:
            agent_method += "\n            tools=["
            for tool in agent_tools:
                agent_method += f"\n                {tool}(),"
            agent_method += "\n            ],"

        # Add optional parameters
        if agent.get("verbose"):
            agent_method += "\n            verbose=True,"
        if agent.get("allow_delegation"):
            agent_method += "\n            allow_delegation=True,"
        if agent.get("max_iter") and agent["max_iter"] != 25:
            agent_method += f"\n            max_iter={agent['max_iter']},"
        if agent.get("cache") is False:
            agent_method += "\n            cache=False,"

        agent_method += "\n        )"

        agent_methods.append(agent_method)

    agents_code = "\n\n".join(agent_methods)

    # Generate task methods
    task_methods = []
    for i, task in enumerate(tasks):
        task_key = task.get("name", f"task_{i+1}").lower().replace(" ", "_")
        task_method = f'''    @task
    def {task_key}(self) -> Task:
        """Create {task.get('name', f'Task {i+1}')}."""
        return Task(
            config=self.tasks_config['{task_key}'],'''

        # Add output file if specified
        if task.get("output_file"):
            task_method += f"\n            output_file='{task['output_file']}',"

        task_method += "\n        )"

        task_methods.append(task_method)

    tasks_code = "\n\n".join(task_methods)

    # Generate crew method
    process = crew_config.get("process", "sequential")
    crew_method = f'''    @crew
    def crew(self) -> Crew:
        """Create the {project_name} crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.{process},'''

    if crew_config.get("verbose"):
        crew_method += "\n            verbose=True,"
    if crew_config.get("memory"):
        crew_method += "\n            memory=True,"
    if crew_config.get("planning"):
        crew_method += "\n            planning=True,"
    if crew_config.get("max_rpm"):
        crew_method += f"\n            max_rpm={crew_config['max_rpm']},"
    if crew_config.get("manager_llm"):
        crew_method += f"\n            manager_llm='{crew_config['manager_llm']}',"

    crew_method += "\n        )"

    # Combine everything
    content = f'''"""
{project_name.replace("_", " ").title()} Crew
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
{imports_section}


@CrewBase
class {class_name}Crew:
    """
    {project_name.replace("_", " ").title()} crew for orchestrating AI agents.
    """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

{agents_code}

{tasks_code}

{crew_method}
'''

    return content


def generate_main_py(project_name: str, input_variables: List[str]) -> str:
    """
    Generate main.py file content.

    Args:
        project_name: Name of the project
        input_variables: List of input variable names used in descriptions

    Returns:
        String content for main.py
    """
    class_name = "".join(word.capitalize() for word in project_name.split("_"))

    # Generate example inputs
    example_inputs = {}
    for var in input_variables:
        example_inputs[var] = f"your_{var}_here"

    inputs_code = "{\n"
    for var in input_variables:
        inputs_code += f"        '{var}': 'your_{var}_here',\n"
    inputs_code += "    }"

    content = f'''#!/usr/bin/env python
"""
Main entry point for the {project_name.replace("_", " ").title()} crew.
"""

import sys
from {project_name}.crew import {class_name}Crew


def run():
    """
    Run the crew with custom inputs.
    """
    inputs = {inputs_code}
    {class_name}Crew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.

    Usage:
        python main.py train <n_iterations> <training_data.pkl>
    """
    if len(sys.argv) < 3:
        print("Usage: python main.py train <n_iterations> <training_data.pkl>")
        sys.exit(1)

    n_iterations = int(sys.argv[1])
    filename = sys.argv[2]

    inputs = {inputs_code}

    try:
        {class_name}Crew().crew().train(
            n_iterations=n_iterations,
            filename=filename,
            inputs=inputs
        )
        print(f"Training completed! Model saved to {{filename}}")
    except Exception as e:
        print(f"Error during training: {{e}}")
        raise


def replay():
    """
    Replay the crew execution from a specific task.

    Usage:
        python main.py replay <task_id>
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py replay <task_id>")
        sys.exit(1)

    task_id = sys.argv[1]

    try:
        {class_name}Crew().crew().replay(task_id=task_id)
    except Exception as e:
        print(f"Error during replay: {{e}}")
        raise


def test():
    """
    Test the crew for a given number of iterations.

    Usage:
        python main.py test <n_iterations> <eval_llm>
    """
    if len(sys.argv) < 3:
        print("Usage: python main.py test <n_iterations> <eval_llm>")
        sys.exit(1)

    n_iterations = int(sys.argv[1])
    eval_llm = sys.argv[2]

    inputs = {inputs_code}

    try:
        {class_name}Crew().crew().test(
            n_iterations=n_iterations,
            eval_llm=eval_llm,
            inputs=inputs
        )
        print(f"Testing completed!")
    except Exception as e:
        print(f"Error during testing: {{e}}")
        raise


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "train":
            train()
        elif command == "replay":
            replay()
        elif command == "test":
            test()
        else:
            print(f"Unknown command: {{command}}")
            print("Available commands: train, replay, test")
            sys.exit(1)
    else:
        run()
'''

    return content


def generate_custom_tool(tool_name: str, tool_description: str) -> str:
    """
    Generate a custom tool template.

    Args:
        tool_name: Name of the custom tool
        tool_description: Description of what the tool does

    Returns:
        String content for custom tool file
    """
    class_name = "".join(word.capitalize() for word in tool_name.split("_"))

    content = f'''"""
Custom tool: {tool_name}
"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class {class_name}Input(BaseModel):
    """Input schema for {class_name}."""
    argument: str = Field(..., description="Description of the input argument")


class {class_name}(BaseTool):
    name: str = "{tool_name}"
    description: str = "{tool_description}"
    args_schema: Type[BaseModel] = {class_name}Input

    def _run(self, argument: str) -> str:
        """
        Execute the tool.

        Args:
            argument: Input argument for the tool

        Returns:
            Result of the tool execution
        """
        # TODO: Implement your tool logic here
        result = f"Processed: {{argument}}"
        return result
'''

    return content


def generate_init_py(project_name: str) -> str:
    """Generate __init__.py for the project package."""
    return f'''"""
{project_name.replace("_", " ").title()} Package
"""

from {project_name}.crew import {("".join(word.capitalize() for word in project_name.split("_")))}Crew

__all__ = ['{("".join(word.capitalize() for word in project_name.split("_")))}Crew']
'''


def generate_tool_stubs(
    selected_tools: List[str],
    tools_catalog: Dict[str, List[Dict[str, Any]]]
) -> List[Tuple[str, str]]:
    """
    Generate tool stub files based on selected tools.

    Args:
        selected_tools: List of selected tool names
        tools_catalog: Complete tools catalog from constants.py

    Returns:
        List of tuples (filename, content) for each tool stub
    """
    if not selected_tools:
        # Return generic custom tool template if no tools selected
        return [("custom_tool.py", _generate_generic_tool_template())]

    tool_stubs = []

    # Create a lookup dictionary for tools
    tools_lookup = {}
    for category, tools in tools_catalog.items():
        for tool in tools:
            tools_lookup[tool["name"]] = {
                "category": category,
                **tool
            }

    # Generate stub for each selected tool
    for tool_name in selected_tools:
        if tool_name not in tools_lookup:
            continue

        tool_info = tools_lookup[tool_name]
        stub_content = _generate_tool_stub(tool_name, tool_info)

        # Create filename: tool_name_tool.py (sanitized)
        filename = f"{tool_name.lower().replace('tool', '').rstrip('_')}_tool.py"
        tool_stubs.append((filename, stub_content))

    # Always include a generic template as well
    tool_stubs.append(("custom_tool.py", _generate_generic_tool_template()))

    return tool_stubs


def _generate_generic_tool_template() -> str:
    """Generate a generic custom tool template."""
    return '''"""
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


def _generate_tool_stub(tool_name: str, tool_info: Dict[str, Any]) -> str:
    """
    Generate a stub file for a specific tool.

    Args:
        tool_name: Name of the tool
        tool_info: Tool information from catalog including category, description, requires_auth, env_vars

    Returns:
        String content for the tool stub file
    """
    description = tool_info.get("description", "")
    requires_auth = tool_info.get("requires_auth", False)
    env_vars = tool_info.get("env_vars", [])
    auth_note = tool_info.get("auth_note", "")
    category = tool_info.get("category", "Unknown")

    # Build authentication section
    auth_section = ""
    if requires_auth and env_vars:
        auth_section = f"""
## Authentication Required

This tool requires the following environment variables:
{chr(10).join(f"- {var}" for var in env_vars)}
"""
        if auth_note:
            auth_section += f"""
{auth_note}
"""

    # Generate the stub content
    content = f'''"""
{tool_name} - {category}

{description}
{auth_section}
## Usage Example

```python
from crewai_tools import {tool_name}

# Initialize the tool'''

    if requires_auth and env_vars:
        content += f'''
# Make sure environment variables are set:
'''
        for var in env_vars:
            content += f'''
# {var} = "your_{var.lower()}_here"
'''

    content += f'''

tool = {tool_name}()

# Use in agent configuration:
# tools=[{tool_name}()]
```

## Configuration

To use this tool in your agents, import it and add to the tools list:

```python
from crewai_tools import {tool_name}

@agent
def my_agent(self) -> Agent:
    return Agent(
        config=self.agents_config['my_agent'],
        tools=[{tool_name}()],  # Add tool here
        verbose=True
    )
```
"""

# Import statement for reference
from crewai_tools import {tool_name}

# Tool is ready to use - no additional configuration needed in this file
# Simply import and use in your crew.py agent definitions
'''

    return content
