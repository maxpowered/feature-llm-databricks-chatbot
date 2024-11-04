Simple LLM Bot built with Python for Databricks

This Python script sets up a chatbot using the LangChain library and the Databricks ChatDatabricks model, which helps it remember what you talked about in previous messages. The bot keeps chatting with you based on your input until you decide to exit the conversation.

Added error handling: The script attempts to generate a response from the chatbot up to three times if an error occurs. If successful, it returns the response. If all attempts fail, it returns a friendly error message to the user instead of crashing the program
