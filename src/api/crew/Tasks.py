from crewai import Agent, Task

class Tasks:

    def case_resolution(self, agent: Agent, tools: list) -> Task:
        return Task(
            description="\n".join([
                "You are a customer support assistant handling conversations with {customer_name}.",
                "Here is the chat history between you and the customer:",
                "\n```{chat_history}```\n",
                "Here is the customer's current question:",
                "\n```{question}```\n",
                "And here is the customer's ID:",
                "\n```{customer_id}```\n",
                "----------------------------",
                "### Instructions:",
                "1. You have access to the customer's subscription using the `load_customer_subscription` tool.",
                "2. If the customer wants to update their plan, use the `update_subscription` tool directly (do NOT search docs).",
                "   - If they ask to cancel their plan, set their subscription to **No Plan**.",
                "3. When answering technical questions:",
                "   - First, retrieve and use relevant docs from our local database.",
                "   - If no relevant docs are found, say clearly: *'I don’t know the answer yet.'*",
                "   - Never make assumptions or provide unsupported answers.",
                "4. When the question is NOT related to the docs:",
                "   - Do NOT attempt to answer from your own knowledge.",
                "   - If it's about subscriptions, handle it with the tools.",
                "   - If it’s general small-talk, respond in a **friendly, respectful, and warm tone**, and ask if they need further help.",
                "5. Always consider the full conversation history when crafting your response.",
                "6. Always answer in **Markdown** format.",
                "7. You must provide a complete, accurate, and polite response to every customer question."
            ]),

            expected_output="\n".join([
                "A detailed, informative response to the customer question",
                "Ensure the answer is complete",
                "Leaving no question not answered",
                "do not use tools if the question is not related to the docs, or the customer didn't mention their subscription plan",
                "maintain a helpful and super friendly tone throughout",
                "if the customer question is a general chat, do not use the docs retrival tool, and chat the customer with super friendly response and ask if he/she need help?"
            ]),
            agent=agent,
            tools=tools
        )
    
    def resolution_quality(self, agent: Agent, remember_message_func: any) -> Task:
        return Task(
            description="\n".join([
                "Review the response from the customer support agent for customer {customer_name}'s input.",
                "If the input is a greeting or small-talk (e.g., 'hi', 'hello', 'thanks'), ensure the agent responds politely and naturally without over-elaboration.",
                "If the input is a greeting or small-talk and the agent responds politely and naturally without over-elaboration. pass the agent response to the customer without any changes.",
                "If the input is a question, ensure that the customer support agent answered it accurately, comprehensively, and covered all parts of the question.",
                "Ensure that the response leaves no relevant questions unanswered.",
                "The customer support agent should answer customer non-technical questions (like greetings or plan inquiries) politely and should not ignore them.",
            ]),
            expected_output="\n".join([
                "The response should be JUST the final customer-facing answer, without internal thoughts or reasoning.",
                "For greetings or small-talk: a short, polite, natural response is expected.",
                "For actual questions: the response should fully address the customer query, with accuracy and completeness.",
            ]),
            agent=agent,
            callback=lambda output: remember_message_func("agent", output.raw, user_id=f"agent_{hash(output.raw)}"),
        )