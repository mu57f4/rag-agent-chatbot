from crewai import Agent, Task

class Tasks:

    def case_resolution(self, agent: Agent, tools: list) -> Task:
        return Task(
            description="\n".join([
                "You will recive a chat history between you and the customer {customer_name}",
                "\n```{chat_history}```\n",
                "and super important question:"
                "\n```{question}```\n",
                "and this is the customer's id:"
                "\n```{customer_id}```\n"
                "ask the customer if they want to update their plan, you have access to their subscription using the load_customer_subscription tool",
                "if the customer wants to update their plan, you should do the update using the update_subscription tool",
                "if the customer ask for plan update, don't search for relevant docs, just update the plan",
                "if the customer ask for cancling their plan, update their plan to No Plan",
                "Answer the customer question considering the older messages from the chat history",
                "if you think the customer support quesiton in not a technical one, you should be a sweet talker and chat with the customer if he/she want's to",
                "Make sure to retrive and use the related docs from out local database to give the best support possible",
                "if you didn't find the answer in the retrived docs, don't make any assumptions, just tell the customer I don't know the answer yet",
                "if the question is not releated to the docs, DO NOT ANSWER THE QUESTION."
                "You must provide a complete and accurate response to the customer's question",
                "Your answer should be in MarkDown and in general chat way",
                "if the customer question is a general chat, you should chat the customer to the customer with super friendly and respectable response and ask customer if he/she need help?"
            ]),
            expected_output="\n".join([
                "A detailed, informative response to the customer question",
                "Ensure the answer is complete",
                "Leaving no question not answered",
                "maintain a helpful and super friendly tone throughout",
                "if the customer question is a general chat, do not use the docs retrival tool, and chat the customer with super friendly response and ask if he/she need help?"
            ]),
            agent=agent,
            tools=tools
        )
    
    def resolution_quality(self, agent: Agent, remember_message_func: any) -> Task:
        return Task(
            description="\n".join([
                "Review the reponse from customer support agent for customer {customer_name} question",
                "Ensure that the customer support agent answered the question",
                "Ensure that the answer is comprehensive, accurate",
                "Verify that all parts of the customer question have been addressed",
                "Ensure that the response leaves no questions unanswered."
                "the customer support agent should answer the customer non-techincal questions and should not ignore them",
            ]),
            expected_output="\n".join([
                "Just a Final informative response",
                "The response should be JUST the final customer answer without any thoughts"
                "The response should fully address the customer question",
            ]),
            agent=agent,
            callback=lambda output: remember_message_func("agent", output.raw, user_id=f"agent_{hash(output.raw)}"),
        )