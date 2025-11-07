"""Constants and configuration options for CrewAI."""

from typing import Dict, List

# All 87 Available Tools
TOOLS_CATALOG: Dict[str, List[Dict[str, str]]] = {
    "File/Document Tools": [
        {"name": "CSVSearchTool", "description": "Search within CSV files for specific data"},
        {"name": "DOCXSearchTool", "description": "Search content within DOCX documents"},
        {"name": "FileCompressorTool", "description": "Compress files and directories"},
        {"name": "FileReadTool", "description": "Read content from files"},
        {"name": "FileWriterTool", "description": "Write content to files"},
        {"name": "JSONSearchTool", "description": "Search and query JSON files"},
        {"name": "MDXSearchTool", "description": "Search within MDX files"},
        {"name": "PDFSearchTool", "description": "Search content within PDF documents"},
        {"name": "TXTSearchTool", "description": "Search within text files"},
        {"name": "XMLSearchTool", "description": "Search and parse XML files"},
    ],
    "Search & Scraping Tools": [
        {"name": "BraveSearchTool", "description": "Search the web using Brave Search API"},
        {"name": "BrightDataSearchTool", "description": "Search using BrightData API"},
        {"name": "CodeDocsSearchTool", "description": "Search technical documentation and code docs"},
        {"name": "DirectorySearchTool", "description": "Search files within directories"},
        {"name": "EXASearchTool", "description": "Search using EXA API"},
        {"name": "FirecrawlScrapeWebsiteTool", "description": "Scrape websites using Firecrawl"},
        {"name": "FirecrawlSearchTool", "description": "Search using Firecrawl API"},
        {"name": "GithubSearchTool", "description": "Search GitHub repositories and code"},
        {"name": "JinaScrapeWebsiteTool", "description": "Scrape websites using Jina API"},
        {"name": "LinkupSearchTool", "description": "Search using Linkup API"},
        {"name": "MongoDBVectorSearchTool", "description": "Vector search in MongoDB"},
        {"name": "MySQLSearchTool", "description": "Search MySQL databases"},
        {"name": "OxylabsAmazonProductScraperTool", "description": "Scrape Amazon product data"},
        {"name": "OxylabsAmazonSearchScraperTool", "description": "Scrape Amazon search results"},
        {"name": "OxylabsGoogleSearchScraperTool", "description": "Scrape Google search results"},
        {"name": "OxylabsUniversalScraperTool", "description": "Universal web scraping tool"},
        {"name": "ParallelSearchTool", "description": "Execute parallel searches across multiple sources"},
        {"name": "QdrantVectorSearchTool", "description": "Vector search using Qdrant"},
        {"name": "ScrapeElementFromWebsiteTool", "description": "Scrape specific elements from websites"},
        {"name": "ScrapeWebsiteTool", "description": "General website scraping tool"},
        {"name": "ScrapegraphScrapeTool", "description": "Scrape using Scrapegraph"},
        {"name": "ScrapflyScrapeWebsiteTool", "description": "Scrape websites using Scrapfly"},
        {"name": "SerpApiGoogleSearchTool", "description": "Google search via SerpAPI"},
        {"name": "SerperScrapeWebsiteTool", "description": "Scrape websites using Serper"},
        {"name": "SerplyJobSearchTool", "description": "Search job listings"},
        {"name": "SerplyNewsSearchTool", "description": "Search news articles"},
        {"name": "SerplyScholarSearchTool", "description": "Search academic papers"},
        {"name": "SerplyWebSearchTool", "description": "Web search using Serply"},
        {"name": "SingleStoreSearchTool", "description": "Search SingleStore database"},
        {"name": "SnowflakeSearchTool", "description": "Search Snowflake data warehouse"},
        {"name": "TavilySearchTool", "description": "Search using Tavily AI"},
        {"name": "WeaviateVectorSearchTool", "description": "Vector search using Weaviate"},
        {"name": "WebsiteSearchTool", "description": "Search website content"},
        {"name": "YoutubeChannelSearchTool", "description": "Search YouTube channels"},
        {"name": "YoutubeVideoSearchTool", "description": "Search YouTube videos"},
    ],
    "Web Browser/Automation Tools": [
        {"name": "BrightDataDatasetTool", "description": "Access BrightData datasets"},
        {"name": "BrightDataWebUnlockerTool", "description": "Unlock web content with BrightData"},
        {"name": "BrowserbaseLoadTool", "description": "Load pages using Browserbase"},
        {"name": "FirecrawlCrawlWebsiteTool", "description": "Crawl entire websites"},
        {"name": "HyperbrowserLoadTool", "description": "Load pages using Hyperbrowser"},
        {"name": "MultiOnTool", "description": "Multi-browser automation"},
        {"name": "SeleniumScrapingTool", "description": "Web scraping with Selenium"},
        {"name": "SpiderTool", "description": "Web crawling and scraping"},
        {"name": "StagehandTool", "description": "Browser automation orchestration"},
    ],
    "Database & Vector Search Tools": [
        {"name": "CouchbaseFTSVectorSearchTool", "description": "Full-text and vector search in Couchbase"},
        {"name": "MongoDBVectorSearchTool", "description": "Vector search in MongoDB"},
        {"name": "MySQLSearchTool", "description": "Search MySQL databases"},
        {"name": "NL2SQLTool", "description": "Natural language to SQL queries"},
        {"name": "QdrantVectorSearchTool", "description": "Vector search using Qdrant"},
        {"name": "SingleStoreSearchTool", "description": "Search SingleStore database"},
        {"name": "SnowflakeSearchTool", "description": "Search Snowflake data warehouse"},
        {"name": "WeaviateVectorSearchTool", "description": "Vector search using Weaviate"},
    ],
    "Integration Tools": [
        {"name": "ApifyActorsTool", "description": "Run Apify actors for automation"},
        {"name": "BedrockInvokeAgentTool", "description": "Invoke AWS Bedrock agents"},
        {"name": "BedrockKBRetrieverTool", "description": "Retrieve from Bedrock knowledge base"},
        {"name": "ComposioTool", "description": "Integration with Composio platform"},
        {"name": "DatabricksQueryTool", "description": "Query Databricks data"},
        {"name": "EnterpriseActionTool", "description": "Execute enterprise actions"},
        {"name": "GithubSearchTool", "description": "Search GitHub repositories and code"},
        {"name": "ZapierActionTool", "description": "Trigger Zapier workflows"},
    ],
    "AI & ML Tools": [
        {"name": "AIMindTool", "description": "AI-powered decision making"},
        {"name": "ContextualAICreateAgentTool", "description": "Create contextual AI agents"},
        {"name": "ContextualAIParseTool", "description": "Parse content with contextual AI"},
        {"name": "ContextualAIQueryTool", "description": "Query using contextual AI"},
        {"name": "ContextualAIRerankTool", "description": "Rerank results with contextual AI"},
        {"name": "DallETool", "description": "Generate images using DALL-E"},
        {"name": "InvokeCrewAIAutomationTool", "description": "Invoke CrewAI automations"},
        {"name": "LlamaIndexTool", "description": "Query LlamaIndex knowledge base"},
        {"name": "OCRTool", "description": "Optical character recognition"},
        {"name": "PatronusEvalTool", "description": "Evaluate outputs with Patronus"},
        {"name": "PatronusLocalEvaluatorTool", "description": "Local evaluation with Patronus"},
        {"name": "PatronusPredefinedCriteriaEvalTool", "description": "Evaluate against criteria"},
        {"name": "VisionTool", "description": "Computer vision and image analysis"},
    ],
    "Other Tools": [
        {"name": "ArxivPaperTool", "description": "Search and retrieve arXiv papers"},
        {"name": "CodeInterpreterTool", "description": "Execute code in sandboxed environment"},
        {"name": "DirectoryReadTool", "description": "Read directory contents"},
        {"name": "GenerateCrewaiAutomationTool", "description": "Generate CrewAI automation code"},
        {"name": "RagTool", "description": "Retrieval-augmented generation"},
        {"name": "S3ReaderTool", "description": "Read from AWS S3 buckets"},
        {"name": "S3WriterTool", "description": "Write to AWS S3 buckets"},
        {"name": "SerpApiGoogleShoppingTool", "description": "Search Google Shopping via SerpAPI"},
        {"name": "SerperDevTool", "description": "Web search using Serper"},
        {"name": "SerplyWebpageToMarkdownTool", "description": "Convert webpages to markdown"},
        {"name": "TavilyExtractorTool", "description": "Extract content using Tavily"},
    ],
}

