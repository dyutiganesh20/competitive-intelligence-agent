from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def ask_llm(question):
    response = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=1024,
        messages=[{'role': 'user', 'content': question}]
    )
    return response.content[0].text

print(ask_llm('What are the three biggest risks of an AI agent system?'))