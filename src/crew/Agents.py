from crewai import Agent, LLM
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

class Agents:

    def __init__(self):
        self.chat_llm = LLM(
            model="gemini/gemini-2.5-flash",
            temperature=0.0,
        )
                
    def customer_support_agent(self) -> Agent: 
        return Agent(
            role="Customer Support Agent",
            goal="Be the most friendly and helpful support agent in your team",
            backstory="\n".join([
                "You are an AI Agent working for Netflex, Inc (netflex.com) for providing customer support for to {customer_name}",
                "{customer_name} is very important customer to your company",
                "You need to make sure that you provide the best support",
                "Provide a full complete ansewr without any assumptions.",
            ]),
            allow_delegation=False,
            llm=self.chat_llm,
            max_iter=5,
            max_execution_time=30,
            verbose=False
        )
    
    def support_quality_agent(self) -> Agent:
        return Agent(
            role="Customer Suport Quality Assurance Specialist",
            goal="\n".join([
                "Provde the best support quality assurance in your team",        
            ]),
            backstory="\n".join([
                "You are an AI Agent working for Netflex, Inc (netflex.com) for providing customer support quality assurace to {customer_name} case",
                "Ensure that the support agent is providing the best support to the customer",
                "You need to make sure the that support agent answered the question of the customer",
                "Even if the customer wants a general chat and didn't ask a techincal question, make sure it is answered and not ignored",
            ]),
            allow_delegation=False,
            llm=self.chat_llm,
            verbose=False,
    )
