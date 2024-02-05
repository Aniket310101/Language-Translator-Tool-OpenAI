import openai
from dotenv import load_dotenv
from os import environ

def initialize_openai():
    load_dotenv()
    openai.api_key = environ.get('OPENAI_API_KEY')

def set_system_context(conversations): 
    # the "system" role is used to provide context to the model.
    conversations.append({"role": "system", "content": "You are an AI assistant that performs Language Translation."})

def get_model_response(model, conversations):
    response = openai.chat.completions.create(
        model=model,
        messages=conversations
    )
    return response.choices[0].message.content

def initialize_model(model, conversations, role, message):
    # Role can be system/user/assistant (Refer Documentation)
    conversations.append({"role": role, "content": message})
    # Initialize model
    response = get_model_response(model, conversations)
    # We keep appending the responses to store the conversation history so that the model can refer to prior responses for generating future prompts.
    conversations.append({"role": "assistant", "content": response})
    return response

def initialize_greetings_prompts(conversations):
    # Greetings Prompt
    greetings_prompt = "Make a response saying: 'Hello! I am an AI Powered Language Translator Tool. (Type 'END' if you wish to close the Tool anytime !)'"
    greetings_prompt_response = initialize_model("gpt-3.5-turbo", conversations, 'user', greetings_prompt)
    print('AI: ', greetings_prompt_response)

def initialize_language_query_prompt(conversations):
  # Initialize Prompt ask user in what language the text needs to be converted to
  insert_language_prompt = "Make a response saying: 'Kindly specify the language you would like your text to be translated into?'"
  language_prompt_response = initialize_model("gpt-3.5-turbo", conversations, 'user', insert_language_prompt)
  print('AI: ', language_prompt_response)

def get_user_input_for_language_query(conversations, chat_continue):
    # Take user input for Language Query Response
    user_input = input("You: ")
    conversations.append({"role": "user", "content": user_input})
    if user_input.lower() == 'end':
        chat_continue = False

def initialize_input_text_prompt(conversations):
    # Initialize prompt to ask user to input text that requires translation
    insert_text_prompt = "Make a response saying: 'Kindly insert the Text.'"
    text_prompt_response = initialize_model("gpt-3.5-turbo", conversations, 'user', insert_text_prompt)
    print('AI: ', text_prompt_response)

def initialize_translation_prompt(conversations, user_input):
    # Initialize prompt to Translate text
    message = 'Translate: {}'.format(user_input) 
    response = initialize_model("gpt-3.5-turbo", conversations, 'user', message)
    print("AI:", response)
    

def initialize_end_prompt(conversations):
    # Initialize ending Prompt
    ending_prompt = "Make a response saying: 'Thank You!.'"
    ending_prompt_response = initialize_model("gpt-3.5-turbo", conversations, 'user', ending_prompt)
    print('AI: ', ending_prompt_response)

def main():
    initialize_openai()
    conversations = []
    set_system_context(conversations)
    initialize_greetings_prompts(conversations)
    initialize_language_query_prompt(conversations)
    chat_continue = True
    get_user_input_for_language_query(conversations, chat_continue)
    while chat_continue:
        # Initialize query prompt to input text
        initialize_input_text_prompt(conversations)
        # Get user input
        user_input = input("You: ")
        if (user_input.lower() == 'end'):
            break
        # Translate Prompt
        initialize_translation_prompt(conversations, user_input)

    # Initialize ending prompt when user asks to stop
    initialize_end_prompt(conversations)

if __name__ == "__main__":
    main()