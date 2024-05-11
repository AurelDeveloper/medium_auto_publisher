from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

token = os.getenv('TOKEN')

with open('./data.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item.get('uploaded', False):
        continue

    article = item['article']
    title = item['metadata']['title']
    description = item.get('description', '')
    thumbnail = item['metadata']['thumbnail_url']
    keywords = item.get('keywords', [])[:5]

    response = requests.get('https://api.medium.com/v1/me', headers={'Authorization': f'Bearer {token}'})
    user_id = response.json()['data']['id']

    post_data = {
    'title': title,
    'contentFormat': 'markdown',
    'content': f'![{title}]({thumbnail})\n\n{description}\n\n{article}',
    'publishStatus': 'public',
    'tags': keywords,
    }
    response = requests.post(f'https://api.medium.com/v1/users/{user_id}/posts', headers={'Authorization': f'Bearer {token}'}, json=post_data)

    if response.status_code == 201:
        print('Post created successfully')
        item['uploaded'] = True
    else:
        print('Failed to create post:', response.text)
        break

with open('./data.json', 'w') as f:
    json.dump(data, f)