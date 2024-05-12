from dotenv import load_dotenv
import os
import json
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama
from collections import Counter

load_dotenv()

article_prompt = os.getenv('ARTICLE_PROMPT')
description_prompt = os.getenv('DESCRIPTION_PROMPT')
all_tags = os.getenv('TAGS').split(',')

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
    ollama_description = ollama.invoke(formatted_prompt)
    return ollama_description.content.split('\n\n', 1)[1]

def generate_tags(article, all_tags):
    words = article.split()
    tag_counts = Counter(tag for tag in words if tag in all_tags)
    most_common_tags = [tag for tag, _ in tag_counts.most_common(5)]
    return most_common_tags

with open('./data.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item.get('processed', False):
        continue

    item['article'] = generate_article_ollama(transcript=item['transcript'])
    item['ollama_description'] = generate_description_ollama(transcript=item['transcript'])
    item['tags'] = generate_tags(item['article'], all_tags)
    item['processed'] = True

with open('./data.json', 'w') as f:
    json.dump(data, f)