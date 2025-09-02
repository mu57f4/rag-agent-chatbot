import chromadb
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("CHROMA_API_KEY") 


local = chromadb.PersistentClient(path="chroma_db")
col = local.get_collection("netflex_faqs")

data = col.get(include=["documents"])

cloud = chromadb.CloudClient(api_key=api_key)
dst = cloud.get_or_create_collection("netflex_faqs")

dst.add(
    ids=data["ids"],
    documents=data["documents"],
)
