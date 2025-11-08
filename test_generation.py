"""
Test script for Gunny project generation with CrewAI 1.4.1
"""

from generators.yaml_generator import generate_agents_yaml, generate_tasks_yaml
from generators.python_generator import generate_crew_py, generate_main_py
from generators.project_generator import generate_project_structure, create_zip_file
from utils.constants import DEFAULT_AGENT_CONFIG, DEFAULT_TASK_CONFIG, DEFAULT_CREW_CONFIG
import os

print("=== PHASE 2: CONFIGURATION & GENERATION TESTING ===\n")

# Test configuration
project_name = "test_crew_1_4_1"
project_description = "Test project for validating Gunny with CrewAI 1.4.1"

# Configure 2 agents
agents = [
    {
        **DEFAULT_AGENT_CONFIG,
        "role": "Research Agent",
        "goal": "Conduct thorough research on the provided topic",
        "backstory": "An expert researcher with 10 years of experience in finding accurate information",
        "llm": "gpt-4",
        "llm_provider": "OpenAI",
        "verbose": True,
        "allow_delegation": False,
    },
    {
        **DEFAULT_AGENT_CONFIG,
        "role": "Analysis Agent",
        "goal": "Analyze research findings and create insights",
        "backstory": "A data analyst specialized in pattern recognition and insight extraction",
        "llm": "claude-3-sonnet-20240229",
        "llm_provider": "Anthropic",
        "verbose": True,
        "allow_delegation": False,
    }
]

# Configure 2 tasks
tasks = [
    {
        **DEFAULT_TASK_CONFIG,
        "name": "research_task",
        "description": "Research the topic: {topic} and gather comprehensive information",
        "expected_output": "A detailed research report with at least 5 key findings",
        "agent": "Research Agent",
        "async_execution": False,
    },
    {
        **DEFAULT_TASK_CONFIG,
        "name": "analysis_task",
        "description": "Analyze the research findings and extract actionable insights",
        "expected_output": "An analysis report with insights and recommendations",
        "agent": "Analysis Agent",
        "context": ["research_task"],
        "async_execution": False,
    }
]

# Crew configuration
crew_config = {
    **DEFAULT_CREW_CONFIG,
    "process": "sequential",
    "verbose": True,
    "memory": True,
    "cache": True,
}

# Selected tools
selected_tools = ["FileReadTool", "SerperDevTool", "BraveSearchTool"]

# Tools by agent (optional fine-grained control)
tools_by_agent = {}

# Environment variables
env_vars = {
    "OPENAI_API_KEY": "your_openai_api_key_here",
    "ANTHROPIC_API_KEY": "your_anthropic_api_key_here",
    "SERPER_API_KEY": "your_serper_api_key_here",
    "BRAVE_API_KEY": "your_brave_api_key_here",
}

print("✓ Test Configuration:")
print(f"  - Project: {project_name}")
print(f"  - Agents: {len(agents)}")
print(f"  - Tasks: {len(tasks)}")
print(f"  - Process: {crew_config['process']}")
print(f"  - Tools: {len(selected_tools)}")
print()

# Generate YAML files
print("Generating YAML files...")
agents_yaml = generate_agents_yaml(agents)
tasks_yaml = generate_tasks_yaml(tasks)
print("✓ YAML files generated")

# Validate YAML syntax
import yaml
try:
    yaml.safe_load(agents_yaml)
    print("✓ agents.yaml is valid YAML")
except yaml.YAMLError as e:
    print(f"❌ agents.yaml YAML error: {e}")

try:
    yaml.safe_load(tasks_yaml)
    print("✓ tasks.yaml is valid YAML")
except yaml.YAMLError as e:
    print(f"❌ tasks.yaml YAML error: {e}")

# Generate Python files
print("\nGenerating Python files...")
crew_py = generate_crew_py(
    project_name, agents, tasks, crew_config, tools_by_agent
)

# Extract input variables from task descriptions
import re
input_vars = set()
for task in tasks:
    desc = task.get("description", "")
    goal = task.get("goal", "")
    vars_in_desc = re.findall(r'\{(\w+)\}', desc + goal)
    input_vars.update(vars_in_desc)

main_py = generate_main_py(
    project_name, list(input_vars)
)
print("✓ Python files generated")
print(f"  Input variables detected: {list(input_vars)}")

# Validate Python syntax
import ast
try:
    ast.parse(crew_py)
    print("✓ crew.py is valid Python")
except SyntaxError as e:
    print(f"❌ crew.py syntax error: {e}")

try:
    ast.parse(main_py)
    print("✓ main.py is valid Python")
except SyntaxError as e:
    print(f"❌ main.py syntax error: {e}")

print("\n=== PHASE 3: GENERATE CORE FILES MODE ===\n")

# Generate core files mode
generation_mode = "core_files"
project_files = generate_project_structure(
    project_name=project_name,
    description=project_description,
    python_version="3.11",
    agents=agents,
    tasks=tasks,
    crew_config=crew_config,
    tools_by_agent=tools_by_agent,
    env_vars=env_vars,
    generation_mode=generation_mode,
)

print(f"✓ Core files mode generated {len(project_files)} files:")
for filepath in sorted(project_files.keys()):
    size = len(project_files[filepath])
    print(f"  - {filepath} ({size} bytes)")

# Create ZIP for core files
zip_data = create_zip_file(project_files, f"{project_name}_core")
print(f"\n✓ Core ZIP created ({len(zip_data)} bytes)")

# Save ZIP
core_zip_path = f"/tmp/{project_name}_core.zip"
with open(core_zip_path, "wb") as f:
    f.write(zip_data)
print(f"✓ Saved to {core_zip_path}")

print("\n=== PHASE 4: GENERATE COMPLETE PROJECT MODE ===\n")

# Generate complete project mode
generation_mode = "complete_project"
project_files_complete = generate_project_structure(
    project_name=project_name,
    description=project_description,
    python_version="3.11",
    agents=agents,
    tasks=tasks,
    crew_config=crew_config,
    tools_by_agent=tools_by_agent,
    env_vars=env_vars,
    generation_mode=generation_mode,
)

print(f"✓ Complete project mode generated {len(project_files_complete)} files:")
for filepath in sorted(project_files_complete.keys()):
    size = len(project_files_complete[filepath])
    print(f"  - {filepath} ({size} bytes)")

# Create ZIP for complete project
zip_data_complete = create_zip_file(project_files_complete, project_name)
print(f"\n✓ Complete ZIP created ({len(zip_data_complete)} bytes)")

# Save ZIP
complete_zip_path = f"/tmp/{project_name}_complete.zip"
with open(complete_zip_path, "wb") as f:
    f.write(zip_data_complete)
print(f"✓ Saved to {complete_zip_path}")

print("\n=== SUMMARY ===")
print(f"✓ Core files mode: {len(project_files)} files, {len(zip_data)} bytes")
print(f"✓ Complete project mode: {len(project_files_complete)} files, {len(zip_data_complete)} bytes")
print(f"\nGenerated ZIPs:")
print(f"  - {core_zip_path}")
print(f"  - {complete_zip_path}")