# Embedder Providers
EMBEDDER_PROVIDERS = [
    "aws",  # Bedrock
    "cohere",
    "custom",
    "google",  # Generative AI, Vertex AI
    "huggingface",
    "ibm",  # WatsonX
    "instructor",
    "jina",
    "microsoft",  # Azure
    "ollama",
    "onnx",
    "openai",
    "openclip",
    "roboflow",
    "sentence_transformer",
    "text2vec",
    "voyageai",
]

# LLM Providers
LLM_PROVIDERS = {
    "OpenAI": ["gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"],
    "Anthropic": ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"],
    "Google": ["gemini-pro", "gemini-1.5-pro", "gemini-1.5-flash"],
    "Ollama (Local)": ["llama2", "mistral", "mixtral", "codellama"],
    "Azure OpenAI": ["azure/gpt-4", "azure/gpt-35-turbo"],
    "Other": ["Enter custom model name"],
}

# Process Types
PROCESS_TYPES = {
    "sequential": "Tasks executed one after another in order",
    "hierarchical": "Tasks managed by a manager agent (requires manager_llm)",
}

# Knowledge Source Types
KNOWLEDGE_SOURCE_TYPES = [
    "String",
    "PDF",
    "TextFile",
    "CSV",
    "JSON",
    "Excel",
    "Docling",
]

