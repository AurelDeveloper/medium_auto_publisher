# medium_auto_publisher

This project converts YouTube videos into articles. It consists of three main scripts that are executed in the `main.py` file:

1. `download.py`: This script is responsible for downloading the YouTube videos. It uses the YouTube Data API to download the videos and extract the transcripts.

2. `articles.py`: This script generates articles and short descriptions from the downloaded YouTube transcripts. It uses Ollama with llama3 to generate the articles.

3. `upload.py`: This script uploads the generated articles to Medium. It uses the Medium API to publish the articles.

## Setup

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/AurelDeveloper/medium_auto_publisher.git
    cd medium_auto_publisher
    ```

2. Take a pull of Ollama docker image and run it:

    ```bash
    docker pull ollama/ollama
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
    ```

3. To start or stop the Ollama docker image:

    ```bash
    docker start ollama
    docker stop ollama
    ```

4. Add the llama3 LLM model in Ollama:

    ```bash
    curl http://localhost:11434/api/pull -d '{"name": "llama3"}'
    ```

5. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

6. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

7. Copy the `.env.example` file to `.env`:

    ```bash
    cp .env.example .env
    ```

8. Open the `.env` file and replace the placeholders with your actual values.

## Running the Project

To run the project, simply execute the `main.py` script:

```bash
python3 main.py
