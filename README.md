# Gunny - CrewAI Companion

A comprehensive Streamlit application for creating complete CrewAI projects with all available configuration options.

<img width="4200" height="2512" alt="Gunny" src="https://github.com/user-attachments/assets/c91ad078-c547-42b8-b251-71ccc79c7436" />

## Features

- **Complete Configuration Coverage**: Access to ALL 50+ agent parameters, 30+ task parameters, and 40+ crew parameters
- **94 Built-in Tools**: Select from the complete CrewAI tools catalog with visible descriptions
- **Dynamic Tool Stub Generation**: Auto-generates configuration files for selected tools with usage examples, authentication requirements, and integration instructions
- **Version Detection**: Automatic CrewAI version detection with compatibility warnings
- **Custom Model Support**: Enter custom model names for any LLM provider
- **Two Generation Modes**: Core Files Only or Complete Project - both now include dynamic tool stubs and knowledge/ directory
- **Real-time Preview**: See generated YAML and Python code as you configure
- **Validation**: Built-in validation to ensure your configuration is correct
- **One-Click Download**: Generate and download complete project as ZIP file
- **Knowledge Base Support**: Configure knowledge sources for your agents
- **Advanced Features**: Memory, planning, code execution, and more

## Installation

### Prerequisites

- Python 3.10 or higher
- [UV](https://docs.astral.sh/uv/) (recommended) or pip package manager

### Setup

1. **Clone or download the repository:**
   ```bash
   cd gunny
   ```

2. **Install UV (if not already installed):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Run the application:**
   ```bash
   uv run streamlit run app.py
   ```

   UV will automatically create a virtual environment and install all dependencies on first run.

4. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

### Alternative: Using pip

If you prefer using pip:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Usage

### 1. Project Information
- Set your project name and description
- Choose Python version
- **Select generation mode**: Core Files Only (default) or Complete Project
- Preview the project structure

### 2. Configure Agents
- Add multiple agents with unique roles
- Configure 50+ parameters per agent:
  - Basic: role, goal, backstory
  - Execution: verbose, cache, max iterations
  - AI Features: reasoning, multimodal, code execution
  - LLM: Select from OpenAI, Anthropic, Google, Ollama, etc., or enter custom model names
  - Tools: Assign tools to each agent

### 3. Define Tasks
- Create tasks and assign them to agents
- Configure 30+ parameters per task:
  - Basic: description, expected output
  - Dependencies: context from other tasks
  - Execution: async, human input
  - Output: file paths, markdown formatting

### 4. Crew Configuration
- Choose process type (Sequential or Hierarchical)
- Enable memory and planning
- Configure manager LLM for hierarchical crews
- Set rate limits and caching

### 5. Select Tools
- Browse 94 available tools by category with visible descriptions:
  - File/Document Tools
  - Search & Scraping Tools
  - Web Browser/Automation Tools
  - Database & Vector Search Tools
  - Integration Tools
  - AI & ML Tools
  - Other Tools
- Tool descriptions are displayed directly (no hover required)
- Search by tool name or description
- Organized in expandable category cards

#### Tool Stub Generation
When you select tools, Gunny automatically generates:
- Individual stub files for each selected tool with usage examples
- Authentication requirements and environment variable setup
- Integration instructions for your agents
- Generic custom tool template for building your own tools

All stubs are included in both Core Files and Complete Project modes in the `tools/` directory.

### 6. Knowledge Base
- Add knowledge sources (PDF, Text, CSV, JSON, Excel)
- Configure embedder providers (17 options)
- Set up custom knowledge configuration

### 7. Advanced Settings
- Configure environment variables and API keys
- Enable enterprise app integrations
- Add custom configurations

### 8. Preview & Generate
- Review generated code (agents.yaml, tasks.yaml, crew.py, main.py)
- Preview dynamic tool stubs for selected tools
- Validate configuration
- Download complete project as ZIP with tools/ and knowledge/ directories

## License

MIT License - See LICENSE file for details

## CrewAI Version Compatibility

Gunny has been tested with CrewAI versions 0.1.0 through 1.4.1. The sidebar displays compatibility status:

- ✅ **Green**: Tested and compatible version
- ⚠️ **Yellow**: Untested version (may have new features or breaking changes)

Currently tested versions: 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.10.0, 0.20.0, 0.30.0, 0.40.0, 0.50.0, 0.60.0, 0.70.0, 0.80.0, 0.86.0, 1.4.1

For maintenance and sync procedures, see [MAINTAINABILITY.md](MAINTAINABILITY.md).

## Documentation

- **[MAINTAINABILITY.md](MAINTAINABILITY.md)**: How to keep Gunny in sync with CrewAI updates
- **[TEST_REPORT_1.4.1.md](TEST_REPORT_1.4.1.md)**: Detailed testing results for CrewAI 1.4.1

## Support

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI Community Forum](https://community.crewai.com/)
- Report issues via your repository's issue tracker

---
