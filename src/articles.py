from dotenv import load_dotenv
import os
import json
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama

load_dotenv()

article_prompt = os.getenv('ARTICLE_PROMPT')
description_prompt = os.getenv('DESCRIPTION_PROMPT')

def generate_article_ollama(transcript, template=article_prompt, model="llama3"):
    article_prompt = ChatPromptTemplate.from_template(template)
    formatted_prompt = article_prompt.format_messages(transcript=transcript)
    ollama = ChatOllama(model=model, temperature=0.1)
    article = ollama.invoke(formatted_prompt)
    return article.content.split('\n\n', 1)[1] 

def generate_description_ollama(transcript, template=description_prompt, model="llama3"):
    description_prompt = ChatPromptTemplate.from_template(template)
    formatted_prompt = description_prompt.format_messages(transcript=transcript)
    ollama = ChatOllama(model=model, temperature=0.1)
    article = ollama.invoke(formatted_prompt)
    return article.content.split('\n\n', 1)[1]

with open('./data.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item.get('processed', False):
        continue

    item['article'] = generate_article_ollama(transcript=item['transcript'])
    item['description'] = generate_description_ollama(transcript=item['transcript'])
    item['processed'] = True

with open('./data.json', 'w') as f:
    json.dump(data, f)