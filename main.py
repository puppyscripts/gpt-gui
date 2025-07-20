import tkinter as tk
from tkinter import scrolledtext
import os
from openai import OpenAI

# Clear Terminal
os.system('cls')

# Initialize OpenAI API
client = OpenAI(
    api_key="enter-api-key-here"  # Ensure your API key is set in the environment variables
)

def get_response(prompt):
    try:
        # Use the Responses API to generate text
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions="You are an advanced AI chatbot.",
            input=prompt
        )
        return response.output_text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# GUI Setup
def send_message(event=None):  # Add event parameter for keybind compatibility
    user_input = user_entry.get()
    chat_area.insert(tk.END, f"You: {user_input}\n\n")
    user_entry.delete(0, tk.END)

    bot_response = get_response(user_input)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")

    # Automatically scroll to the bottom
    chat_area.see(tk.END)

root = tk.Tk()
root.title("AI Chatbot")

# Styling changes
root.configure(bg="#2c2c2c")  # Dark grey background
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, bg="#2c2c2c", fg="white", font=("Arial", 12))
chat_area.pack(pady=10)

user_entry = tk.Entry(root, width=40, bg="#2c2c2c", fg="white", font=("Arial", 12))
user_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message, bg="#444444", fg="white", font=("Arial", 12))
send_button.pack(pady=5)

# Bind Enter key to send_message function
root.bind("<Return>", send_message)

root.mainloop()
