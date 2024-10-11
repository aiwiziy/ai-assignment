# this is the api key for openai: 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
import openai
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.1")


def chat_with_gpt(api_key, prompt):
    openai.api_key = api_key
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    
    return response.choices[0].message['content'].strip()
    

def chat_with_olama(context, prompt):
    response = model.invoke(input=prompt, context=context)
    return response