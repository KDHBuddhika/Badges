import tkinter as tk
from tkinter import scrolledtext

# Chatbot response logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm a bot, but I'm doing great! How can I help you?"
    elif "your name" in user_input:
        return "I am ChatBot, your virtual assistant!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Please ask something else."

# Function to handle user input and chatbot response
def handle_user_input():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    # Display user input in chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    
    # Get chatbot response
    response = chatbot_response(user_input)
    
    # Display chatbot response in chat window
    chat_window.insert(tk.END, "ChatBot: " + response + "\n\n")
    
    # Scroll to the bottom
    chat_window.yview(tk.END)
    
    # Clear the input field
    entry.delete(0, tk.END)
    
    # If the user says "bye", close the application
    if "bye" in user_input.lower():
        root.after(1000, root.quit)

# Setting up the GUI with Tkinter
root = tk.Tk()
root.title("ChatBot GUI")
root.geometry("400x500")

# Create a chat display window (ScrolledText widget)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry box for user input
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

# Create a button to submit user input
submit_button = tk.Button(root, text="Send", command=handle_user_input)
submit_button.pack(pady=5)

# Allow pressing 'Enter' to submit the input
entry.bind("<Return>", lambda event: handle_user_input())

# Run the Tkinter event loop
root.mainloop()
