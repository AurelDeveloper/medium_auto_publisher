from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

token = os.getenv('TOKEN')

# Load the data from the JSON file
with open('./data.json', 'r') as f:
    data = json.load(f)

for item in data:
    # Check if the video has already been uploaded
    if item.get('uploaded', False):
        continue

    article = item['article']
    title = item['metadata']['title']
    description = item['metadata']['description']
    thumbnail = item['metadata']['thumbnail_url']

    # Get your user ID
    response = requests.get('https://api.medium.com/v1/me', headers={'Authorization': f'Bearer {token}'})
    user_id = response.json()['data']['id']

    # Create a post
    post_data = {
        'title': title,
        'contentFormat': 'markdown',
        'content': f'![{title}]({thumbnail})\n\n{article}',
        'publishStatus': 'public',
        'tags': ['programming', 'python'],  # Add your own tags
    }
    response = requests.post(f'https://api.medium.com/v1/users/{user_id}/posts', headers={'Authorization': f'Bearer {token}'}, json=post_data)

    # Check the response
    if response.status_code == 201:
        print('Post created successfully')
        item['uploaded'] = True
    else:
        print('Failed to create post:', response.text)
        break

# Write the data back to the JSON file
with open('./data.json', 'w') as f:
    json.dump(data, f)