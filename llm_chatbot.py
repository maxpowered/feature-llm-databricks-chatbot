from langchain_databricks import ChatDatabricks
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# Initialize the ChatDatabricks model
chat_model = ChatDatabricks(
    endpoint="databricks-meta-llama-3-1-70b-instruct",
    temperature=0.7,
    max_tokens=250
)

# Create a prompt template
prompt_template = ChatPromptTemplate.from_template(
    "You are a helpful assistant. {chat_history}\nHuman: {human_input}\nAI:"
)

# Set up conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Create the LLMChain
llm_chain = LLMChain(
    llm=chat_model,
    prompt=prompt_template,
    memory=memory,
    verbose=True
)

# Function to interact with the chatbot
def chat_with_bot(user_input):
    response = llm_chain.predict(human_input=user_input)
    return response

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    bot_response = chat_with_bot(user_input)
    print("Bot:", bot_response)
