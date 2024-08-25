# Motivational Bard Hackathon Submission

## Introduction

Motivational Bard is a simple Python-based application that provides developers with motivational quotes tailored to their programming journey. The application uses Google Generative AI to generate unique and inspiring messages at specified intervals. Users can set their preferred programming language and notification frequency through the starting UI.

## Installation preface
You can either install the required packages and run the .py file OR build the .exe file yourself. Keep on reading for the installation process.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.10 or above
- Access to a Google Generative AI API key

## Installation running the .py file

### 1. Clone the Repository

```bash
git clone https://github.com/AntoMakh/motivational-bard-hackathon-submission.git
cd motivational-bard-hackathon-submission
```

### 2. Download the required packages using pip
```bash
pip install -r requirements.txt
```

### 3. Set up the environment variable
Create a .env file in the root directory based on the provided .env.example file. You will need to add your Google Generative AI API key here:
```makefile
API_KEY=your_google_generativeai_api_key
```

### 4. Running the application
To run the application, simply execute the script:
```bash
python src/motivational_bard.py
```

## Installation through building the .exe file

### 1. Make sure you have pyinstaller downloaded
```bash
pip install pyinstaller
```

### 2. If you are missing packages, modify the .spec file accordingly, such as changing the hidden_imports attributes

### 3. Build the executable
```bash
pyinstaller --clean --noconfirm motivational_bard.spec
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.




