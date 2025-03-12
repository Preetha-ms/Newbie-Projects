# Chatbot Project

Welcome to the **Chatbot Project**! This repository contains a simple AI-powered chatbot implemented using **FastAPI, CrewAI, and Ollama**. The chatbot serves as an interactive assistant, leveraging **local AI models** to process and respond to user queries.

## 📌 Project Structure
```
AI/
 ├── Chatbot/
 │   ├── chatbot.py          # The main backend API
 │   ├── index.html          # The frontend UI
 │   ├── requirements.txt    # List of dependencies
 ├── README.md               # Project documentation
```

## 🚀 Getting Started
To use or enhance this project, follow these steps:

### 1️⃣ **Set Up Anaconda & Create a Conda Environment**
This project uses **Anaconda Navigator** to manage dependencies and environments.

#### **Install Anaconda (if not already installed)**
Download and install Anaconda from [here](https://www.anaconda.com/download/).

#### **Create a New Conda Environment**
To ensure dependencies are properly managed, create a virtual environment:
```bash
conda create --name chatbot_env python=3.12
```
Activate the environment:
```bash
conda activate chatbot_env
```

### 2️⃣ **Install Required Dependencies**
The `requirements.txt` file contains all the necessary libraries for this project. Install them using:
```bash
pip install -r requirements.txt
```
This will install:
- **FastAPI** – Framework for building APIs
- **CrewAI** – AI agent framework for managing conversations
- **CrewAI Tools** – Additional tools for CrewAI
- **Uvicorn** – ASGI server for FastAPI
- **LiteLLM** – Lightweight LLM model integration
- **Ollama** – Local AI model execution

### 3️⃣ **Run the Chatbot Backend**
Start the FastAPI server by running:
```bash
python AI/Chatbot/chatbot.py
```
By default, the API will run on `http://127.0.0.1:8000`

### 4️⃣ **Understanding the Chatbot Architecture**
The chatbot works by using **AI agents** powered by CrewAI, with **Ollama** as the underlying LLM (local language model). Here’s how it works:
- The chatbot API receives a request from the frontend.
- CrewAI creates an **Agent** that handles user interactions.
- **Ollama (Phi-4 model)** processes the request and generates a response.
- The chatbot responds back via FastAPI.

### 5️⃣ **Access the Chatbot Interface**
Open `index.html` in a browser or use a simple HTTP server:
```bash
python -m http.server 8080
```
Then, visit: `http://127.0.0.1:8080/index.html`

## 🎯 Purpose of Key Files
- **`chatbot.py`**: Implements the FastAPI backend, initializes CrewAI agents, and integrates with Ollama.
- **`index.html`**: Frontend UI for interacting with the chatbot.
- **`requirements.txt`**: List of required libraries to ensure consistency across environments.

## 🤝 Contributing
Pull requests are welcome! If you’d like to enhance this project, feel free to fork the repository, make changes, and submit a PR.

## 📜 License
This project is licensed under the MIT License.

---
📢 **Enjoy building with AI! Feel free to customize and improve this chatbot!** 🚀

