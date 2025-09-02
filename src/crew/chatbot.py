from crewai import Crew, Process
from Agents import Agents
from Tasks import Tasks
import utils
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agents = Agents()
tasks = Tasks()

# Our Agents
customer_support_agent = agents.customer_support_agent()
support_quality_agent = agents.support_quality_agent()

# Our Tasks
case_resolution = tasks.case_resolution(
    agent=customer_support_agent,
    tools=[utils.retrive_docs_tool]
    )
resolution_quality = tasks.resolution_quality(
    agent=support_quality_agent,
    remember_message_func=utils.remember_message
    )

# Our Crew
netflex_support_crew = Crew(
    agents=[customer_support_agent, support_quality_agent],
    tasks=[case_resolution, resolution_quality],
    process=Process.sequential,
    verbose=False,
)

def chat_crew(customer_name, customer_question):
    
    utils.remember_message(
        role="customer",
        content=customer_question
    )
    
    results = netflex_support_crew.kickoff(
        inputs={
            "customer_name": customer_name,
            "question": customer_question,
            "chat_history": utils.recall_messages(),
        }
    )

    return results.raw
