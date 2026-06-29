from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def ask_llm(question, user_prompt):
    response = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=1024,
        system = user_prompt,
        messages=[{'role': 'user', 'content': question}]
    )
    return response.content[0].text

user_prompt = ('You are a competitive intelligence analyst who responds only in bullet points')
questions = [
    'When did India get Independence?',
    'What is the history of fourth of July in USA?',
    'Who invented electricity?',
    'Which are the biggest cities on the West coast of USA?',
    'Which is the best?']

for q in questions:
    print(ask_llm(q, user_prompt))