# Language Translator Tool
- This is an AI Powered Language Translator tool that uses OpenAI Text Generation Model.
- Motive of this project is to understand the implementation of OpenAI's Text Generation Model using Chat Completions API.
- Model used: gpt-3.5-turbo  
<br/><br/>

# Key Concepts

## OpenAI
OpenAI is an artificial intelligence research lab that develops cutting-edge AI technologies. Focused on advancing digital intelligence, OpenAI creates powerful language models like GPT-3, capable of understanding and generating human-like text. The organization aims to ensure AI benefits all of humanity and avoids harmful consequences through responsible development and deployment. For more information [click here](https://platform.openai.com/docs/overview)

## Text Generation Models
OpenAI's text generation models (often called generative pre-trained transformers or large language models) have been trained to understand natural language, code, and images. The models provide text outputs in response to their inputs. The inputs to these models are also referred to as "prompts". Designing a prompt is essentially how you “program” a large language model model, usually by providing instructions or some examples of how to successfully complete a task. For more information [click here](https://platform.openai.com/docs/guides/text-generation)
<br/>

## Chat Completions API
The Chat Completions API by OpenAI enables developers to integrate natural language conversations with AI models like GPT-3. Users can create interactive chat-based applications, virtual assistants, or conversational agents by sending a series of messages as input and receiving model-generated responses, allowing dynamic and context-aware interactions in diverse applications. For more information [click here](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
<br/><br/>

## Tokens
In the context of text generation models, "tokens" refer to units of text that the model processes. A token can be as short as one character or as long as one word, depending on the model and the tokenization strategy used. Tokenization is the process of breaking down text into these units for analysis.

For example, in the sentence "ChatGPT is great!", if we tokenize it at the word level, the tokens would be: ["ChatGPT", "is", "great", "!"]. If we tokenize it at the character level, the tokens might be: ["C", "h", "a", "t", "G", "P", "T", " ", "i", "s", " ", "g", "r", "e", "a", "t", "!"].
<br/><br/>

# Steps to Run the Tool
- Create a .env file with the following content:-<br>
```OPENAI_API_KEY=<YOUR-API-KEY>```
- Install openAI package<br>
```pip3 install openai```
- Run main.py file<br>


# Steps to Generate OpenAI Key
Follow [this](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt)

## Note:-
- As of Feb 5, 2024 OpenAI gives free credit upto $5
- Free credit expires after 3 months. (Even if free credit is not completely utilized)
- Here we have used gpt-3.5-turbo. As of 05 Feb 2024, it's pricing structure follows $0.0015 / 1K tokens.
- Check [here](https://openai.com/pricing) for official pricing structure.
