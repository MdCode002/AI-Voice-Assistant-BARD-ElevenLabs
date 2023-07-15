
<p align="center">
    <h1 align="center">AI-Voice-Assistant-BARD-ElevenLabs</h1>
</p>


This project utilizes the `bardapi` and `elevenlabs` libraries to interact with an AI model and generate and play audio responses. The purpose of the project is to provide short and precise answers to user input.

## Author
 - Mouhamed Diouf : [@Medzo02](https://github.com/Medzo02)
## Prerequisites

Before running the project, ensure that you have the following requirements met:

- Python 3.x installed
- `bardapi` and `elevenlabs` libraries installed
- A valid API key for the `bardapi` library and `elevenlabs` .
- Install ffmpeg

## Installation

1. Clone the project repository:

   ```shell
   git clone https://github.com/Medzo02/AI-Voice-Assistant-BARD-ElevenLabs.git
2. Install the required libraries:
   ```shell
   pip install bardapi elevenlabs
3. Install ffmpeg
   ```shell
   choco install ffmpeg
4. Set up your api key
   - Open the project file main.py.
   - Replace set_api_key("YOUR-API-KEY") with your API key obtained from ELEVENLABS.
   - Update the line os.environ['_BARD_API_KEY'] = "YOUR-API-KEY" with your Bard API key.
   
