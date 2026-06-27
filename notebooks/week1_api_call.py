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

questions = [
    'When did India get Independence?',
    'What is the history of fourth of July in USA?',
    'Who invented electricity?',
    'Which are the biggest cities on the West coast of USA?',
    'Which is the best?']

for q in questions:
    print(ask_llm(q))