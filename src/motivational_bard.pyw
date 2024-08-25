import os
import time
import threading
import tkinter as tk
from tkinter import simpledialog
from plyer import notification
from pystray import Icon, Menu, MenuItem
from PIL import Image
import google.generativeai as genai

# Configure the Generative AI client
genai.configure(api_key="AIzaSyCfglMbp2x-4kHxFi53L-uiIwynvvtxATA")

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Global flag to control the background thread
running = True

def get_motivational_quote(language):
    try:
        # Generate content using the model
        prompt = (
            f"I am a {language} developer. Give me a very short coding-related "
            "message to either motivate me, encourage me, remind me to not give up, "
            "about celebrating achievements, staying inspired, overcoming challenges. "
            "Make sure the answer is also different from your previous answers. Avoid using the line "
            "'every line of code'. The quote can be about building code, finding a bug, etc... Get creative."
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Keep coding, you're doing great!"

def display_notification(language):
    quote = get_motivational_quote(language)
    notification.notify(
        title="Motivational Quote",
        message=quote,
        app_name="Motivation App",
        timeout=10  # Notification will disappear after 10 seconds
    )

def run_background_task(language, frequency):
    global running
    while running:
        display_notification(language)
        time.sleep(frequency)  # Send a quote according to the frequency

def on_quit(icon, item):
    global running
    running = False  # Stop the background thread loop
    icon.stop()  # Stop the system tray icon loop
    os._exit(0)  # Forcefully terminate the program to ensure all threads are stopped

def start_app(language, frequency):
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()

    # Start background task in a new thread
    thread = threading.Thread(target=run_background_task, args=(language, frequency))
    thread.daemon = True  # Daemonize thread to exit on application close
    thread.start()

    # Create a simple icon for the system tray
    image = Image.new("RGB", (64, 64), color=(73, 109, 137))

    # Create the system tray icon and menu
    menu = Menu(MenuItem("Quit", on_quit))
    icon = Icon("MotivationApp", image, menu=menu)
    icon.run()

def show_preferences_window():
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Preferences")

    # Label and entry for programming language
    language_label = tk.Label(root, text="Fill in the blank: I am a _____ developer. (optional)")
    language_label.pack(pady=5)
    language_entry = tk.Entry(root)
    language_entry.pack(pady=5)

    # Label and entry for frequency
    frequency_label = tk.Label(root, text="Frequency of notification (in seconds):")
    frequency_label.pack(pady=5)
    frequency_entry = tk.Entry(root)
    frequency_entry.pack(pady=5)

    # Start button
    start_button = tk.Button(root, text="Start", command=lambda: start_button_clicked(root, language_entry, frequency_entry))
    start_button.pack(pady=10)

    root.mainloop()

def start_button_clicked(root, language_entry, frequency_entry):
    language = language_entry.get()
    frequency = int(frequency_entry.get())

    root.destroy()  # Close the preferences window
    start_app(language, frequency)

if __name__ == "__main__":
    show_preferences_window()
