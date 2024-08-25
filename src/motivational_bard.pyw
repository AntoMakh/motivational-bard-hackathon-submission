import os
import time
import threading
import tkinter as tk
from tkinter import simpledialog
from plyer import notification
from pystray import Icon, Menu, MenuItem
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCfglMbp2x-4kHxFi53L-uiIwynvvtxATA")

model = genai.GenerativeModel('gemini-1.5-flash')

running = True

def get_motivational_quote(language):
    try:
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
        timeout=10
    )

def run_background_task(language, frequency):
    global running
    while running:
        display_notification(language)
        time.sleep(frequency)
def on_quit(icon, item):
    global running
    running = False
    icon.stop()
    os._exit(0)

def start_app(language, frequency):
    root = tk.Tk()
    root.withdraw()

    thread = threading.Thread(target=run_background_task, args=(language, frequency))
    thread.daemon = True
    thread.start()

    image = Image.new("RGB", (64, 64), color=(73, 109, 137))

    menu = Menu(MenuItem("Quit", on_quit))
    icon = Icon("MotivationApp", image, menu=menu)
    icon.run()

def show_preferences_window():
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Preferences")

    language_label = tk.Label(root, text="Fill in the blank: I am a _____ developer. (optional)")
    language_label.pack(pady=5)
    language_entry = tk.Entry(root)
    language_entry.pack(pady=5)

    frequency_label = tk.Label(root, text="Frequency of notification (in seconds):")
    frequency_label.pack(pady=5)
    frequency_entry = tk.Entry(root)
    frequency_entry.pack(pady=5)

    start_button = tk.Button(root, text="Start", command=lambda: start_button_clicked(root, language_entry, frequency_entry))
    start_button.pack(pady=10)

    root.mainloop()

def start_button_clicked(root, language_entry, frequency_entry):
    language = language_entry.get()
    frequency = int(frequency_entry.get())

    root.destroy()
    start_app(language, frequency)

if __name__ == "__main__":
    show_preferences_window()
