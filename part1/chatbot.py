from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage,AIMessage,SystemMessage

print("___welcome to the ai app press 0 to exit___")
print("1. Funny")
print("2. angry")
print("3 sarcastic")
print("4. Sad")
print("5 Romantic")


personalities = {
    "1": "You are a funny and witty AI agent, if asked about any topic you have to answer with jokes and make sure that answer is related to the topic",
    "2": "You are an angry AI agent, if asked about any topic you have to answer with anger and make sure that answer is related to the topic",
    "3": "You are a sarcastic AI agent, if asked about any topic you have to answer with sarcasm and make sure that answer is related to the topic",
    "4": "You are a sad AI agent, if asked about any topic you have to answer with sadness and make sure that answer is related to the topic",
    "5": "You are a romantic AI agent, if asked about any topic you have to answer with romance and make sure that answer is related to the topic",


}
choice = input("\n Choose personality(1-5):")
if choice not in personalities:
    print("Invalid choice")
    exit()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
messages =[
    SystemMessage(content=personalities[choice])
]
while True:
    prompt = input("Enter your question:")
    messages.append(HumanMessage(content=prompt))
    if prompt =="0":
        print("\n thank you for using the chatbot")
        break
    response = model.invoke(messages) 
    messages.append(AIMessage(content= response.content[0]["text"]))
    print(response.content[0]["text"])
    #print(messages)