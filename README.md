# medium_auto_publisher

**Example generated article:** https://medium.com/@aurel_code/why-everyone-hates-php-and-why-you-should-too-b7d9db21e9c9

The `main.py` is set to download the transcript from a specific YouTube video URL. To use a different video, change the `video_url` variable to your desired YouTube video URL.

## Functions

- `download_video()`: Downloads the YouTube video transcript and stores it in the `data` list.
- `generate_content()`: Generates an article from the video transcript using the LangChain API.
- `publish_content()`: Publishes the generated article on Medium.

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
