# Gunny - CrewAI Companion

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)
![Docker](https://img.shields.io/badge/docker-supported-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

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

## Running with Docker

Gunny is available as a Docker image for easy deployment without installing dependencies.

### Quick Start with Docker

**Using Docker Hub:**
```bash
docker run -p 8501:8501 bitbrujo/gunny:latest
```

**Using GitHub Container Registry:**
```bash
docker run -p 8501:8501 ghcr.io/bitbrujo/gunny:latest
```

Then open your browser to `http://localhost:8501`

### Using docker-compose

1. **Download or create `docker-compose.yml`:**
   ```yaml
   services:
     gunny:
       image: bitbrujo/gunny:latest
       container_name: gunny
       ports:
         - "8501:8501"
       restart: unless-stopped
   ```

2. **Start the application:**
   ```bash
   docker-compose up -d
   ```

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Stop the application:**
   ```bash
   docker-compose down
   ```

### Building Locally

If you want to build the Docker image yourself:

```bash
# Clone the repository
cd gunny

# Build the image
docker build -t gunny .

# Run the container
docker run -p 8501:8501 gunny
```

## License

MIT License - See LICENSE file for details

## CrewAI Version Compatibility

Gunny has been tested with CrewAI versions 0.1.0 through 1.4.1. The sidebar displays compatibility status:

- ✅ **Green**: Tested and compatible version
- ⚠️ **Yellow**: Untested version (may have new features or breaking changes)

Currently tested versions: 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.10.0, 0.20.0, 0.30.0, 0.40.0, 0.50.0, 0.60.0, 0.70.0, 0.80.0, 0.86.0, 1.4.1

For maintenance and sync procedures, see [MAINTAINABILITY.md](MAINTAINABILITY.md).

## Support

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI Community Forum](https://community.crewai.com/)
- Report issues via your repository's issue tracker

---
