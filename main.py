import openai
from dotenv import load_dotenv
from os import environ
load_dotenv()

openai.api_key=environ.get('OPENAI_API_KEY')

# Pre-defined Prompts
greetings_prompt = "Make a response saying: 'Hello! I am an AI Powered Language Translator Tool. (Type 'END' if you wish to close the Tool anytime !)'"
insert_language_prompt = "Make a response saying: 'Kindly specify the language you would like your text to be translated into?'"
insert_text_prompt = "Make a response saying: 'Kindly insert the Text.'"
ending_prompt = "Make a response saying: 'Thank You!.'"

# Greetings Prompt
# Roles can be system/user/assistant (Refer Documentation)
conversations = [
    {"role": "system", "content": "You are an AI assistant that performs Language Translation."},
    {"role": "user", "content": greetings_prompt},
]
greetings_prompt_response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=conversations
)
# We keep appending the responses to store the conversation history so that the model can refer to these for generating future prompts.
conversations.append({"role": "assistant", "content": greetings_prompt_response.choices[0].message.content})
print('AI: ', greetings_prompt_response.choices[0].message.content)

# Prompt AI to ask user in what language the text needs to be converted to
conversations.append({"role": "user", "content": insert_language_prompt})
language_prompt_response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=conversations
)
conversations.append({"role": "assistant", "content": language_prompt_response.choices[0].message.content})
print('AI: ', language_prompt_response.choices[0].message.content)


chat_continue = True

# Take user input for Language Query Response
user_input = input("You: ")
conversations.append({"role": "user", "content": user_input})
if user_input.lower() == 'end':
    chat_continue = False


while chat_continue:
    # Prompt User to input Text
    conversations.append({"role": "user", "content": insert_text_prompt})
    text_prompt_response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=conversations
    )
    conversations.append({"role": "assistant", "content": text_prompt_response.choices[0].message.content})
    print('AI: ', text_prompt_response.choices[0].message.content)

    # Get user input
    user_input = input("You: ")

    if (user_input.lower() == 'end'):
        break

    # Add user message to the conversation
    message = 'Translate: {}'.format(user_input) 
    conversations.append({"role": "user", "content": message})

    # Generate a response from the model
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversations
    )

    # Extract and print the model's reply
    reply = response.choices[0].message.content
    print("AI:", reply)

    # Add model's response to the conversation
    conversations.append({"role": "assistant", "content": reply})

# Prompt to Stop the AI tool
conversations.append({"role": "user", "content": ending_prompt})
endingPromptResponse = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=conversations
)
conversations.append({"role": "assistant", "content": language_prompt_response.choices[0].message.content})
print('AI: ', endingPromptResponse.choices[0].message.content)