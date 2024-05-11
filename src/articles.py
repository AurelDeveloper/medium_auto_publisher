from dotenv import load_dotenv
import os
import json
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama

load_dotenv()

prompt = os.getenv('PROMPT')

def generate_article_ollama(transcript, template=prompt, model="llama3"):
    prompt = ChatPromptTemplate.from_template(template)
    formatted_prompt = prompt.format_messages(transcript=transcript)
    ollama = ChatOllama(model=model, temperature=0.1)
    article = ollama.invoke(formatted_prompt)
    return article.content.split('\n\n', 1)[1] 

with open('./data.json', 'r') as f:
    data = json.load(f)

for item in data:
    item['article'] = generate_article_ollama(transcript=item['transcript'])

with open('./data.json', 'w') as f:
    json.dump(data, f)