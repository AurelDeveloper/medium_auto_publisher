from dotenv import load_dotenv
import os
import requests
from langchain_community.document_loaders import YoutubeLoader
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama

load_dotenv()

video_url = "https://www.youtube.com/watch?v=ZQX4FLrm9ac&ab_channel=EricMurphy"
article_prompt = os.getenv('PROMPT')
token = os.getenv('TOKEN')

data = []

def download_video():
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True)
    docs = loader.load()

    data.append({
        'url': video_url,
        'metadata': docs[0].metadata,
        'transcript': docs[0].page_content,
    })

def generate_content():
    for item in data:
        article_prompt_template = ChatPromptTemplate.from_template(article_prompt)
        formatted_article_prompt = article_prompt_template.format_messages(transcript=item['transcript'])
        ollama = ChatOllama(model="llama3", temperature=0.1)
        item['article'] = ollama.invoke(formatted_article_prompt).content.split('\n\n', 1)[1]

def publish_content():
    for item in data:
        article = item['article']
        title = item['metadata']['title']
        thumbnail = item['metadata']['thumbnail_url']

        response = requests.get('https://api.medium.com/v1/me', headers={'Authorization': f'Bearer {token}'})
        user_id = response.json()['data']['id']

        post_data = {
            'title': title,
            'contentFormat': 'markdown',
            'content': f'![{title}]({thumbnail})\n\n{article}',
            'publishStatus': 'public',
        }
        response = requests.post(f'https://api.medium.com/v1/users/{user_id}/posts', headers={'Authorization': f'Bearer {token}'}, json=post_data)

        if response.status_code == 201:
            print('Post created successfully')
        else:
            print('Failed to create post:', response.text)
            break

def main():
    download_video()
    generate_content()
    publish_content()

if __name__ == "__main__":
    main()