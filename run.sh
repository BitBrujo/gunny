#!/bin/bash

# Gunny - Quick Start Script

echo "🎯 Starting Gunny - CrewAI Project Generator"
echo ""

# Check if UV is installed (preferred method)
if command -v uv &> /dev/null; then
    echo "✨ Using UV (faster dependency management)"
    echo "🚀 Launching Gunny..."
    echo ""
    uv run streamlit run app.py
    exit 0
fi

# Fallback to traditional Python/pip method
echo "💡 Tip: Install UV for faster dependency management: curl -LsSf https://astral.sh/uv/install.sh | sh"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or higher is required. You have Python $PYTHON_VERSION"
    exit 1
fi

# Check if requirements are installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Run the app
echo "🚀 Launching Gunny..."
echo ""
streamlit run app.py
