from crewai.tools import tool
import chromadb
import os
from dotenv import load_dotenv
load_dotenv()

cwd = os.getcwd()

# Docs Client
client = chromadb.PersistentClient(path=os.path.join(cwd, 'src', 'docs', 'chroma_db'))
collection = client.get_or_create_collection('netflex_faqs')

# Memory Client
memory_client = chromadb.PersistentClient(path=os.path.join(cwd, 'src', 'memory_db'))
chat_collection = memory_client.get_or_create_collection("chat_memory")
subscription_collection = memory_client.get_or_create_collection("subscription")

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

@tool
def update_subscription_tool(customer_id: str, new_plan: str):
    """A function that updates the customer's subscription plan
    
    Args:
        customer_id (str): The customer's username
        new_plan (str): The new subscription plan to set, only 3 values accepted: ["No Plan", "Basic", "Standard", "Premium"]

    Returns:
        str: Message indicating whether subscription was added or updated
    """
    add_or_update_subscription(
        customer_id=customer_id,
        subscription_plan=new_plan
    )
    return f"Updated subscription for {customer_id} to {new_plan}"

@tool
def load_customer_subscription_tool(customer_id: str):

    """A tool that loads the customer's current subscription

    Args:
        customer_id (str): The customer's username

    Returns:
        dict: The customer's plan
    """
    return get_subscription(customer_id=customer_id)

# helper functions
def add_or_update_subscription(customer_id: str, subscription_plan: str):
    # Check if customer exists
    existing = subscription_collection.get(
        where={"user_id": customer_id}
    )
    # print(existing['ids'])
    if existing["ids"]:
        subscription_collection.update(
            ids=existing["ids"],
            metadatas=[{"user_id": customer_id, "subscription_plan": subscription_plan}],
        )

    else:
        subscription_collection.add(
            ids=[customer_id],
            documents=[customer_id],
            metadatas=[{"user_id": customer_id, "subscription_plan": subscription_plan}],
        )

def get_subscription(customer_id: str):
    result = subscription_collection.get(where={"user_id": customer_id})
    if result["metadatas"]:
        return result["metadatas"][0]["subscription_plan"]
    return "Customer not found in the database"

def reset_memory():
    chat_collection.delete(where={'role': 'customer'})
    chat_collection.delete(where={'role': 'agent'})

def remember_message(role: str, content: str, user_id: str):
    """Store a message in memory"""
    chat_collection.add(
        ids=[f"{role}_{hash(content)}"],
        documents=[content],
        metadatas=[{"role": role, "user_id": user_id},]
    )

def recall_messages(user_id: str, last_n: int = 5):
    """Retrieve last_n past messages"""
    chat_history = []
    
    results = chat_collection.get(include=["documents", "metadatas"], where={"user_id": user_id})
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