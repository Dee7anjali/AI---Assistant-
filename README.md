# AI Voice Assistant

A modular, Python-based virtual assistant that executes tasks through voice commands. This project integrates speech recognition, text-to-speech, web APIs, and local data retrieval.

## Features

* **Time & Date:** Responds to queries about the current time and calendar date.
* **Web Search:** Provides summaries of public figures or topics using Wikipedia.
* **Media Playback:** Automatically opens and plays YouTube videos/music via `pywhatkit`.
* **Personal Data Retrieval:** Accesses and speaks pre-configured information (e.g., bank account numbers) based on voice triggers.

## Prerequisites

To run this project, you will need Python 3 installed. Install the necessary dependencies via pip:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyaudio

```

## Setup & Configuration

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git

```


2. **Configure Data:** Open the script and modify the `bank_account_numbers` dictionary to include your own labels and identifiers.
3. **Permissions:** Ensure your operating system allows your terminal or code editor microphone access.

## Usage

Run the script from your terminal:

```bash
python assistant.py

```

Once initialized, the assistant will listen for commands. Common examples include:

* "What time is it?"
* "What is the date?"
* "Play [song name]"
* "Who is [person]?"
* "What is my [bank name] account number?"

## ⚠️ Security Warning

**Data Privacy:** This project stores personal information (like bank account numbers) in the source code.

* **DO NOT** push your local version containing real sensitive data to a public GitHub repository.
* Use environment variables or a configuration file that is added to your `.gitignore` to keep personal data off the cloud.
