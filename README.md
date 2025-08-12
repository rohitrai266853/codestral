# Codestral Chat Client

A Python CLI tool to chat with the Codestral model, supporting multi-lines inputs and code pasting.

## Features

- Multi-line input support (type `END` to finish input on a new line).
- Maintains conversation history.
- Exit by typing `exit`.

## Usage

1. Run the script as :
    ```bash
    python3 mistral.py
    ```

2. Replace the varaible `API_KEY` with your own Codestral API key.

3. After you input your prompt, press enter and type `END` and enter again.

4. This feature is provided so you can paste your code as is. At the end, remember to type `END` always on a new line.

## Requirements

- Make sure the `requests` library is installed, if not run the commmand `pip install requests`.
