from crewai import Crew, Process
from .Agents import Agents
from .Tasks import Tasks
from . import utils
import os
from dotenv import load_dotenv
load_dotenv()

agents = Agents()
tasks = Tasks()

# Our Agents
customer_support_agent = agents.customer_support_agent()
support_quality_agent = agents.support_quality_agent()

# Our Tasks
case_resolution = tasks.case_resolution(
    agent=customer_support_agent,
    tools=[
        utils.retrive_docs_tool,
        utils.update_subscription_tool,
        utils.load_customer_subscription_tool,
    ]
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
    verbose=True,
)

def chat_crew(customer_id, customer_name, customer_question):
    utils.remember_message(
        role="customer",
        content=customer_question,
        user_id=customer_id,
    )
    
    results = netflex_support_crew.kickoff(
        inputs={
            "customer_id": customer_id,
            "customer_name": customer_name,
            "question": customer_question,
            "chat_history": utils.recall_messages(user_id=customer_id),
        }
    )

    return results.raw
