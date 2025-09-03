# Netflix Customer Support AI Agent

An AI-powered customer support system that leverages RAG (Retrieval-Augmented Generation), CrewAI, and multiple LLM agents to provide intelligent, context-aware customer support for a Netflix-like streaming service.


## Stack Overview

- **Scrapy**: collecting docs from the internet
- **ChromaDB**: for vector storage and efficient document retrieval
- **CrewAI**: for orchestrating AI agents
- **Gemini-2.5-flash**: brain & response generator for the agents
- **Fast API**: as a backend to access and chat with crew from an endpoint.
- **Streamlit**: the interactive web interface for real-time chat

## Architecture Components
- **Web Spider**: Developed `CrawlSpider` to collect web pages and extract releated docs. 
- **RAG System**: Implemented for enhanced response accuracy and context awareness
- **Vector Database**: ChromaDB used for efficient similarity search and document retrieval
- **Memory System**: Custom implementation for maintaining conversation context and customer data

## Key Features

- **Intelligent Multi-Agent System**:
  - Customer Support Agent powered by gemini-2.5-flash model
  - Quality Assurance Agent for response verification
  - Sequential processing for enhanced response quality

- **RAG Knowledge Base**:
  - ChromaDB-powered document retrieval for context-aware responses
  - Persistent chat history for each user.

- **Customer Management**
  - Subscription plan tracking and automated plan updates

- **Quality Assurance**
  - Automated response verification and context retention checking

## Technology Stack
- **Frontend**: Streamlit
- **Backend**: Fast API, Lightning AI
- **Database**: ChromaDB (Vector Database)
- **AI Models**: Google Gemini-2.5-flash

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rag-agent-chatbot.git
   cd rag-agent-chatbot/src
   ```

2. **Set up environment**
   ```bash
   conda create -n rag-agent-chatbot python=3.10
   conda activate rag-agent-chatbot
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the Netflex Spider**
    ```bash
    scrapy runspider src/docs/netflex.py
    ```

5. **Initialize the knowledge base**

    Run the `src\docs\data_processing.ipynb` file to initialize the knowledge base.

6. **Run the application**
   First command to run the backend api localy, Second one for streamlit UI.
   ```bash
   python api/main.py
   streamlit run app.py
   ```

## Usage

1. **Customer Registration**
   - Enter customer details in the sidebar
   - Choose subscription plan
   - Save customer information

2. **Start Chatting**
   - Type your question in the chat input
   - Receive real-time AI-powered responses
   - View chat history and context

3. **Subscription Management**
   - Update subscription plans
   - View current subscription status

## Project folders

```
└── 📁src
    └── 📁api
        └── 📁crew
            ├── __init__.py
            ├── .gitignore
            ├── agentops.log
            ├── Agents.py
            ├── chatbot.py
            ├── Tasks.py
            ├── utils.py
        └── 📁helpers
            ├── config.py
        └── 📁routes
            ├── __init__.py
            ├── base_router.py
            ├── chat_router.py
        ├── main.py
    └── 📁docs
        └── 📁chroma_db
            ├── chroma.sqlite3
        ├── 📁netflex_data
        ├── .gitignore
        ├── chroma_upload.py
        ├── data_processing.ipynb
        ├── netflex.py
    └── 📁memory_db
        ├── chroma.sqlite3
    ├── __init__.py
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── agentops.log
    ├── app.py
    ├── requirements.txt
    └── start.ipynb
```

## Future Updates:
- Monitor the system using AgentOps.
- Adding more tools to expand automation for other customer services.
