import subprocess

# Run download_videos.py
subprocess.run(["python3", "./src/download.py"])

# Run generate_articles.py
subprocess.run(["python3", "./src/articles.py"])

# Run generate_articles.py
subprocess.run(["python3", "./src/upload.py"])