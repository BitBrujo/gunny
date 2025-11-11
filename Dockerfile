# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Create non-root user
RUN useradd -m -u 1000 -s /bin/bash gunny

# Set working directory
WORKDIR /app

# Copy requirements first for better layer caching
COPY --chown=gunny:gunny requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=gunny:gunny app.py .
COPY --chown=gunny:gunny generators/ ./generators/
COPY --chown=gunny:gunny ui/ ./ui/
COPY --chown=gunny:gunny utils/ ./utils/

# Copy documentation (explicitly include/exclude)
COPY --chown=gunny:gunny README.md .
COPY --chown=gunny:gunny MAINTAINABILITY.md .
COPY --chown=gunny:gunny TEST_REPORT_1.4.1.md .
# CLAUDE.md is excluded via .dockerignore

# Switch to non-root user
USER gunny

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
