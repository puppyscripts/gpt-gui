# GUI interface for GPT

This project is a gui interface for openai's gpt model. The is built using Python and features a graphical user interface (GUI) created with Tkinter.

## Features
- **Natural Language Understanding**: Powered by OpenAI's GPT model.
- **User-Friendly GUI**: Built with Tkinter for easy interaction.
- **Dynamic Response Generation**: Generates responses based on user input.

## Requirements
- Python 3.7+
- OpenAI Python SDK
- Tkinter (comes pre-installed with Python)

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install openai
   ```
3. Add your OpenAI API key in `main.py`:
   ```python
   openai.api_key = "your-api-key-here"
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Enter your message in the input field and click "Send".
- The chatbot will respond dynamically based on your input.

## License
This project is licensed under the MIT License.
