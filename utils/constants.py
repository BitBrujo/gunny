"""Constants and configuration options for CrewAI."""

from typing import Dict, List

# All 94 Available Tools
TOOLS_CATALOG: Dict[str, List[Dict[str, any]]] = {
    "File/Document Tools": [
        {
            "name": "CSVSearchTool",
            "description": "Search within CSV files for specific data. Supports querying structured data with filtering and column selection. Works with local CSV files without external dependencies.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "DOCXSearchTool",
            "description": "Search content within DOCX documents. Extracts and searches text from Microsoft Word files. Handles formatting and embedded content for comprehensive document analysis.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "FileCompressorTool",
            "description": "Compress files and directories into archives. Supports ZIP, TAR, and GZ formats. Useful for packaging outputs and reducing storage requirements.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "FileReadTool",
            "description": "Read content from files in various formats. Supports text, binary, and encoded files. Essential for accessing local file system data.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "FileWriterTool",
            "description": "Write content to files with support for multiple formats. Creates or overwrites files with structured or unstructured data. Handles encoding and permissions automatically.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "JSONSearchTool",
            "description": "Search and query JSON files using path expressions. Supports nested object navigation and array filtering. Ideal for configuration files and API response processing.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "MDXSearchTool",
            "description": "Search within MDX (Markdown + JSX) files. Parses both markdown content and embedded components. Useful for documentation sites and React-based content.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "PDFSearchTool",
            "description": "Search content within PDF documents with text extraction. Handles multi-page documents and preserves document structure. Works with both text-based and OCR-processed PDFs.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "TXTSearchTool",
            "description": "Search within plain text files using pattern matching. Supports regex and simple string searches. Fast and efficient for large text file analysis.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "XMLSearchTool",
            "description": "Search and parse XML files with XPath support. Navigates complex XML structures and validates against schemas. Essential for processing structured data and configurations.",
            "requires_auth": False,
            "env_vars": [],
        },
    ],
    "Search & Scraping Tools": [
        {
            "name": "BraveSearchTool",
            "description": "Search the web using Brave Search API. Privacy-focused search engine with independent index. Provides web, news, and image search results with customizable parameters.",
            "requires_auth": True,
            "env_vars": ["BRAVE_API_KEY"],
            "auth_note": "Sign up at brave.com/search/api for API credentials"
        },
        {
            "name": "BrightDataSearchTool",
            "description": "Search using BrightData's data collection network. Enterprise-grade web data platform with proxy rotation. Access to structured datasets and real-time web data.",
            "requires_auth": True,
            "env_vars": ["BRIGHTDATA_API_KEY", "BRIGHTDATA_USERNAME"],
            "auth_note": "BrightData account with API access required"
        },
        {
            "name": "CodeDocsSearchTool",
            "description": "Search technical documentation and code docs. Indexes programming language docs, API references, and developer resources. Optimized for code-related queries.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "DirectorySearchTool",
            "description": "Search files within local directories. Recursive file system search with pattern matching. Supports filtering by name, type, and content.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "EXASearchTool",
            "description": "Search using EXA AI-powered search API. Neural search engine optimized for developer queries. Returns semantically relevant results with rich metadata.",
            "requires_auth": True,
            "env_vars": ["EXA_API_KEY"],
            "auth_note": "Get API key from exa.ai dashboard"
        },
        {
            "name": "FirecrawlScrapeWebsiteTool",
            "description": "Scrape websites using Firecrawl service. Handles JavaScript rendering and dynamic content. Bypasses common anti-bot protections with residential proxies.",
            "requires_auth": True,
            "env_vars": ["FIRECRAWL_API_KEY"],
            "auth_note": "Firecrawl account required for API access"
        },
        {
            "name": "FirecrawlSearchTool",
            "description": "Search indexed web content via Firecrawl API. Pre-crawled and structured web data for fast retrieval. Includes content extraction and formatting.",
            "requires_auth": True,
            "env_vars": ["FIRECRAWL_API_KEY"],
            "auth_note": "Same credentials as FirecrawlScrapeWebsiteTool"
        },
        {
            "name": "GithubSearchTool",
            "description": "Search GitHub repositories, code, issues, and users. Access to GitHub's comprehensive search API with filters. Supports advanced query syntax and result sorting.",
            "requires_auth": True,
            "env_vars": ["GITHUB_TOKEN"],
            "auth_note": "Generate personal access token in GitHub settings"
        },
        {
            "name": "JinaScrapeWebsiteTool",
            "description": "Scrape websites using Jina AI's reader API. Converts web pages to clean markdown format. Optimized for LLM consumption with noise removal.",
            "requires_auth": True,
            "env_vars": ["JINA_API_KEY"],
            "auth_note": "Free tier available at jina.ai"
        },
        {
            "name": "LinkupSearchTool",
            "description": "Search using Linkup API for real-time web search. Aggregates results from multiple search engines. Provides unified interface with deduplication.",
            "requires_auth": True,
            "env_vars": ["LINKUP_API_KEY"],
            "auth_note": "Linkup account required"
        },
        {
            "name": "MongoDBVectorSearchTool",
            "description": "Vector similarity search in MongoDB Atlas. Leverages MongoDB's vector search capabilities for semantic queries. Requires Atlas cluster with vector index configured.",
            "requires_auth": True,
            "env_vars": ["MONGODB_URI", "MONGODB_DATABASE"],
            "auth_note": "MongoDB Atlas connection string required"
        },
        {
            "name": "MySQLSearchTool",
            "description": "Query and search MySQL databases with natural language. Converts queries to SQL automatically. Supports complex joins and aggregations.",
            "requires_auth": True,
            "env_vars": ["MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"],
            "auth_note": "MySQL database credentials required"
        },
        {
            "name": "OxylabsAmazonProductScraperTool",
            "description": "Scrape Amazon product data via Oxylabs. Extracts prices, reviews, ratings, and availability. Enterprise-grade reliability with proxy rotation.",
            "requires_auth": True,
            "env_vars": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
            "auth_note": "Oxylabs subscription required"
        },
        {
            "name": "OxylabsAmazonSearchScraperTool",
            "description": "Scrape Amazon search results using Oxylabs. Collects search rankings and sponsored listings. Supports multiple Amazon marketplaces.",
            "requires_auth": True,
            "env_vars": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
            "auth_note": "Same Oxylabs account as product scraper"
        },
        {
            "name": "OxylabsGoogleSearchScraperTool",
            "description": "Scrape Google search results via Oxylabs SERP API. Retrieves organic results, ads, and knowledge panels. Geo-targeting and device type selection available.",
            "requires_auth": True,
            "env_vars": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
            "auth_note": "Oxylabs SERP API access required"
        },
        {
            "name": "OxylabsUniversalScraperTool",
            "description": "Universal web scraping tool from Oxylabs. Handles any website with automatic parser selection. JavaScript rendering and CAPTCHA solving included.",
            "requires_auth": True,
            "env_vars": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
            "auth_note": "Oxylabs universal scraper license needed"
        },
        {
            "name": "ParallelSearchTool",
            "description": "Execute parallel searches across multiple sources simultaneously. Aggregates and deduplicates results from various search tools. Significantly faster than sequential searches.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "QdrantVectorSearchTool",
            "description": "Vector similarity search using Qdrant database. High-performance vector search engine for embeddings. Supports filtering, hybrid search, and clustering.",
            "requires_auth": True,
            "env_vars": ["QDRANT_URL", "QDRANT_API_KEY"],
            "auth_note": "Qdrant Cloud or self-hosted instance required"
        },
        {
            "name": "ScrapeElementFromWebsiteTool",
            "description": "Scrape specific HTML elements from websites using CSS selectors. Target exact content without full page parsing. Efficient for structured data extraction.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "ScrapeWebsiteTool",
            "description": "General-purpose website scraping tool. Extracts full page content with basic anti-bot handling. Suitable for static sites and simple scraping tasks.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "ScrapegraphScrapeTool",
            "description": "AI-powered scraping using Scrapegraph. Uses LLMs to understand page structure and extract data. Adapts to layout changes automatically.",
            "requires_auth": True,
            "env_vars": ["SCRAPEGRAPH_API_KEY"],
            "auth_note": "Scrapegraph account required"
        },
        {
            "name": "ScrapflyScrapeWebsiteTool",
            "description": "Professional web scraping via Scrapfly API. Anti-bot bypass with residential proxies and browser emulation. Includes screenshot capture and JavaScript execution.",
            "requires_auth": True,
            "env_vars": ["SCRAPFLY_API_KEY"],
            "auth_note": "Sign up at scrapfly.io for API key"
        },
        {
            "name": "SerpApiGoogleSearchTool",
            "description": "Google search results via SerpAPI. Structured JSON data from Google SERP. Includes organic results, ads, knowledge graph, and more.",
            "requires_auth": True,
            "env_vars": ["SERPAPI_API_KEY"],
            "auth_note": "Get API key from serpapi.com dashboard"
        },
        {
            "name": "SerperScrapeWebsiteTool",
            "description": "Scrape websites using Serper service. Complementary to SerperDevTool for full page extraction. Handles JavaScript-heavy sites.",
            "requires_auth": True,
            "env_vars": ["SERPER_API_KEY"],
            "auth_note": "Same key as SerperDevTool"
        },
        {
            "name": "SerplyJobSearchTool",
            "description": "Search job listings across multiple platforms. Aggregates Indeed, LinkedIn, Glassdoor, and more. Includes salary ranges and company details.",
            "requires_auth": True,
            "env_vars": ["SERPLY_API_KEY"],
            "auth_note": "Serply account required for job search access"
        },
        {
            "name": "SerplyNewsSearchTool",
            "description": "Search news articles from thousands of sources. Real-time news aggregation with sentiment analysis. Filter by date, source, and topic.",
            "requires_auth": True,
            "env_vars": ["SERPLY_API_KEY"],
            "auth_note": "Same Serply account as job search"
        },
        {
            "name": "SerplyScholarSearchTool",
            "description": "Search academic papers and scholarly articles. Access to Google Scholar and academic databases. Includes citations, abstracts, and full-text links.",
            "requires_auth": True,
            "env_vars": ["SERPLY_API_KEY"],
            "auth_note": "Serply API key provides scholar access"
        },
        {
            "name": "SerplyWebSearchTool",
            "description": "General web search using Serply API. Alternative to Google with similar result quality. Supports location-based and filtered searches.",
            "requires_auth": True,
            "env_vars": ["SERPLY_API_KEY"],
            "auth_note": "Single API key for all Serply tools"
        },
        {
            "name": "SingleStoreSearchTool",
            "description": "Search SingleStore distributed SQL database. High-performance queries on large datasets. Combines transactional and analytical workloads.",
            "requires_auth": True,
            "env_vars": ["SINGLESTORE_HOST", "SINGLESTORE_USER", "SINGLESTORE_PASSWORD", "SINGLESTORE_DATABASE"],
            "auth_note": "SingleStore cluster credentials required"
        },
        {
            "name": "SnowflakeSearchTool",
            "description": "Query Snowflake cloud data warehouse. Enterprise data platform for analytics at scale. Supports complex SQL and semi-structured data.",
            "requires_auth": True,
            "env_vars": ["SNOWFLAKE_ACCOUNT", "SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_WAREHOUSE", "SNOWFLAKE_DATABASE"],
            "auth_note": "Snowflake account and warehouse access required"
        },
        {
            "name": "TavilySearchTool",
            "description": "AI-optimized search using Tavily API. Purpose-built for LLM applications with clean, relevant results. Includes real-time data and source attribution.",
            "requires_auth": True,
            "env_vars": ["TAVILY_API_KEY"],
            "auth_note": "Free tier available at tavily.com"
        },
        {
            "name": "WeaviateVectorSearchTool",
            "description": "Vector search using Weaviate database. Open-source vector database with GraphQL API. Supports hybrid search combining vector and keyword.",
            "requires_auth": True,
            "env_vars": ["WEAVIATE_URL", "WEAVIATE_API_KEY"],
            "auth_note": "Weaviate Cloud or self-hosted instance needed"
        },
        {
            "name": "WebsiteSearchTool",
            "description": "Search specific website content with site-restricted queries. Focuses search on single domain. Useful for documentation and knowledge base searches.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "YoutubeChannelSearchTool",
            "description": "Search YouTube channels and retrieve channel metadata. Access subscriber counts, video lists, and channel descriptions. No API quota limits for basic searches.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "YoutubeVideoSearchTool",
            "description": "Search YouTube videos with filters and sorting. Retrieves video metadata, transcripts, and statistics. Free access without YouTube Data API quota.",
            "requires_auth": False,
            "env_vars": [],
        },
    ],
    "Web Browser/Automation Tools": [
        {
            "name": "BrightDataDatasetTool",
            "description": "Access BrightData's pre-collected datasets. Ready-to-use structured data from major platforms. Includes e-commerce, social media, and business data.",
            "requires_auth": True,
            "env_vars": ["BRIGHTDATA_API_KEY", "BRIGHTDATA_USERNAME"],
            "auth_note": "BrightData dataset subscription required"
        },
        {
            "name": "BrightDataWebUnlockerTool",
            "description": "Unlock and access protected web content via BrightData proxies. Bypasses geo-restrictions and anti-bot systems. Enterprise-grade proxy network with automatic rotation.",
            "requires_auth": True,
            "env_vars": ["BRIGHTDATA_API_KEY", "BRIGHTDATA_USERNAME"],
            "auth_note": "BrightData Web Unlocker plan needed"
        },
        {
            "name": "BrowserbaseLoadTool",
            "description": "Load and render pages using Browserbase cloud browsers. Managed browser infrastructure with screenshot and PDF export. Handles JavaScript-heavy sites without local resources.",
            "requires_auth": True,
            "env_vars": ["BROWSERBASE_API_KEY", "BROWSERBASE_PROJECT_ID"],
            "auth_note": "Sign up at browserbase.com for credentials"
        },
        {
            "name": "FirecrawlCrawlWebsiteTool",
            "description": "Crawl entire websites recursively via Firecrawl. Discovers and extracts all pages within a domain. Respects robots.txt and implements rate limiting.",
            "requires_auth": True,
            "env_vars": ["FIRECRAWL_API_KEY"],
            "auth_note": "Firecrawl crawling plan required"
        },
        {
            "name": "HyperbrowserLoadTool",
            "description": "Load pages using Hyperbrowser cloud automation. Stealth browser with advanced anti-detection. Optimized for bot-protected sites and automation.",
            "requires_auth": True,
            "env_vars": ["HYPERBROWSER_API_KEY"],
            "auth_note": "Hyperbrowser account needed"
        },
        {
            "name": "MultiOnTool",
            "description": "Multi-browser automation for parallel web tasks. Coordinate actions across multiple browser instances. Useful for testing and distributed scraping.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "SeleniumScrapingTool",
            "description": "Web scraping with Selenium WebDriver. Full browser automation with JavaScript execution. Supports Chrome, Firefox, and Edge browsers.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "SpiderTool",
            "description": "Fast web crawling and scraping with Spider. High-performance crawler with concurrent requests. Includes content extraction and URL discovery.",
            "requires_auth": True,
            "env_vars": ["SPIDER_API_KEY"],
            "auth_note": "Spider Cloud API key required"
        },
        {
            "name": "StagehandTool",
            "description": "Browser automation orchestration platform. Manage complex multi-step browser workflows. Includes session persistence and debugging tools.",
            "requires_auth": True,
            "env_vars": ["STAGEHAND_API_KEY"],
            "auth_note": "Stagehand account required"
        },
    ],
    "Database & Vector Search Tools": [
        {
            "name": "CouchbaseFTSVectorSearchTool",
            "description": "Full-text and vector search in Couchbase database. Combines traditional FTS with vector similarity search. Scalable NoSQL solution for hybrid search workloads.",
            "requires_auth": True,
            "env_vars": ["COUCHBASE_CONNECTION_STRING", "COUCHBASE_USERNAME", "COUCHBASE_PASSWORD"],
            "auth_note": "Couchbase cluster with vector search enabled"
        },
        {
            "name": "MongoDBVectorSearchTool",
            "description": "Vector similarity search in MongoDB Atlas. Leverages MongoDB's vector search capabilities for semantic queries. Requires Atlas cluster with vector index configured.",
            "requires_auth": True,
            "env_vars": ["MONGODB_URI", "MONGODB_DATABASE"],
            "auth_note": "MongoDB Atlas connection string required"
        },
        {
            "name": "MySQLSearchTool",
            "description": "Query and search MySQL databases with natural language. Converts queries to SQL automatically. Supports complex joins and aggregations.",
            "requires_auth": True,
            "env_vars": ["MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"],
            "auth_note": "MySQL database credentials required"
        },
        {
            "name": "NL2SQLTool",
            "description": "Convert natural language questions to SQL queries. AI-powered query generation for any SQL database. Supports MySQL, PostgreSQL, SQL Server, and more.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "QdrantVectorSearchTool",
            "description": "Vector similarity search using Qdrant database. High-performance vector search engine for embeddings. Supports filtering, hybrid search, and clustering.",
            "requires_auth": True,
            "env_vars": ["QDRANT_URL", "QDRANT_API_KEY"],
            "auth_note": "Qdrant Cloud or self-hosted instance required"
        },
        {
            "name": "SingleStoreSearchTool",
            "description": "Search SingleStore distributed SQL database. High-performance queries on large datasets. Combines transactional and analytical workloads.",
            "requires_auth": True,
            "env_vars": ["SINGLESTORE_HOST", "SINGLESTORE_USER", "SINGLESTORE_PASSWORD", "SINGLESTORE_DATABASE"],
            "auth_note": "SingleStore cluster credentials required"
        },
        {
            "name": "SnowflakeSearchTool",
            "description": "Query Snowflake cloud data warehouse. Enterprise data platform for analytics at scale. Supports complex SQL and semi-structured data.",
            "requires_auth": True,
            "env_vars": ["SNOWFLAKE_ACCOUNT", "SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_WAREHOUSE", "SNOWFLAKE_DATABASE"],
            "auth_note": "Snowflake account and warehouse access required"
        },
        {
            "name": "WeaviateVectorSearchTool",
            "description": "Vector search using Weaviate database. Open-source vector database with GraphQL API. Supports hybrid search combining vector and keyword.",
            "requires_auth": True,
            "env_vars": ["WEAVIATE_URL", "WEAVIATE_API_KEY"],
            "auth_note": "Weaviate Cloud or self-hosted instance needed"
        },
    ],
    "Integration Tools": [
        {
            "name": "ApifyActorsTool",
            "description": "Run Apify actors for web automation and scraping. Access 1000+ pre-built actors for data extraction. Scalable serverless execution with cloud infrastructure.",
            "requires_auth": True,
            "env_vars": ["APIFY_API_TOKEN"],
            "auth_note": "Sign up at apify.com for API token"
        },
        {
            "name": "BedrockInvokeAgentTool",
            "description": "Invoke AWS Bedrock AI agents for task execution. Orchestrate foundation models with business logic. Enterprise AWS integration with security and compliance.",
            "requires_auth": True,
            "env_vars": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
            "auth_note": "AWS account with Bedrock access required"
        },
        {
            "name": "BedrockKBRetrieverTool",
            "description": "Retrieve from AWS Bedrock knowledge bases. Query enterprise knowledge with semantic search. Integrated with S3, databases, and document stores.",
            "requires_auth": True,
            "env_vars": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
            "auth_note": "AWS Bedrock KB must be configured"
        },
        {
            "name": "ComposioTool",
            "description": "Integration with Composio automation platform. Connect to 100+ SaaS tools via single API. Handles OAuth, rate limits, and data formatting.",
            "requires_auth": True,
            "env_vars": ["COMPOSIO_API_KEY"],
            "auth_note": "Composio account required"
        },
        {
            "name": "DatabricksQueryTool",
            "description": "Query Databricks data lakehouse platform. Execute SQL and Spark queries on massive datasets. Enterprise analytics with Delta Lake integration.",
            "requires_auth": True,
            "env_vars": ["DATABRICKS_HOST", "DATABRICKS_TOKEN", "DATABRICKS_WAREHOUSE_ID"],
            "auth_note": "Databricks workspace access required"
        },
        {
            "name": "EnterpriseActionTool",
            "description": "Execute enterprise workflow actions. Trigger business processes and approvals. Integrates with enterprise systems via APIs.",
            "requires_auth": True,
            "env_vars": ["ENTERPRISE_API_KEY", "ENTERPRISE_ENDPOINT"],
            "auth_note": "Enterprise system credentials required"
        },
        {
            "name": "GithubSearchTool",
            "description": "Search GitHub repositories, code, issues, and users. Access to GitHub's comprehensive search API with filters. Supports advanced query syntax and result sorting.",
            "requires_auth": True,
            "env_vars": ["GITHUB_TOKEN"],
            "auth_note": "Generate personal access token in GitHub settings"
        },
        {
            "name": "ZapierActionTool",
            "description": "Trigger Zapier workflows and zaps from agents. Connect to 5000+ apps without coding. Automate tasks across multiple platforms.",
            "requires_auth": True,
            "env_vars": ["ZAPIER_NLA_API_KEY"],
            "auth_note": "Zapier account with Natural Language Actions enabled"
        },
    ],
    "AI & ML Tools": [
        {
            "name": "AIMindTool",
            "description": "AI-powered decision making and reasoning tool. Analyzes complex scenarios and recommends optimal actions. Combines logic, heuristics, and learned patterns.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "ContextualAICreateAgentTool",
            "description": "Create contextual AI agents dynamically. Build specialized agents for specific tasks on-the-fly. Leverages Contextual AI platform for agent generation.",
            "requires_auth": True,
            "env_vars": ["CONTEXTUAL_AI_API_KEY"],
            "auth_note": "Contextual AI account required"
        },
        {
            "name": "ContextualAIParseTool",
            "description": "Parse and extract structured data using Contextual AI. Handles unstructured text, PDFs, and documents. AI-powered entity recognition and relationship extraction.",
            "requires_auth": True,
            "env_vars": ["CONTEXTUAL_AI_API_KEY"],
            "auth_note": "Same Contextual AI account"
        },
        {
            "name": "ContextualAIQueryTool",
            "description": "Query knowledge bases with Contextual AI. Semantic search across enterprise documents. Natural language interface for data retrieval.",
            "requires_auth": True,
            "env_vars": ["CONTEXTUAL_AI_API_KEY"],
            "auth_note": "Contextual AI platform access needed"
        },
        {
            "name": "ContextualAIRerankTool",
            "description": "Rerank search results using Contextual AI. Improves relevance of retrieved documents. Optimizes results for specific query intent.",
            "requires_auth": True,
            "env_vars": ["CONTEXTUAL_AI_API_KEY"],
            "auth_note": "Reranking API access required"
        },
        {
            "name": "DallETool",
            "description": "Generate images using OpenAI DALL-E model. Create images from text descriptions. Supports DALL-E 2 and DALL-E 3 with various sizes and styles.",
            "requires_auth": True,
            "env_vars": ["OPENAI_API_KEY"],
            "auth_note": "OpenAI API key with DALL-E access"
        },
        {
            "name": "InvokeCrewAIAutomationTool",
            "description": "Invoke CrewAI automations and workflows from within agents. Trigger other crew executions programmatically. Enables nested and chained AI workflows.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "LlamaIndexTool",
            "description": "Query LlamaIndex knowledge bases and indices. RAG (Retrieval Augmented Generation) over custom data. Supports multiple index types and retrieval strategies.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "OCRTool",
            "description": "Optical character recognition for text extraction from images. Converts scanned documents and photos to editable text. Supports multiple languages and document types.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "PatronusEvalTool",
            "description": "Evaluate LLM outputs with Patronus AI platform. Assess quality, accuracy, and safety of generated content. Enterprise-grade LLM evaluation and monitoring.",
            "requires_auth": True,
            "env_vars": ["PATRONUS_API_KEY"],
            "auth_note": "Patronus AI account required"
        },
        {
            "name": "PatronusLocalEvaluatorTool",
            "description": "Local LLM evaluation using Patronus framework. Run evaluations without cloud dependency. Privacy-focused assessment for sensitive applications.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "PatronusPredefinedCriteriaEvalTool",
            "description": "Evaluate LLM outputs against predefined criteria. Check adherence to specific requirements and guidelines. Automated quality assurance for AI-generated content.",
            "requires_auth": True,
            "env_vars": ["PATRONUS_API_KEY"],
            "auth_note": "Patronus evaluation API access"
        },
        {
            "name": "VisionTool",
            "description": "Computer vision and image analysis capabilities. Object detection, classification, and scene understanding. Powered by multimodal LLMs for visual reasoning.",
            "requires_auth": False,
            "env_vars": [],
        },
    ],
    "Other Tools": [
        {
            "name": "ArxivPaperTool",
            "description": "Search and retrieve academic papers from arXiv. Access to physics, math, CS, and other scientific preprints. Free access to full-text PDFs and metadata.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "CodeInterpreterTool",
            "description": "Execute Python code in sandboxed environment. Run data analysis, visualizations, and computations safely. Includes popular libraries like pandas, numpy, matplotlib.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "DirectoryReadTool",
            "description": "Read and list directory contents from file system. Recursive directory traversal with filtering. Useful for file discovery and organization tasks.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "GenerateCrewaiAutomationTool",
            "description": "Generate CrewAI automation code from descriptions. AI-powered code generation for crew workflows. Automates the creation of agents, tasks, and crew configurations.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "RagTool",
            "description": "Retrieval-augmented generation for knowledge-based Q&A. Combines document retrieval with LLM generation. Custom knowledge base integration for domain-specific answers.",
            "requires_auth": False,
            "env_vars": [],
        },
        {
            "name": "S3ReaderTool",
            "description": "Read files and objects from AWS S3 buckets. Access cloud-stored data for processing. Supports streaming large files and folder traversal.",
            "requires_auth": True,
            "env_vars": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
            "auth_note": "AWS credentials with S3 read permissions"
        },
        {
            "name": "S3WriterTool",
            "description": "Write files and objects to AWS S3 buckets. Upload results and outputs to cloud storage. Handles multipart uploads for large files.",
            "requires_auth": True,
            "env_vars": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
            "auth_note": "AWS credentials with S3 write permissions"
        },
        {
            "name": "SerpApiGoogleShoppingTool",
            "description": "Search Google Shopping for product listings via SerpAPI. Compare prices, reviews, and availability. Structured e-commerce data extraction.",
            "requires_auth": True,
            "env_vars": ["SERPAPI_API_KEY"],
            "auth_note": "SerpAPI key with Shopping access"
        },
        {
            "name": "SerperDevTool",
            "description": "Web search using Serper.dev API. Fast Google search results without official API. Includes web, news, images, and videos with JSON responses.",
            "requires_auth": True,
            "env_vars": ["SERPER_API_KEY"],
            "auth_note": "Sign up at serper.dev for API key"
        },
        {
            "name": "SerplyWebpageToMarkdownTool",
            "description": "Convert webpages to clean markdown format via Serply. Removes ads and navigation for content extraction. Optimized for LLM processing and storage.",
            "requires_auth": True,
            "env_vars": ["SERPLY_API_KEY"],
            "auth_note": "Serply API key required"
        },
        {
            "name": "TavilyExtractorTool",
            "description": "Extract and structure content from URLs using Tavily. AI-powered content extraction with noise removal. Returns clean, relevant information for processing.",
            "requires_auth": True,
            "env_vars": ["TAVILY_API_KEY"],
            "auth_note": "Tavily account for extraction API"
        },
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

# CrewAI Version Compatibility
# These versions have been tested with Gunny and are known to work correctly
TESTED_CREWAI_VERSIONS = [
    "0.1.0", "0.2.0", "0.3.0", "0.4.0",
    "0.10.0", "0.20.0", "0.30.0", "0.40.0",
    "0.50.0", "0.60.0", "0.70.0", "0.80.0",
    "0.86.0"
]
LATEST_TESTED_VERSION = "0.86.0"

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
    "LangSmith": ["LANGCHAIN_API_KEY", "LANGCHAIN_PROJECT"],
}

# Required Environment Variables by Tool
# NOTE: This is a legacy dict maintained for backward compatibility.
# The primary source of truth is now the 'env_vars' field in TOOLS_CATALOG above.
TOOL_ENV_REQUIREMENTS = {
    # Search & Scraping Tools
    "BraveSearchTool": ["BRAVE_API_KEY"],
    "BrightDataSearchTool": ["BRIGHTDATA_API_KEY", "BRIGHTDATA_USERNAME"],
    "EXASearchTool": ["EXA_API_KEY"],
    "FirecrawlScrapeWebsiteTool": ["FIRECRAWL_API_KEY"],
    "FirecrawlSearchTool": ["FIRECRAWL_API_KEY"],
    "GithubSearchTool": ["GITHUB_TOKEN"],
    "JinaScrapeWebsiteTool": ["JINA_API_KEY"],
    "LinkupSearchTool": ["LINKUP_API_KEY"],
    "MongoDBVectorSearchTool": ["MONGODB_URI", "MONGODB_DATABASE"],
    "MySQLSearchTool": ["MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"],
    "OxylabsAmazonProductScraperTool": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
    "OxylabsAmazonSearchScraperTool": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
    "OxylabsGoogleSearchScraperTool": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
    "OxylabsUniversalScraperTool": ["OXYLABS_USERNAME", "OXYLABS_PASSWORD"],
    "QdrantVectorSearchTool": ["QDRANT_URL", "QDRANT_API_KEY"],
    "ScrapegraphScrapeTool": ["SCRAPEGRAPH_API_KEY"],
    "ScrapflyScrapeWebsiteTool": ["SCRAPFLY_API_KEY"],
    "SerpApiGoogleSearchTool": ["SERPAPI_API_KEY"],
    "SerperScrapeWebsiteTool": ["SERPER_API_KEY"],
    "SerplyJobSearchTool": ["SERPLY_API_KEY"],
    "SerplyNewsSearchTool": ["SERPLY_API_KEY"],
    "SerplyScholarSearchTool": ["SERPLY_API_KEY"],
    "SerplyWebSearchTool": ["SERPLY_API_KEY"],
    "SingleStoreSearchTool": ["SINGLESTORE_HOST", "SINGLESTORE_USER", "SINGLESTORE_PASSWORD", "SINGLESTORE_DATABASE"],
    "SnowflakeSearchTool": ["SNOWFLAKE_ACCOUNT", "SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_WAREHOUSE", "SNOWFLAKE_DATABASE"],
    "TavilySearchTool": ["TAVILY_API_KEY"],
    "WeaviateVectorSearchTool": ["WEAVIATE_URL", "WEAVIATE_API_KEY"],

    # Web Browser/Automation Tools
    "BrightDataDatasetTool": ["BRIGHTDATA_API_KEY", "BRIGHTDATA_USERNAME"],
    "BrightDataWebUnlockerTool": ["BRIGHTDATA_API_KEY", "BRIGHTDATA_USERNAME"],
    "BrowserbaseLoadTool": ["BROWSERBASE_API_KEY", "BROWSERBASE_PROJECT_ID"],
    "FirecrawlCrawlWebsiteTool": ["FIRECRAWL_API_KEY"],
    "HyperbrowserLoadTool": ["HYPERBROWSER_API_KEY"],
    "SpiderTool": ["SPIDER_API_KEY"],
    "StagehandTool": ["STAGEHAND_API_KEY"],

    # Database & Vector Search Tools
    "CouchbaseFTSVectorSearchTool": ["COUCHBASE_CONNECTION_STRING", "COUCHBASE_USERNAME", "COUCHBASE_PASSWORD"],

    # Integration Tools
    "ApifyActorsTool": ["APIFY_API_TOKEN"],
    "BedrockInvokeAgentTool": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
    "BedrockKBRetrieverTool": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
    "ComposioTool": ["COMPOSIO_API_KEY"],
    "DatabricksQueryTool": ["DATABRICKS_HOST", "DATABRICKS_TOKEN", "DATABRICKS_WAREHOUSE_ID"],
    "EnterpriseActionTool": ["ENTERPRISE_API_KEY", "ENTERPRISE_ENDPOINT"],
    "ZapierActionTool": ["ZAPIER_NLA_API_KEY"],

    # AI & ML Tools
    "ContextualAICreateAgentTool": ["CONTEXTUAL_AI_API_KEY"],
    "ContextualAIParseTool": ["CONTEXTUAL_AI_API_KEY"],
    "ContextualAIQueryTool": ["CONTEXTUAL_AI_API_KEY"],
    "ContextualAIRerankTool": ["CONTEXTUAL_AI_API_KEY"],
    "DallETool": ["OPENAI_API_KEY"],
    "PatronusEvalTool": ["PATRONUS_API_KEY"],
    "PatronusPredefinedCriteriaEvalTool": ["PATRONUS_API_KEY"],

    # Other Tools
    "S3ReaderTool": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
    "S3WriterTool": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
    "SerpApiGoogleShoppingTool": ["SERPAPI_API_KEY"],
    "SerperDevTool": ["SERPER_API_KEY"],
    "SerplyWebpageToMarkdownTool": ["SERPLY_API_KEY"],
    "TavilyExtractorTool": ["TAVILY_API_KEY"],
}
