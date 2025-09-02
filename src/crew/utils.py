from crewai.tools import tool
import chromadb
from dotenv import load_dotenv
load_dotenv()

# Docs Client
client = chromadb.PersistentClient('../../src/docs/chroma_db')
collection = client.get_or_create_collection('netflex_faqs')

# Memory Client
memory_client = chromadb.Client()
memory_collection = memory_client.get_or_create_collection("chat_memory")

@tool
def retrive_docs_tool(question: str):
    """A function that takes the customer question and returns it's most relevant
    documents from local chroma DB

    Args:
        question (str): Customer question

    Returns:
        list: List[str] of the 3 most related documents to the customer question

    Usage Example: retrive_docs_tool(question="how to disable notification in my Iphone?")
    """
    return collection.query(
        query_texts=question,
        n_results=3,
    )['documents']

def reset_memory():
    memory_collection.delete(where={'role': 'customer'})
    memory_collection.delete(where={'role': 'agent'})

def remember_message(role: str, content: str):
    """Store a message in memory"""
    memory_collection.add(
        ids=[f"{role}_{hash(content)}"],
        documents=[content],
        metadatas=[{"role": role}]
    )

def recall_messages(last_n: int = 5):
    """Retrieve last_n past messages"""
    chat_history = []
    
    results = memory_collection.get(include=["documents", "metadatas"])
    docs = results["documents"]
    roles = results["metadatas"]
    
    # format chat history
    for i in range(len(docs)):
        chat_history.append({
            "role": roles[i]['role'],
            "content": docs[i]
        })

    # return the last n chat messages
    return chat_history[::-1][:last_n] if len(chat_history) >= last_n else chat_history