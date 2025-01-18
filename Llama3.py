import os
from groq import Groq

# Initialize the client
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )
client = Groq(api_key="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")


# Take user input dynamically
user_input = input("Enter your question or message: ")

# Create a chat completion request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="llama3-8b-8192",
)

# Print the response from the model
print("Response:", chat_completion.choices[0].message.content)

