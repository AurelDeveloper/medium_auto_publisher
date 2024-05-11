from dotenv import load_dotenv
import os
import json
from pytube import Playlist
from langchain.document_loaders import YoutubeLoader

load_dotenv()

playlist_url = os.getenv('PLAYLIST_URL')

playlist = Playlist(playlist_url)

try:
    with open('./data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

for url in playlist.video_urls:
    # Check if the URL is already in the data
    if any(item['url'] == url for item in data):
        continue

    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
    docs = loader.load()

    # Append the data to the list
    data.append({
        'url': url,
        'metadata': docs[0].metadata,
        'transcript': docs[0].page_content
    })

# Write the data back to the JSON file
with open('./data.json', 'w') as f:
    json.dump(data, f)