# Code Execution Modes
CODE_EXECUTION_MODES = {
    "safe": "Execute code in Docker container (recommended)",
    "unsafe": "Execute code directly on host system (use with caution)",
}

# Enterprise App Integrations
ENTERPRISE_APPS = [
    "gmail",
    "slack",
    "github",
    "salesforce",
    "hubspot",
    "outlook",
    "teams",
    "onedrive",
    "drive",
    "calendar",
    "sheets",
    "docs",
    "notion",
    "jira",
    "trello",
    "asana",
]

# Default Agent Values
DEFAULT_AGENT_CONFIG = {
    "verbose": False,
    "cache": True,
    "max_iter": 25,
    "max_rpm": None,
    "max_tokens": None,
    "max_execution_time": None,
    "max_retry_limit": 2,
    "respect_context_window": True,
    "allow_delegation": False,
    "reasoning": False,
    "max_reasoning_attempts": None,
    "multimodal": False,
    "allow_code_execution": False,
    "code_execution_mode": "safe",
    "inject_date": False,
    "date_format": "%Y-%m-%d",
    "use_system_prompt": True,
    "guardrail_max_retries": 3,
}

# Default Task Values
DEFAULT_TASK_CONFIG = {
    "async_execution": False,
    "human_input": False,
    "markdown": False,
    "create_directory": True,
    "guardrail_max_retries": 3,
    "allow_crewai_trigger_context": False,
}

# Default Crew Values
DEFAULT_CREW_CONFIG = {
    "name": "crew",
    "process": "sequential",
    "verbose": False,
    "cache": True,
    "memory": False,
    "planning": False,
    "max_rpm": None,
    "tracing": False,
    "share_crew": False,
}

# Environment Variables Template
ENV_VARIABLES = {
    "OpenAI": ["OPENAI_API_KEY"],
    "Anthropic": ["ANTHROPIC_API_KEY"],
    "Google": ["GOOGLE_API_KEY"],
    "Azure": ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT"],
    "Serper": ["SERPER_API_KEY"],
    "Tavily": ["TAVILY_API_KEY"],
    "BraveSearch": ["BRAVE_API_KEY"],
    "SerpAPI": ["SERPAPI_API_KEY"],
}

# Required Environment Variables by Tool
TOOL_ENV_REQUIREMENTS = {
    "SerperDevTool": ["SERPER_API_KEY"],
    "TavilySearchTool": ["TAVILY_API_KEY"],
    "BraveSearchTool": ["BRAVE_API_KEY"],
    "SerpApiGoogleSearchTool": ["SERPAPI_API_KEY"],
    "GithubSearchTool": ["GITHUB_TOKEN"],
}
