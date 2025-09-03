# Netflix Customer Support AI Agent

An AI-powered customer support system that leverages RAG (Retrieval-Augmented Generation), CrewAI, and multiple LLM agents to provide intelligent, context-aware customer support for a Netflix-like streaming service.


## Stack Overview

- **Scrapy**: collecting docs from the internet
- **ChromaDB**: for vector storage and efficient document retrieval
- **CrewAI**: for orchestrating AI agents
- **Gemini-2.5-flash**: brain & response generator for the agents
- **Streamlit**: the interactive web interface and real-time chat

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
- **Backend**: Python, CrewAI
- **Database**: ChromaDB (Vector Database)
- **AI Models**: Google Gemini-2.5-flash

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rag-agent-chatbot.git
   cd rag-agent-chatbot
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
   ```bash
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
rag-agent-chatbot/
├── app.py                 # Main Streamlit application
├── src/
│   ├── crew/             # Agent and task definitions
│   │   ├── Agents.py     # AI agent configurations
│   │   ├── Tasks.py      # Task definitions
│   │   ├── chatbot.py    # Core chatbot logic
│   │   └── utils.py      # Utility functions
│   ├── docs/             # Docs data
│   │   ├── chroma_db/    # Vector database for docs
│   │   └── netflex_data/ # Knowledge base 
│   └── memory_db/        # Chat history storage
|
├── requirements.txt      # Project dependencies
└── .env                  # Env variables 
```

## Future Updates:
- Monitor the system using AgentOps.
- Adding more tools to scale up the automation for customer services.
