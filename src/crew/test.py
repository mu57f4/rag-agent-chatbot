from chatbot import chat_crew
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit"]:
        print('==== end of chat ====')
        break
     
    answer = chat_crew('Mustafa Ahmed', user_input)
    print(answer)

